import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from browse.forms import *

from browse.models import *


@csrf_exempt
def Home_page(request):
    return render(request, 'home_page.html')


@csrf_exempt
def webhook_notification(request):
    try:
        order = json.loads(request.body)
        print(order)

        order_details = OrderDetails.objects.get_or_create(order_id=order.get('order_number'),
                                                           email=order.get('email'),
                                                           phone=order.get('phone'),
                                                           notes=order.get('notes'),
                                                           )

        order_price = OrderPriceDetails.objects.create(order=order_details[0],
                                                       subtotal_price=order.get('subtotal_price'),
                                                       total_price=order.get('total_price'),
                                                       total_tax=order.get('total_tax')
                                                       )

        for each in order.get('line_items'):
            order_item = OrderItemDetails.objects.create(order=order_details[0],
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
        order_details = OrderDetails.objects.all().values()
        context = {'order': list(order_details)}
    except Exception as e:
        context = {'error': e}
        pass
    return render(request, 'home_page.html', context=context)


def update_order(request):
    form = {}
    if request.method == "GET":
        order_id = request.GET.get('id')
        order_details = OrderDetails.objects.get(order_id=order_id)
        form = UpdateForm(instance=order_details)

    if request.method == "POST":
        data = request.POST
        order_details = OrderDetails.objects.get(order_id=data.get('order_id'))
        order_details.email = data.get('email')
        order_details.phone = data.get('phone')
        order_details.save()
        return redirect('home')

    return render(request, 'update.html', context={'form': form})
