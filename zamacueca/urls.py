from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from index import views
from . import views 
app_name = 'main'
urlpatterns = [
     url(r'^', include('index.urls'), name='index'), 
     url(r'^admin/', admin.site.urls), 
     url(r'^citas/', include('cita.urls')),
     url(r'^productos/', include('productos.urls')),
     url(r'^register/$', views.UserFormView.as_view() , name='register'), 
     url(r'^login_user/$', views.login_user , name='login_user'),
     url(r'^logout_user/$', views.login_user , name='logout_user'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)