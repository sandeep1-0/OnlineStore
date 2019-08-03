from django.db import models


class OrderPriceDetails(models.Model):
    subtotal_price = models.IntegerField()
    total_price = models.IntegerField()
    total_tax = models.IntegerField()


class OrderDetails(models.Model):
    order_id = models.IntegerField(primary_key=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    price_details = models.ForeignKey(OrderPriceDetails, on_delete=models.CASCADE)


class OrderItemDetails(models.Model):
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    fulfillment_status = models.CharField(max_length=100, null=True, blank=True)
