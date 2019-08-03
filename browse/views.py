import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from browse.models import *


@csrf_exempt
def Home_page(request):
    return render(request, 'home_page.html')


@csrf_exempt
def webhook_notification(request):
    try:
        order = json.loads(request.body)
        print(order)
        order_price = OrderPriceDetails.objects.create(subtotal_price=order.get('subtotal_price'),
                                                       total_price=order.get('total_price'),
                                                       total_tax=order.get('total_tax')
                                                       )
        order_details = OrderDetails.objects.create(order_id=order.get('order_number'),
                                                    email=order.get('email'),
                                                    phone=order.get('phone'),
                                                    notes=order.get('notes'),
                                                    price_details=order_price,
                                                    )

        for each in order.get('line_items'):
            order_item = OrderItemDetails.objects.create(order=order_details,
                                                         name=each.get('name'),
                                                         quantity=each.get('quantity'),
                                                         fulfillment_status=each.get('fulfillment_status')
                                                         )
    except Exception as e:
        print(e, "exception")
        return HttpResponse(status=201)

    return HttpResponse(status=200)


def view_order(request):
    try:
        print("naynta moneee")
        order_details = OrderDetails.objects.all()
        print(order_details, 1111)
    except Exception as e:
        print(e)
        pass
    return HttpResponse(status=200)