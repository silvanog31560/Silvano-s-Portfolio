from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('email', 'subject', 'sent')
    ordering=('subject', 'sent')
    search_fields=('email',)
    fieldsets=(
        ('Messages',{
            'fields':(
            'email', 'subject', 'message',
            )
        }),
    )
