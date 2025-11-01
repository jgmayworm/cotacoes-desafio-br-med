from rest_framework import serializers
from .models import TaxaCambio


class TaxaCambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxaCambio
        fields = ['data', 'moeda_base', 'moeda_tgt', 'taxa']
