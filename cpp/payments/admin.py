from django.contrib import admin
from payments import models
# Register your models here.
admin.site.register(models.Conceptos_Pago)
admin.site.register(models.Proveedores)
admin.site.register(models.Facturas)
admin.site.register(models.CuentaContable)
admin.site.register(models.AsientoContable)
admin.site.register(models.Divisa)
admin.site.register(models.TazaCambio)


