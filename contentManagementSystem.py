# content_management/models.py
from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

# content_management/admin.py
from django.contrib import admin
from .models import Announcement, Language

admin.site.register(Announcement)
admin.site.register(Language)
