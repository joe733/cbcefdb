from .models import Family
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView, DetailView


class HomeView(TemplateView):
    template_name = "index.html"


class FamilyView(ListView):
    model = Family
    template_name = "list_family.html"


class FamilyCreateView(CreateView):
    model = Family
    template_name = "add_family.html"
    fields = ["fam_name", "nofm", ]

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Thank you! Family data has been added."
        )

        return super().form_valid(form)


class FamilyInfoView(DetailView):
    model = Family
    template_name = "family_info.html"
