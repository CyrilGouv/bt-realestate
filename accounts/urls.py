from django.urls import path
from .views import login, register, dashboard


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]