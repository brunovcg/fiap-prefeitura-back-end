from django.urls import path
from .views import LoginView, SignupView, PersonasView, AllUsersView, UserView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    path('personas/', PersonasView.as_view()),
    path('users/', AllUsersView.as_view()),
    path('user/<int:user_id>', UserView.as_view())
]
