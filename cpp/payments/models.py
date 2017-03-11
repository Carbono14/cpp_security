from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# class User(AbstractUser):
#     birth_date = models.DateField(blank=True, null=True)
#     def __str__(self):
#         return self.username


class AuditModel(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now = True, null=True, blank=True )

    class Meta:
        abstract = True

class Conceptos_Pago(AuditModel):
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField()


class Proveedores(AuditModel):
    nombre = models.CharField(max_length=50)
    tipo_persona = models.BooleanField()
    cedula_rnc = models.CharField(max_length=11)
    balance = models.IntegerField()
    estado = models.BooleanField()


class Divisa (AuditModel):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

class Facturas (AuditModel):
    numero_factura = models.CharField(max_length=50)
    fecha_factura = models.DateField()
    monto = models.DecimalField(max_digits=30, decimal_places=2)
    fecha_registro = models.DateField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    estado = models.BooleanField()
    divisa = models.ForeignKey(Divisa, null=True)

class CuentaContable(AuditModel):
    nombre = models.CharField(max_length=100)


class AsientoContable(AuditModel):
    descripcion = models.CharField(max_length=150)
    cuenta_contable = models.ForeignKey(CuentaContable, on_delete=models.CASCADE)
    tipo = models.IntegerField(choices=[(0, 'DB'),(1, 'CR')])
    fecha_asiento = models.DateField()
    monto_asiento = models.FloatField()

class TazaCambio(AuditModel):
    divisa = models.ForeignKey(Divisa, null=True)
    fecha = models.DateField
    taza = models.FloatField()


