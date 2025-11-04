from rest_framework import serializers
from .models import Cotacao


class CotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotacao
        fields = ['data', 'moeda_base', 'moeda_tgt', 'taxa']
