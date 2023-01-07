from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView

from .forms import MyPasswordResetForm

# Have to use SenGrid Api to send emails with free PythonAnywhere account.
class CustomPasswordResetView(PasswordResetView):

    form_class = MyPasswordResetForm
