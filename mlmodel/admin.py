from django.contrib import admin
from .models import Tweet


class TweetAdmin(admin.ModelAdmin):
    list_display = ("tweet", "predictions")


admin.site.register(Tweet, TweetAdmin)
