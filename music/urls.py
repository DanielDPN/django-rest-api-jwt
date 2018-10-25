from django.urls import path
from .views import ListSongsView, LoginView, RegisterUsersView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register"),
    path('songs/', ListSongsView.as_view(), name="songs-all")
]
