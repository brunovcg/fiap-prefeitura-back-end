from django.urls import path
from .views import BuildingsView, NeighborhoodView

urlpatterns = [
    path('buildings/', BuildingsView.as_view()),
    path('buildings/neighborhood/', NeighborhoodView.as_view())
]
