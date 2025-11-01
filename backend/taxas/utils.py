import requests
from datetime import timedelta
from .models import TaxaCambio

api_url = "https://api.vatcomply.com/rates"  # url base da vatcomply - buscar de config?


def fetch_taxas_cambio(moeda, data_ini, data_fim):
    data_atual = data_ini

    if not moeda:
        moeda = "BRL"

    while data_atual <= data_fim:
        params = {'base': 'USD', 'date': f"{data_atual}"}
        res = requests.get(api_url, params=params, timeout=10).json()

        valor_taxa = res["rates"][moeda]

        TaxaCambio.objects.update_or_create(
                data=data_atual,
                moeda_tgt=moeda,
                defaults={"taxa": valor_taxa}
            )
        data_atual += timedelta(days=1)
