from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Home_page(request):
    return render(request,'home_page.html')


@csrf_exempt
def webhook_notification(request):
    print(request.method, 111111)
    print(request.POST)
    print(request.body)
    return HttpResponse(status=200)