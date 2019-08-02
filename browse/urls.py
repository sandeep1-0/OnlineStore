from django.conf.urls import url
from browse import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url(r'^$',views.Home_page),
    url(r'webhook_notify/', views.webhook_notification, name="webhook_notification")
]
urlpatterns += staticfiles_urlpatterns()