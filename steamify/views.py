
"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
"""

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

from django.forms import modelform_factory
from .forms import PickTeamIdForm


from .models import Choice, Question, EngMiddle



class IndexView(generic.ListView):
    template_name = 'steamify/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'steamify/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'steamify/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'steamify/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('steamify:results', args=(question.id,)))


class EngMiddleCreate(CreateView):
    model = EngMiddle
    form_class = modelform_factory(EngMiddle, fields="__all__")

# Maybe do public-facing list, edit, view, and delete IF I CAN limit it
# ALSO WE WOULD NEED TIME RESTRICTION. might not be worth it.
#  only view/eit your own
# class EngMiddleUpdate(UpdateView):
#     model = EngMiddle
#     fields = engfields
# class EngMiddleDelete(DeleteView):
#     model = EngMiddle
#     success_url = "/"   # if using reverse, must use reverse_lazy here as per docs. example:  # reverse_lazy('EngMiddle-list')
# class EngMidDetailView(generic.DetailView):
#     model = EngMiddle
# class EngMidListView(generic.ListView):
#     model = EngMiddle
#     def get_queryset(self):      
#         # We would change this to only list your own submissions.
#         return Question.objects.all()



class PickTeamIdView(FormView):
    template_name = 'steamify/pickteamname.html'
    form_class = PickTeamIdForm

    def form_valid(self, form):
        # as per https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/
        # This method is called when valid form data has been POSTed. It should return an HttpResponse.
        team_id = form.cleaned_data['team_id']
        return HttpResponseRedirect(reverse("steamify:engmid-add", kwargs={'spontOrLong': self.kwargs['spontOrLong'], 'team_id': team_id}))
