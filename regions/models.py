from django.db import models

# Create your models here.
class Region(models.Model):
    region_name = models.CharField(name= 'region name', max_length=20)
    existing_population = models.IntegerField(name='existing population')
    current_personal = models.IntegerField(name='current personal')
    required_personal = models.IntegerField(name='required personal')
    generated_costs = models.FloatField(name='generated costs')
    deads = models.IntegerField(name='deads')
    qualification = models.IntegerField(name='qualification')

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.name