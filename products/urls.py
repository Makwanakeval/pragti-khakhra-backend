from django.urls import path
from .views import FlavourListView

urlpatterns = [
    path('flavours/', FlavourListView.as_view()),
]