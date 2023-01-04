from django.shortcuts import render
from django.views.generic import ListView

from .models import MyEducation, Technology, Goal

class MyEducationListView(ListView):
    template_name = 'education/myeducation_list.html'
    context_object_name = 'education'

    def get_queryset(self):
        queryset = {
            'list': MyEducation.objects.all(),
            'goal': Goal.objects.all(),
        }
        return queryset

class TechnologyListView(ListView):
    model = Technology
    context_object_name = 'technology_list'
