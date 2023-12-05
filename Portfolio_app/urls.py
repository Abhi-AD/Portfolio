from django.urls import path
from Portfolio_app import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
