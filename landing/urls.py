from django.urls import path

from landing.views import LandingTemplView

urlpatterns = [
    path('simple/', LandingTemplView.as_view(), name='simple'),
]