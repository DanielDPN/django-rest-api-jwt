from django.urls import path
from .views import LoginView, RegisterUsersView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register")
]
