from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello World, This is our homepage")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello, this is our about page")


def contact(request):
    return HttpResponse("Hello, this is our contact page")
