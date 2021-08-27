from django.urls import path
from .views import HomeView, FamilyView, FamilyCreateView, FamilyInfoView

app_name = "survey"  # avoids creating template/app_name

urlpatterns = [
    path('', HomeView.as_view(), name="survey_home"),
    path('families/', FamilyView.as_view(), name="family_list"),
    path('families/add/', FamilyCreateView.as_view(), name="family_add"),
    path('families/<int:pk>/', FamilyInfoView.as_view(), name='family_info'),
]
