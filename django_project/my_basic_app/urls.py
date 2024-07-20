from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_basics, name='app_basics'),
]
