from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Technology(models.Model):
    title = models.CharField(max_length=75)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    percent = models.IntegerField(blank=True, null=True)
    image = models.ImageField()
    image_medium = ImageSpecField(source='image',
                                      processors=[
                                      ResizeToFill(300 , 300),
                                      ],
                                      format='JPEG',
                                      options={'quality': 60})

    image_small = ImageSpecField(source='image',
                                      processors=[
                                      ResizeToFill(200 , 200),
                                      ],
                                      format='JPEG',
                                      options={'quality': 60})

    class Meta:
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.percent = self.rating * 10
        super().save(*args, **kwargs)

class MyEducation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    technology = models.ForeignKey(
        'Technology', on_delete=models.SET_NULL,
        blank=True, null=True, related_name='+',
        )
    course = models.CharField(max_length=75, unique=True)
    active = models.BooleanField()
    completed = models.BooleanField()
    certificate = models.BooleanField(verbose_name = 'Certificate Available')
    cert_image = models.ImageField(blank=True)
    try:
        image_medium = ImageSpecField(source='cert_image',
                                          processors=[
                                          ResizeToFill(600 , 466),
                                          ],
                                          format='JPEG',
                                          options={'quality': 60})

    except:
        pass

    class Meta:
        ordering=['created']
        verbose_name_plural = 'My education'

    def __str__(self):
        return self.course

class Goal(models.Model):
    subject = models.CharField(max_length=75)
    details = models.TextField()

    def __str__(self):
        return self.subject
