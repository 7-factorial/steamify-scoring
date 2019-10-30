from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.models import User
from django import db
from typing import Tuple, Optional, Any, Type, List
from django.utils import timezone

from .utils.misc import tla_from_fullId

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import json

from django.forms import modelform_factory
from .forms import PickTeamIdForm

from .utils.misc import score_instance_to_dict, makeEditLink
from .utils.dupe import getEntriesIfAlreadyExist

from .models import Team, ALL_EXCEPT_SPONT, Shared, Spont, ALL_COMPETS, update_allowed_devices



class EntryHomeView(LoginRequiredMixin, TemplateView):
    template_name = "steamify/entryhome.html"
    
    def get(self, request, *args, **kwargs):
        update_allowed_devices(request)
        return super().get(request, *args, **kwargs)


def all_entries_by_category():

    def name_and_dat(Compet):
        # type: (Type[Shared]) -> Tuple[str, list]
        return Compet.__name__, list(Compet.objects.all())

    return dict(map(name_and_dat, ALL_COMPETS))
    

def precalcTeam(team):
    # type: (Team) -> dict
    dat = team.three_averages()
    dat.update({
        "dotted_id": team.dotted_id,
        "team_obj": team,
        "tla": tla_from_fullId(team.dotted_id)
    })
    return dat

## Didn't need this because of js tablesorter
# def orderTeams(teams):
#     # type: (List[dict]) -> List[dict]
#     def keyfunc():
#         # type: (dict) -> str
#         fill_this
#     return sorted(teams, key=keyfunc)
    



class TeamBreakdownView(UserPassesTestMixin, TemplateView):
    template_name = 'steamify/teambreakdown.html'

    def test_func(self):
        user = self.request.user
        # probably unnecessarily redundant
        return user.is_staff and user.is_superuser

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        from .utils.teamscores import makeTeamScoreData
        context['team_score_data'] = map(makeTeamScoreData, Team.objects.all())

        return context


class AdminJudgeListView(UserPassesTestMixin, TemplateView):
    template_name = 'steamify/adminjudgelist.html'

    def test_func(self):
        user = self.request.user
        # probably unnecessarily redundant
        return user.is_staff and user.is_superuser

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        context['all_judge_objects'] = User.objects.all()
        context['nowdatets'] = 0 - timezone.now().timestamp()

        return context


class AdminStatusView(UserPassesTestMixin, TemplateView):
    template_name = 'steamify/adminstatus.html'

    def test_func(self):
        user = self.request.user
        # probably unnecessarily redundant
        return user.is_staff and user.is_superuser

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        ## Experimenting, but I don't think this will be the best way to do it.
        # context['Non_blank_Status'] = getUnblankStatus()

        context['all_entries_by_category'] = all_entries_by_category()
        context['all_team_objects'] = [precalcTeam(x) for x in Team.objects.all()]

        # TODO: set up a query for dupes (it will of course overlap with the 
        # non blank status query, but I will handle the non blank first
        # and the others later)
        return context


def create_and_update_get_success_url(self):
    if self.model.TLA == "FAKE_TLA_FOR_SPONT":
        partial = "spont"
    else:
        partial = self.model.TLA
    viewname = 'steamify:{}-view'.format(partial)
    return reverse(viewname, kwargs={
        "spontOrLong": self.kwargs['spontOrLong'],
        'full_team_id': self.kwargs["full_team_id"],
        "pk": self.object.id})


def getTeamFromReq(request):
    # if it can't find one, it will raise an exception, but that shouldn't happen here.
    ftid = request.resolver_match.kwargs["full_team_id"]
    return Team.objects.get(dotted_id=ftid)


def addTeamToContext(selfdata, context):
    """this is unfortunately mutating `context` to avoid extra code"""
    context['team'] = Team.objects.get(dotted_id=selfdata.kwargs['full_team_id'])
    return context


class GenericCreate(LoginRequiredMixin, CreateView):
    template_name = "steamify/generic_score_form.html"
    get_success_url = create_and_update_get_success_url
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        return addTeamToContext(self, context)

    def get(self, request, *args, **kwargs):
        update_allowed_devices(request)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # as per https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/#models-and-request-user
        inst = form.instance  # type: Shared 
        inst.judge = self.request.user
        inst.team = getTeamFromReq(self.request)

        ## Experimenting... I don't think this will end up being the best way to do it though.
        # inst.status_for_admin = ""
        # oldEntries = getEntriesIfAlreadyExist(inst)
        # if oldEntries:
        #     for ent in oldEntries:
        #         ent.status_for_admin = "probably_should_delete"
        #         ent.save()
        #     inst.status_for_admin = "probably_should_supersede_older_entry"
        #     # inst is saved later

        return super().form_valid(form)


# Maybe do public-facing list, edit, view, and delete IF I CAN limit it
# ALSO WE WOULD NEED TIME RESTRICTION. might not be worth it.
#  only view/eit your own
class GenericUpdate(LoginRequiredMixin, UpdateView):
    template_name = "steamify/generic_score_form.html"
    get_success_url = create_and_update_get_success_url
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        return addTeamToContext(self, context)

# class EngMiddleDelete(DeleteView):
#     model = EngMiddle
#     success_url = "/"   # if using reverse, must use reverse_lazy here as per docs. example:  # reverse_lazy('EngMiddle-list')

class GenericDetail(LoginRequiredMixin, generic.DetailView):
    template_name="steamify/genericdetail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['serial_keys_vals'] = score_instance_to_dict(kwargs['object'])
        context['premade_edit_link'] = makeEditLink(self.model.TLA, self.kwargs)
        # editname = 'steamify:{}-edit'.format(self.model.TLA)
        # context['premade_edit_link'] = reverse(editname, kwargs=self.kwargs)
        return addTeamToContext(self, context)


# class EngMidListView(generic.ListView):
#     model = EngMiddle
#     def get_queryset(self):
#         # We would change this to only list your own submissions.
#         return Question.objects.all()

def getPastSubmissionsInAllCompets(judgeInstance, spontOrLong):
    # type: (auth.models.User, str) -> Optional[dict]

    def _one(compet):
        # type: (db.models.model) -> Tuple[str, list]
        competData = list(compet.objects.filter(judge=judgeInstance))
        return compet.__name__, competData

    def _all():
        # type: () -> dict
        if spontOrLong == "spont":
            return dict([_one(Spont)])
        else:
            return dict(map(_one, ALL_EXCEPT_SPONT))
        
    resu = _all()
    if not any(resu.values()):
        return None
    else:
        return resu


class PickTeamIdView(LoginRequiredMixin, FormView):
    template_name = 'steamify/pickteamname.html'
    form_class = PickTeamIdForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        dotted_ids = list(Team.objects.values_list('dotted_id', flat=True).order_by('dotted_id'))   # pylint: disable=no-member
        context['sorted_team_ids'] = json.dumps(dotted_ids)
        context['past_submissions'] = getPastSubmissionsInAllCompets(self.request.user, self.kwargs['spontOrLong'])
        return context

    def form_valid(self, form):
        # as per https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/
        # This method is called when valid form data has been POSTed. It should return an HttpResponse.
        full_team_id = form.cleaned_data['full_team_id']
        # we know it's a valid team id, so we can parse it safely
        grade, comp_type, team_id_number = full_team_id.split(".")
        gct = grade + "." + comp_type
        spontOrLong = self.kwargs['spontOrLong']

        # This is bad url design :-/ but I don't want to refactor everything this late in the game
        if spontOrLong == "spont":
            url = "steamify:spont-add"
        else:
            url = "steamify:{}-add".format(gct)

        return HttpResponseRedirect(reverse(url,
                kwargs={'spontOrLong': spontOrLong, 'full_team_id': full_team_id}))
