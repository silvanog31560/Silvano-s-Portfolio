from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
