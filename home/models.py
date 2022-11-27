from django.db import models
import django_summernote
# Create your models here.


class YoutubeLink(models.Model):
    youtube_link = models.URLField(blank=True)

    def __str__(self):
        return f'{self.youtube_link}'


class Defence(models.Model):
    name = models.CharField(max_length=200)
    rich_accusation = models.TextField(blank=True)
    rich_defence = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'