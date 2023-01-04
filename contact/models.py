from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    sent = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
