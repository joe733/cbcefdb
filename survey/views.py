from django.views.generic import TemplateView, ListView

from .models import Family


class HomeView(TemplateView):
    template_name = "index.html"


class FamilyView(ListView):
    model = Family
    template_name = "families.html"
