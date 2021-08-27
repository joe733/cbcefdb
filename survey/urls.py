from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path('', views.HomeView.as_view(), name="survey-home"),
    path('families/', views.FamilyView.as_view(), name="list_family"),
    path('families/add', views.FamilyCreateView.as_view(), name="add_family"),

]
