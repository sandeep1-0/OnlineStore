from django.conf.urls import url
from browse import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url(r'^$',views.view_order, name="home"),
    url(r'webhook_notify/', views.webhook_notification, name="webhook_notification"),
    url(r'update_order/$',views.update_order, name="update_order")
]
urlpatterns += staticfiles_urlpatterns()