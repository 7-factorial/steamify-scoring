from django.urls import path

from django.views.generic import TemplateView

from . import views
from .views import EngMiddleCreate, EngMidDetailView, EngMidListView, PickTeamNameView
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
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('entry/', TemplateView.as_view(template_name='steamify/entryhome.html'), name="entryhome"),
    
    path('entry/<spontOrLong>/', PickTeamNameView.as_view(), name="pickteamname"),

    path('engmid/add/', EngMiddleCreate.as_view(), name='engmid-add'),
    # path('engmid/edit/<int:pk>/', EngMiddleUpdate.as_view(), name='engmid-edit'),
    # path('engmid/delete/<int:pk>/', EngMiddleDelete.as_view(), name='engmid-delete'),
    path('engmid/view/<int:pk>/', EngMidDetailView.as_view(), name='engmid-view'),
    path('engmid/', EngMidListView.as_view(), name='engmid-list'),
]
