from django.urls import path

from .utils.faketypes import ModelField

from django.views.generic import TemplateView

from . import views
from .views import GenericCreate, PickTeamIdView, GenericDetail, GenericUpdate, EntryHomeView, AdminStatusView, AdminJudgeListView, TeamBreakdownView
from .models import ALL_EXCEPT_SPONT, Spont, Shared
from .utils.misc import shared_fields_to_exlude_in_user_forms, getUserDisplayedAttrs
from django.forms import modelform_factory, RadioSelect
from django import forms
from django.forms.widgets import Input
from typing import List, Callable, Type, Dict, Set, Tuple, Any, NewType

# idk if this is needed; it was in the tutorial
app_name = 'steamify'

urlpatterns = [
    path('', TemplateView.as_view(template_name='steamify/steamifyhome.html'), name="steamifyhome"),
    path('entry/', EntryHomeView.as_view(), name="entryhome"),
    path('entry/<spontOrLong>/', PickTeamIdView.as_view(), name="pickteamname"),
    path('adminstatus', AdminStatusView.as_view(), name="adminstatus"),
    path('adminjudgelist', AdminJudgeListView.as_view(), name="adminjudgelist"),
    path('teambreakdown', TeamBreakdownView.as_view(), name="teambreakdown"),

    # path('engmid/delete/<int:pk>/', EngMiddleDelete.as_view(), name='engmid-delete'),

    # path('engmid/', EngMidListView.as_view(), name='engmid-list'),
]  # type: List[Callable]


def run_as_view(ViewClass, ModelClass):
    # type: (Type[Any], Type[Shared]) -> Any
    keepers = getUserDisplayedAttrs(ModelClass)
    
    # This took me a little while to figure out, so I posted it on StackOverflow:
    # https://stackoverflow.com/questions/58383617/django-how-to-specify-include-blank-false-in-modelform-factory-using-formf/
    def formfield_callback(f, **kwargs):
        # type: (ModelField, dict) -> forms.Field
        if f.name in keepers:
            kwargs['choices'] = f.get_choices(include_blank=False)
            kwargs['widget'] = RadioSelect
        # regardless of whether I modified it, call .formfield()
        return f.formfield(**kwargs)

    modForm = modelform_factory(ModelClass,
                exclude=shared_fields_to_exlude_in_user_forms,
                formfield_callback=formfield_callback,
                )
    return ViewClass.as_view(model=ModelClass, form_class=modForm)


def createUrls(ModelClass, tla_ish):
    # type: (Type[Shared], str) -> List[Callable]
    """for Spont, I'm hijacking `tla_ish`"""
    
    url_base = 'entry/<spontOrLong>/{}/<full_team_id>'.format(tla_ish)
    pattsToReturn = []  # type: List[Callable]

    url_add = url_base + "/add"
    name_add = "{}-add".format(tla_ish)
    pattsToReturn += [path(
        url_add,
        run_as_view(GenericCreate, ModelClass),
        name=name_add
    )]

    url_edit = url_base + "/edit/<pk>"
    name_edit = "{}-edit".format(tla_ish)
    pattsToReturn += [path(
        url_edit,
        run_as_view(GenericUpdate, ModelClass),
        name=name_edit
    )]

    url_view = url_base + "/view/<pk>"
    name_view = "{}-view".format(tla_ish)
    pattsToReturn += [path(
        url_view,
        GenericDetail.as_view(model=ModelClass),
        name=name_view
    )]

    return pattsToReturn

    # path('engmid/view/<int:pk>/', GenericDetail.as_view(), name='engmid-view'),


# This will create 2*n urls where n=number of competitions (not ideal, but I'm sure django can handle it. I'd be really surprised if it choked on anything less than 100 urls)
for ModelClass in ALL_EXCEPT_SPONT:
    urlpatterns += createUrls(ModelClass, ModelClass.TLA)

urlpatterns += createUrls(Spont, "spont")
    

