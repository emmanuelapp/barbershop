from django.conf.urls import include ,url
from . import views
app_name = 'productos'
urlpatterns  = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^productos/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^productos/nuevo/$' , views.ProductCreate.as_view( ), name="product-add"), 
    url(r'^productos/update/(?P<pk>[0-9]+)/$' , views.ProductUpdate.as_view( ), name="product-update"), 
    url(r'^productos/(?P<pk>[0-9]+)/delete/$' , views.ProductDelete.as_view( ), name="product-delete"),
]