from django.urls import path
from .views import listings, search, detail


urlpatterns = [
    path('', listings, name='listings'),
    path('search/', search, name='search'),
    path('<int:id>/', detail, name='detail'),
]