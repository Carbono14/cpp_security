from django.db import models

class usuarios(models.model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    nombre_usuario = models.CharField(max_length = 50)
    clave = models.CharField(max_length = 50)


class Conceptos_pago(models.Model):
    descripcion = models.CharField(max_length = 50)
    estado = models.BooleanField()

class Proveedores(models.Model):
    nombre = models.CharField(max_length = 50)
    tipo_persona = models.BooleanField()
    cedula_rnc = models.CharField(max_length = 11)
    balance = models.IntegerField()
    estado = models.BooleanField()

class Facturas (models.Model):
    numero_factura = models.CharField(max_length = 50)
    fecha_factura = models.DateField()
    monto = models.DecimalField(max_digits = 11, decimal_places = 2)
    fecha_registro = models.DateField()
    proveedor = models.CharField(max_length = 50)
    estado = models.BooleanField()









