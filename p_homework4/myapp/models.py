from django.db import models

class temperature_db(models.Model):
    myid = models.AutoField(primary_key=True)
    sensor_id = models.IntegerField(null=False, blank=False)
    temperature = models.FloatField(null=False, blank=False)
    humidity =  models.FloatField(null=False, blank=False)
    timestamp = models.DateTimeField(max_length=6, null=False)