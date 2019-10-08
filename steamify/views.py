from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.core import serializers

from django.contrib.auth.mixins import LoginRequiredMixin
import json

from django.forms import modelform_factory
from .forms import PickTeamIdForm

from .utils.misc import score_instance_to_dict

from .models import Team



class EntryHomeView(LoginRequiredMixin, TemplateView):
    template_name = "steamify/entryhome.html"


def create_and_update_get_success_url(self):
    viewname = 'steamify:{}-view'.format(self.model.TLA)
    return reverse(viewname, kwargs={
        "spontOrLong": self.kwargs['spontOrLong'],
        'team_id_number': self.kwargs["team_id_number"],
        "pk": self.object.id})


class GenericCreate(LoginRequiredMixin, CreateView):
    template_name="steamify/generic_score_form.html"
    get_success_url = create_and_update_get_success_url

    def form_valid(self, form):
        # as per https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/#models-and-request-user
        form.instance.judge = self.request.user
        return super().form_valid(form)


# Maybe do public-facing list, edit, view, and delete IF I CAN limit it
# ALSO WE WOULD NEED TIME RESTRICTION. might not be worth it.
#  only view/eit your own
class GenericUpdate(LoginRequiredMixin, UpdateView):
    template_name="steamify/generic_score_form.html"
    get_success_url = create_and_update_get_success_url

# class EngMiddleDelete(DeleteView):
#     model = EngMiddle
#     success_url = "/"   # if using reverse, must use reverse_lazy here as per docs. example:  # reverse_lazy('EngMiddle-list')

class GenericDetail(LoginRequiredMixin, generic.DetailView):
    template_name="steamify/genericdetail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['serial_keys_vals'] = score_instance_to_dict(kwargs['object'])
        editname = 'steamify:{}-edit'.format(self.model.TLA)
        context['premade_edit_link'] = reverse(editname, kwargs=self.kwargs)
        return context


# class EngMidListView(generic.ListView):
#     model = EngMiddle
#     def get_queryset(self):
#         # We would change this to only list your own submissions.
#         return Question.objects.all()


class PickTeamIdView(LoginRequiredMixin, FormView):
    template_name = 'steamify/pickteamname.html'
    form_class = PickTeamIdForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        dotted_ids = list(Team.objects.values_list('dotted_id', flat=True).order_by('dotted_id'))   # pylint: disable=no-member
        context['sorted_team_ids'] = json.dumps(dotted_ids)
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
                kwargs={'spontOrLong': self.kwargs['spontOrLong'], 'team_id_number': team_id_number}))
