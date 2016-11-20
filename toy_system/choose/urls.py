from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'submit/$', views.submit, name='submit'),
    url(r'detail/$', views.detail, name='detail'),
    url(r'review/$', views.review, name='review'),
    url(r'^(?P<cust_id>[0-9]+)/result/$', views.result, name='result'),
]