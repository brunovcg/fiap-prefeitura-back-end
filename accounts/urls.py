from django.urls import path
from .views import LoginView, SignupView, PersonasView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    path('personas/', PersonasView.as_view())
]
