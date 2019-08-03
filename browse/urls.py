from django.conf.urls import url
from browse import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url(r'^$',views.view_order, name="home"),
    url(r'webhook_notify/', views.webhook_notification, name="webhook_notification")
]
urlpatterns += staticfiles_urlpatterns()