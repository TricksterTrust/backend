from django.db import models


class Currency(models.Model):
    flag = models.CharField(max_length=20)
    code = models.CharField(max_length=20, unique=True)
    value = models.FloatField()
    primary = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)