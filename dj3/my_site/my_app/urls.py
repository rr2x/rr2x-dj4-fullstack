from django.urls import path
from . import views

app_name = "my_app"  # used in {% url '...'%}

urlpatterns = [
    path('', views.example_view, name="example_view"),
    path('variable/', views.variable_view, name="variable_view"),
]
