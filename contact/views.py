from django.views.generic import FormView
from django.conf import settings
from django.views.generic import RedirectView

from .forms import ContactForm
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content



class ContactFormView(FormView):
    form_class = ContactForm
    success_url = '?submitted=True'
    template_name = 'contact/contact.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if 'submitted' in request.GET:
            context['submitted'] = request.GET['submitted']
        return self.render_to_response(context)

    def form_valid(self,form):
        form.save()
        cd = form.cleaned_data
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email(settings.ADMIN_EMAILS)
        to_email = To(settings.CONTACT_EMAIL)
        subject = f"From: {cd['email']}; Subject: {cd['subject']}"
        content = Content("text/plain", cd['message'])
        mail = Mail(from_email, to_email, subject, content)
        mail_json = mail.get()
        sg.client.mail.send.post(request_body=mail_json)
        return super().form_valid(form)
