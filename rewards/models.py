from django.conf import settings
from django.db import models


class Reward(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    point_value = models.DecimalField(max_digits=9, decimal_places=2, default=1.00)

    def __str__(self) -> str:
        return self.name


class UserPoints(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points_granted = models.DecimalField(max_digits=9, decimal_places=2, default=10.00)
    points_spent = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
