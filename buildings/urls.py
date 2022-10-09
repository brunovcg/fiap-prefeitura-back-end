from django.urls import path
from .views import BuildingsView, NeighborhoodView, UserBuildingsView

urlpatterns = [
    path('buildings/', BuildingsView.as_view()),
    path ('buildings/<int:user_id>/' , UserBuildingsView.as_view()),
    path('buildings/neighborhood/', NeighborhoodView.as_view())
]
