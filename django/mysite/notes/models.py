from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=255)
    author = models.CharField(max_length=25, default='anonymous')
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def get_absolute_url(self):
        return reverse('notes:index')
