from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.core import serializers
from django.contrib import auth
from django import db
from typing import Tuple

from django.contrib.auth.mixins import LoginRequiredMixin
import json

from django.forms import modelform_factory
from .forms import PickTeamIdForm

from .utils.misc import score_instance_to_dict, makeEditLink

from .models import Team, ALL_EXCEPT_SPONT, Shared



class EntryHomeView(LoginRequiredMixin, TemplateView):
    template_name = "steamify/entryhome.html"


def create_and_update_get_success_url(self):
    viewname = 'steamify:{}-view'.format(self.model.TLA)
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

    def form_valid(self, form):
        # as per https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/#models-and-request-user
        inst = form.instance  # type: Shared 
        inst.judge = self.request.user
        inst.team = getTeamFromReq(self.request)
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
    # type: (auth.models.User, str) -> dict

    def _one(compet):
        # type: (db.models.model) -> Tuple[str, list]
        competData = list(compet.objects.filter(judge=judgeInstance))
        return compet.__name__, competData

    if spontOrLong == "spont":
        return {"Spontaneous": ["TODO:  NOT IMPLEMENTED YET!!!"]}
    else:
        return dict(map(_one, ALL_EXCEPT_SPONT))


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

        url = "steamify:{}-add".format(gct)
        return HttpResponseRedirect(reverse(url,
                kwargs={'spontOrLong': self.kwargs['spontOrLong'], 'full_team_id': full_team_id}))
