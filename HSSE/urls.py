from django.contrib import admin
from django.urls import path
from HSSE import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    url(r'^export-exl/$', views.export, name='export'),
    url(r'^export-csv/$', views.export, name='export'),
    url(r'^form/$', views.Form),
    url(r'^upload/$', views.Upload),
]
