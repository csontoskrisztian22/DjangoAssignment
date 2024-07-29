from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=50)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    REC = 'RECEIVED'
    PRE = 'PREPARING'
    REA = 'READY'
    DEL = 'DELIVERED'

    STATUS_CHOICES = {
        REC: 'Received',
        PRE: 'Preparing',
        REA: 'Ready',
        DEL: 'Delivered',
    }

    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=REC)
    items = models.ManyToManyField(Item, through='OrderItem')

class OrderItem(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    special_instructions = models.TextField(blank=True, null=True)
