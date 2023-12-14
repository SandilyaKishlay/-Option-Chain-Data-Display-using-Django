from django.urls import path
from .views import display_it


urlpatterns = [
    path('display/', display_it, name='display_it'),
]


