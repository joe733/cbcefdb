from django.urls import path
from .views import HomeView, FamilyListView, FamilyCreateView, FamilyInfoView, PersonCreateView

app_name = "survey"  # avoids creating template/app_name

urlpatterns = [
    path('', HomeView.as_view(), name="survey_home"),
    path('family/', FamilyListView.as_view(), name="family_list"),
    path('family/add/', FamilyCreateView.as_view(), name="family_add"),
    path('family/<int:pk>/', FamilyInfoView.as_view(), name="family_info"),
    path('person/add/',
         PersonCreateView.as_view(), name="person_add"),
]
