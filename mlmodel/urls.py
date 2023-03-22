from django.urls import path
from .views import predict_tweet

urlpatterns = [
    path('predict/', predict_tweet),
]