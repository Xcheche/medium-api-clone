from django.shortcuts import render
from .serializers import UserSerializer, CustomRegisterSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()


class CustomUserDetailView(RetrieveUpdateAPIView):
    """A view to retrieve and update the authenticated user's details."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Return the authenticated user."""
        return self.request.user
    
    def get_queryset(self):
        """Return the queryset for the authenticated user."""
        return get_user_model().none()