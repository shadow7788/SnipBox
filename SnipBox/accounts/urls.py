from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserRegisterView, LoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("refresh/", TokenRefreshView.as_view())
]