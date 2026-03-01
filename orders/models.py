from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

class Order(models.Model):             # Model 4
    STATUS = [('pending','Pending'),('paid','Paid'),('shipped','Shipped'),('cancelled','Cancelled')]
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')       # MANY-TO-ONE
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return f'Order #{self.pk} by {self.user.username}'


class OrderItem(models.Model):         # Model 5 — links Order and Product
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity

