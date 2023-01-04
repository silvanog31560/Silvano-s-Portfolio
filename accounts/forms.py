from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.template import loader

# import sendgrid
import os
# from sendgrid.helpers.mail import Mail, Email, To, Content


# Have to use SenGrid Api to send emails with free PythonAnywhere account.
class MyPasswordResetForm(PasswordResetForm):
    pass

    # def send_mail(
    #     self,
    #     subject_template_name,
    #     email_template_name,
    #     context,
    #     from_email,
    #     to_email,
    #     html_email_template_name=None,
    # ):
    #
    #     sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    #     from_email = Email(settings.ADMIN_EMAILS)
    #     to_email = to_email
    #     subject = loader.render_to_string(subject_template_name, context)
    #     # Email subject *must not* contain newlines
    #     subject = "".join(subject.splitlines())
    #     body = loader.render_to_string(email_template_name, context)
    #     content = Content("text/plain", body)
    #     mail = Mail(from_email, to_email, subject, content)
    #     mail_json = mail.get()
    #     sg.client.mail.send.post(request_body=mail_json)
