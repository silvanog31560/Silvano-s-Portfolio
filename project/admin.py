from django.contrib import admin
from .models import MyProject

@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    list_display = ['title',]
    ordering = ('created',)
    prepopulated_fields = {"slug": ("title",)}
