from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^shop/cart/$', views.cart_detail, name='cart_detail'),
    url(r'^shop/cart/add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^shop/cart/remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]
