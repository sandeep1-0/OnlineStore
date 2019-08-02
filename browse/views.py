from django.http import HttpResponse
from django.shortcuts import render


def Home_page(request):
    return render(request,'home_page.html')


def webhook_notification(request):
    print(request.GET,111111)
    return HttpResponse({"test": "test"})