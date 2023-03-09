from django.urls import path
from .views import CityView

urlpatterns = [
    path('city', CityView.as_view()),
    path('hook', SlackEventHookView.as_view()),
]
