from rest_framework import generics, permissions
from .models import Flavour
from .serializers import FlavourSerializer

class FlavourListView(generics.ListAPIView):
    queryset = Flavour.objects.filter(is_active=True)
    serializer_class = FlavourSerializer
    permission_classes = [permissions.AllowAny]   # explicitly public

    def get_serializer_context(self):
        return {'request': self.request}