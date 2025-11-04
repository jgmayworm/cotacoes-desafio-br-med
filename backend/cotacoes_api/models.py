from django.db import models


class Cotacao(models.Model):
    data = models.DateField()
    moeda_base = models.CharField(max_length=3, default='USD')
    moeda_tgt = models.CharField(max_length=3)
    taxa = models.FloatField()

    class Meta:
        unique_together = ('data', 'moeda_tgt')
        ordering = ['data']
