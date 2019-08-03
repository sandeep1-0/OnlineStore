from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def Home_page(request):
    return render(request,'home_page.html')


@csrf_exempt
def webhook_notification(request):
    order = json.loads(request.body)
    print(order)
    return HttpResponse(status=200)