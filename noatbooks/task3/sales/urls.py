
# sales/urls.py
from django.urls import path
from .views import SalesPredictionView

urlpatterns = [
    path('predict/', SalesPredictionView.as_view(), name='predict-sales'),  # Correct endpoint
]
