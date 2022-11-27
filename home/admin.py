from django.contrib import admin
from home.models import YoutubeLink, Defence
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin


class YoutubeLinks(admin.ModelAdmin):
    list_display = ('youtube_link',)
    list_display_links = ('youtube_link',)
    search_fields = ['youtube_link']

    list_per_page = 25


admin.site.register(YoutubeLink, YoutubeLinks)


class MyDefence(SummernoteModelAdmin):
    list_display = ('name', 'date_created')
    list_display_links = ('name', 'date_created')
    search_fields = ['name', 'date_created']

    list_per_page = 25


admin.site.register(Defence, MyDefence)
