from django import forms
from django.shortcuts import render

from .forms import IndividualForm

# Create your views here.


def home(request):
    form = IndividualForm()
    return render(request=request, template_name='survey/index.html', context={'form': form})
