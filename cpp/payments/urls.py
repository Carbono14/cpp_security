from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^cpp/provedor', views.provedor),
    url(r'^cpp/factura', views.factura),
    url(r'^cpp/concepto_de_pago', views.concepto_pago),

]
