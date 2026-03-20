from django import path
from .views import HomePageView

urlPatterns = [
    path('', HomePageView.as_view(), name='home'),
]