from django.urls import path

from django.views.generic import TemplateView

from . import views
from .views import GenericCreate, PickTeamIdView, GenericDetail, GenericUpdate, EntryHomeView
from .models import EngMiddle, VisualArtsMiddle, ALL_COMPETS
from django.forms import modelform_factory
"""
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""
app_name = 'steamify'

urlpatterns = [
    path('', TemplateView.as_view(template_name='steamify/steamifyhome.html'), name="steamifyhome"),
    path('entry/', EntryHomeView.as_view(), name="entryhome"),
    path('entry/<spontOrLong>/', PickTeamIdView.as_view(), name="pickteamname"),

    # path('engmid/delete/<int:pk>/', EngMiddleDelete.as_view(), name='engmid-delete'),

    # path('engmid/', EngMidListView.as_view(), name='engmid-list'),
]

# model_ids = {
#     "M.EN": EngMiddle,

# This will create 2*n urls where n=number of competitions (not ideal, but I'm sure django can handle it. I'd be really surprised if it choked on anything less than 100 urls)
for ModelClass in ALL_COMPETS:
    model_tla = ModelClass.TLA
    url_base = 'entry/<spontOrLong>/{}/<team_id_number>'.format(model_tla)

    url_add = url_base + "/add"
    name_add = "{}-add".format(model_tla)
    urlpatterns += [path(
        url_add,
        GenericCreate.as_view(
            model=ModelClass,
            form_class=modelform_factory(ModelClass, fields="__all__")),
        name=name_add
    )]

    url_edit = url_base + "/edit/<pk>"
    name_edit = "{}-edit".format(model_tla)
    urlpatterns += [path(
        url_edit,
        GenericUpdate.as_view(
            model=ModelClass,
            form_class=modelform_factory(ModelClass, fields="__all__")),
        name=name_edit
    )]

    url_view = url_base + "/view/<pk>"
    name_view = "{}-view".format(model_tla)
    urlpatterns += [path(
        url_view,
        GenericDetail.as_view(model=ModelClass),
        name=name_view
    )]


    # path('engmid/view/<int:pk>/', GenericDetail.as_view(), name='engmid-view'),
