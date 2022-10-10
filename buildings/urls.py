from django.urls import path
from .views import BuildingsView, NeighborhoodView,OneBuildingsView

urlpatterns = [
    path('buildings/', BuildingsView.as_view()),
    path ('buildings/matricula/<int:matricula>/' , OneBuildingsView.as_view()),
    path('neighborhoods/', NeighborhoodView.as_view())
]
