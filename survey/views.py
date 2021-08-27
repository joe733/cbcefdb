from django.views.generic import TemplateView, ListView

from .models import Family


class HomeView(TemplateView):
    template_name = "survey/index.html"


class FamilyView(ListView):
    model = Family
    template_name = "survey/families.html"
