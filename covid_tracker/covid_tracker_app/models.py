from django.db import models


class CovidObservation(models.Model):
    observation_date = models.DateField(auto_now_add=False)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    confirmed = models.IntegerField(default=0, null=True)
    deaths = models.IntegerField(default=0, null=True)
    recovered = models.IntegerField(default=0, null=True)
