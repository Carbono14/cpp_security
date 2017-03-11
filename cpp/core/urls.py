from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^core/rol', views.rol),
    url(r'^core/permiso', views.permiso)

]
