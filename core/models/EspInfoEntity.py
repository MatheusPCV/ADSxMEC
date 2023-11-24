from django.db import models

class EspInfo(models.Model):
    time = models.FloatField(null=False, blank=False)

    def __str__(self) -> str:
        return self.time;