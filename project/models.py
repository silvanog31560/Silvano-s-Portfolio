from django.db import models
from django.urls import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class MyProject(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, blank=True, null=True)
    link = models.CharField(max_length=250, unique=True)
    link_url = models.URLField(max_length=250, blank=True, null=True)
    github = models.CharField(max_length=250, blank=True, null=True)
    github_url = models.URLField(max_length=250, blank=True, null=True)
    description = models.TextField()
    technology = models.TextField()
    image = models.ImageField()
    image_thumbnail = ImageSpecField(
                                source='image',
                                processors=[ResizeToFill(300,146)],
                                format='JPEG',
                                options={'quality':60})
    image_regular = ImageSpecField(source='image',
                                   processors=[
                                    ResizeToFill(800, 389),
                                    ],
                                   format='JPEG',
                                   options={'quality': 60})
    image_medium = ImageSpecField(source='image',
                                      processors=[
                                      ResizeToFill(600 , 292),
                                      ],
                                      format='JPEG',
                                      options={'quality': 60})

    class Meta:
        ordering=['created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:project-detail', kwargs={'slug': self.slug})
