from django.urls import path
from .views import (
    RegistrationView,
    LoginView,
    RefreshView,
    LogoutView,
    UserListView,
    UserDetailView,
    ProfileView,
)

urlpatterns = [
    path("register", RegistrationView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("token/refresh", RefreshView.as_view(), name="token_refresh"),
    path("logout", LogoutView.as_view(), name="logout"),

    path("users", UserListView.as_view(), name="users"),
    path("users/<int:pk>", UserDetailView.as_view(), name="user_detail"),

    path("profile", ProfileView.as_view(), name="profile"),
]