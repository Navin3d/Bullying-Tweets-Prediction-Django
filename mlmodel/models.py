from django.db import models


class Tweet(models.Model):
    tweet = models.TextField()
    predictions = models.TextField()
