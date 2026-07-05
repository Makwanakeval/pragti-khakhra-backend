from rest_framework import generics, permissions
from .serializers import SignupSerializer, ProfileSerializer
from .models import CustomUser

class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]

class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user