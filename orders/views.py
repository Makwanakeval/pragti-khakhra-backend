from rest_framework import generics, permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from django.utils import timezone
from .models import Order, DailyProduction
from .serializers import OrderSerializer, DailyProductionSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

class MyOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created_at')


# ===== ADMIN DASHBOARD VIEWS =====

class AdminOrderListView(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'status': ['exact'],
        'created_at': ['date', 'date__gte', 'date__lte'],
        'delivery_city': ['exact', 'icontains'],
    }

class UpdateOrderStatusView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]


class DailyProductionListCreateView(generics.ListCreateAPIView):
    queryset = DailyProduction.objects.all().order_by('-date')
    serializer_class = DailyProductionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'flavour', 'made_by']

    def perform_create(self, serializer):
        serializer.save(made_by=self.request.user)


class TodaysProductionSummaryView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        today = timezone.now().date()
        data = (
            DailyProduction.objects.filter(date=today)
            .values('flavour__name')
            .annotate(total_kg=Sum('quantity_kg'))
        )
        return Response(data)