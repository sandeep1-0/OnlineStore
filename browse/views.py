from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Home_page(request):
    return render(request,'home_page.html')


@csrf_exempt
def webhook_notification(request):
    print(request.method, 111111)
    print(request.data, 22222)
    print(request.__dict__)
    return HttpResponse(status=200)