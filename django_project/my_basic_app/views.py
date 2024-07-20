from django.shortcuts import render

# Create your views here.
def app_basics(request):
    return render(request, 'my_basic_app/index.html')