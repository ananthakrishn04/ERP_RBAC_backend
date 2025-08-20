from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import IsAdmin, IsAdminOrManager

from .serializers import (
    RegistrationSerializer,
    UserSerializer,
    MyTokenObtainPairSerializer
)

from .models import User

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAdmin]

class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RefreshView(TokenRefreshView):
    pass

class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response({"detail" : "Refresh Token in Required"}, status=400)
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail" : "Successfully logged out"})
        except:
            return Response({"detail" : "Invalid Token Provided"}, status=400)

class UserListView(generics.ListAPIView):
    permission_classes = [IsAdminOrManager]
    serializer_class = UserSerializer

    def get_queryset(self):
        u = self.request.user
        if hasattr(u, "isAdmin") and u.isAdmin():
            return User.objects.all().order_by("id")
        return User.objects.filter(role=User.Roles.EMPLOYEE).order_by("id")


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("id")

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user