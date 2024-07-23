from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.


def app_basics(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'my_basic_app/index.html', {'chais': chais})
