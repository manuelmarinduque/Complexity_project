from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=20)
    poblacion = models.IntegerField()
    estaciones_actuales = models.IntegerField()
    personal_requerido = models.IntegerField()
    costos = models.FloatField()
    muertes = models.IntegerField()
    cualificacion = models.IntegerField()

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.name