from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from .models import Cotacao
from .serializers import CotacaoSerializer
from .utils import fetch_taxas_cambio


def _dias_uteis(inicio, fim):
    """Conta dias úteis há entre duas datas"""
    dias = 0
    atual = inicio
    while atual <= fim:
        if atual.weekday() < 5:
            dias += 1
        atual += timedelta(days=1)
    return dias


@api_view(['GET'])
def get_taxas(request):
    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    moeda = request.GET.get('moeda', 'BRL').upper()

    data_ini = datetime.strptime(inicio, "%Y-%m-%d").date()
    data_fim = datetime.strptime(fim, "%Y-%m-%d").date()

    dias_uteis = _dias_uteis(data_ini, data_fim)
    if dias_uteis > 5:
        return Response({"error": "Máximo de 5 dias úteis"}, status=400)

    fetch_taxas_cambio(moeda, data_ini, data_fim)

    taxas = Cotacao.objects.filter(data__range=[data_ini, data_fim],
                                   moeda_tgt=moeda)
    serializer = CotacaoSerializer(taxas, many=True)
    return Response(serializer.data)
