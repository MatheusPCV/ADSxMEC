from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class EspInfoEntity(models.Model):
    data = models.DateField(auto_now_add=True)
    tempo_de_estudo = models.FloatField()  # Tempo de estudo em horas
    frequencia = models.IntegerField()     # Frequência de estudo

    def __str__(self):
        return f"Estudo em {self.data}"

@receiver(post_save, sender=EspInfoEntity)
def reset_daily_data(sender, instance, **kwargs):
    today = timezone.now().date()
    if instance.data != today:
        EspInfoEntity.objects.filter(data__lt=today).delete()