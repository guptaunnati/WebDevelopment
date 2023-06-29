from django.db import models
from django.utils import timezone

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    iin = models.CharField(max_length=100, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField(default=0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    profit_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
   
    def save(self, *args, **kwargs):
        self.profit = self.selling_price - self.cost
        self.profit_earned = self.profit * self.quantity_sold
        self.revenue = self.selling_price * self.quantity_sold
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=100, default='')
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    orderdttm = models.DateTimeField(default=timezone.now)
    is_received = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    name = models.CharField(max_length=100, default='')
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    transactiondttm = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name