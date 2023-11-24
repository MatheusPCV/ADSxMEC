from django.db import models

class EspInfo(models.Model):
    time = models.FloatField(null=False, blank=False)

class EspReset(models.Model):
    last_notified_at = models.DateTimeField(auto_now_add=True)
    signal_to_send = models.BooleanField(default=False)

