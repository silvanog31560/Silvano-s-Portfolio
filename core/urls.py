"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

from accounts import views

admin.site.site_header = "My Portfolio Administration"
admin.site.site_title = "My Portfolio Admin"
admin.site.index_title = "My Portfolio Admin Home"

urlpatterns = [
    path(
        'admin/password_reset/',
        views.CustomPasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('projects/', include('project.urls', namespace='projects')),
    path('education/', include('education.urls', namespace='education')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('go-to-github/', RedirectView.as_view(url='https://github.com/silvanog31560?tab=repositories'),
    name='go-to-github'),
    path('go-to-linkedin/', RedirectView.as_view(url='https://www.linkedin.com/in/silvano-gonzalez-47171b1b0/'),
    name='go-to-linkedin'),
]
