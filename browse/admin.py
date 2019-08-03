from django.contrib import admin
from browse.models import *


class OrderDetailsAdmin(admin.ModelAdmin):
    pass


class OrderItemDetailsAdmin(admin.ModelAdmin):
    pass


class OrderPriceDetailsAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderDetails, OrderDetailsAdmin)
admin.site.register(OrderItemDetails, OrderItemDetailsAdmin)
admin.site.register(OrderPriceDetails, OrderPriceDetailsAdmin)