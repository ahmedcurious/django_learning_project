from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.


def app_basics(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'my_basic_app/index.html', {'chais': chais})


def chai_details(request, chai_id: int):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'my_basic_app/chai_detail.html', {'chai': chai})
