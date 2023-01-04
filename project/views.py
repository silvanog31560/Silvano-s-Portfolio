from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MyProject

class MyProjectListView(ListView):
    model = MyProject
    context_object_name = 'myproject_list'

class MyProjectDetailView(DetailView):
    model = MyProject
    context_object_name = 'project'
