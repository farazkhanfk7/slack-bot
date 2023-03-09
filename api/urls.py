from django.urls import path
from .views import *

urlpatterns = [
    path('city/', CityView.as_view()),
    path('hook/', SlackEventHookView.as_view()),
    path('send/', SlackSendView.as_view()),
]
