from django.urls import path
from .views import (
    OrderCreateView, MyOrdersView,
    AdminOrderListView, UpdateOrderStatusView,
    DailyProductionListCreateView, TodaysProductionSummaryView
)

urlpatterns = [
    path('create/', OrderCreateView.as_view()),
    path('my-orders/', MyOrdersView.as_view()),

    path('admin/list/', AdminOrderListView.as_view()),
    path('admin/update/<int:pk>/', UpdateOrderStatusView.as_view()),

    path('production/', DailyProductionListCreateView.as_view()),
    path('production/today-summary/', TodaysProductionSummaryView.as_view()),
]