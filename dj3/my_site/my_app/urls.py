from django.urls import path
from . import views

urlpatterns = [
    path('', views.example_view, name="example_view")
]
