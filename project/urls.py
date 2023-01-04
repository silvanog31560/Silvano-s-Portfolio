from django.urls import path

from . import views

app_name='projects'
urlpatterns = [
    path('', views.MyProjectListView.as_view(), name='project-list'),
    path('<str:slug>/', views.MyProjectDetailView.as_view(), name='project-detail'),
]
