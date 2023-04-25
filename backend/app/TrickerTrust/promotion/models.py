from django.db import models


class Promotion(models.Model):
    primary = models.BooleanField(default=False)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=500, null=True)
    end_time = models.DateTimeField(null=True)
