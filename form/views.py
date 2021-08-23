from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request=request, template_name='form/index.html')

# Create your views here.


def about(request):
    return HttpResponse("<h1> Responded </h1>")
