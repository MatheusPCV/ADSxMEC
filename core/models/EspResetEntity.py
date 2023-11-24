from django.db import models

class EspReset(models.Model):
    last_notified_at = models.DateTimeField(auto_now_add=True)
    signal_to_send = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.last_notified_at, self.signal_to_send
