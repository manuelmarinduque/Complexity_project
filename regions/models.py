from django.db import models

# Create your models here.
class Region(models.Model):
    region_name = models.CharField(verbose_name= 'region name', max_length=20)
    existing_population = models.IntegerField(verbose_name='existing population')
    current_personal = models.IntegerField(verbose_name='current personal')
    required_personal = models.IntegerField(verbose_name='required personal')
    generated_costs = models.FloatField(verbose_name='generated costs')
    deads = models.IntegerField(verbose_name='deads')
    qualification = models.IntegerField(verbose_name='qualification')

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.name