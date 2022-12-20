from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    description = models.CharField(max_length=200, verbose_name='description')


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(decimal_places=1, max_digits=3, verbose_name='temperature')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='created_date')


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
