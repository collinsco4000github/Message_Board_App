from django.urls import path
from .views import HomePageView

urlPatterns = [
    path('', HomePageView.as_view(), name='home'),
]