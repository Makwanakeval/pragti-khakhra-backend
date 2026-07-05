from django.db import models
from accounts.models import CustomUser
from products.models import Flavour

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=15)
    delivery_city = models.CharField(max_length=50)
    delivery_address = models.TextField()
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_charge = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    is_free_delivery = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.delivery_city.strip().lower() == 'viramgam':
            self.is_free_delivery = True
            self.delivery_charge = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    quantity_kg = models.DecimalField(max_digits=5, decimal_places=2)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)


class DailyProduction(models.Model):
    made_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    quantity_kg = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.made_by} - {self.flavour} - {self.quantity_kg}kg on {self.date}"