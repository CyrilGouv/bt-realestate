from django.urls import path
from .views import listings


urlpatterns = [
    path('', listings, name='listings'),
]