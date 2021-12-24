from django.urls import path
from .views import listings, search, detail


urlpatterns = [
    path('', listings, name='listings'),
    path('<int:listing_id>', detail, name='detail'),
    path('search/', search, name='search'),
]