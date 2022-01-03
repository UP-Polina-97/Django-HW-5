from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    decription = models.TextField()
    #measurements = models.ManyToManyField(Measurement, related_name='measurements')

#on_delete=models.CASCADE
class Measurement(models.Model):
    id_sensor= models.ForeignKey(Sensor,
                                 on_delete=models.CASCADE,
                                 related_name='measurement'
                                 )
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)