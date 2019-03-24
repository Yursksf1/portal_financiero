from django.db import models

# Create your models here.
class Inversion(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField("Motivo de Inversion", max_length=400, default="")
    interes = models.FloatField("Tasa de intres",null=True, blank=True, default=None)
    monto = models.FloatField("Monto",null=True, blank=True, default=None)
    creacion = models.DateField('Fecha agregada', auto_now_add=True)

    