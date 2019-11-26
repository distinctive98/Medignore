from __future__ import unicode_literals

from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo_file = models.FileField(upload_to='medignore/')