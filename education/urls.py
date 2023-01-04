from django.urls import path

from . import views

app_name='education'
urlpatterns = [
    path('', views.MyEducationListView.as_view(), name='education-list'),
    path('technology/', views.TechnologyListView.as_view(), name='technology-list'),
]
