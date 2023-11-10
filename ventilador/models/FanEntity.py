from django.db import models

# Create your models here.
class FanModel(models.Model):
    temparature = models.DecimalField(blank=False, null=False, decimal_places=2);
    turn_on = models.BooleanField(False);

