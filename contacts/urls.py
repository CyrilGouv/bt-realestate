from django.urls import path
from .views import enquiry


urlpatterns = [
    path('contact/', enquiry, name='enquiry'),
]