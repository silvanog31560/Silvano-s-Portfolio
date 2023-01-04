from django.contrib import admin
from .models import MyEducation, Technology, Goal

admin.site.register(Technology)
admin.site.register(Goal)

@admin.register(MyEducation)
class MyEducationAdmin(admin.ModelAdmin):
    list_display = ['course', 'technology']
    ordering = ('created',)
