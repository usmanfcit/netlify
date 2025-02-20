from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User

from .permissions import IsStaff
from .serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
    RegisterSerializer,
)


class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserListingAPIView(generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsStaff,)
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsStaff,)
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsStaff,)
    serializer_class = UserSerializer


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsStaff,)
    serializer_class = UserSerializer


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
