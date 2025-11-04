from django.test import TestCase
from unittest.mock import patch
from cotacoes_api.utils import fetch_taxas_cambio
from cotacoes_api.models import Cotacao
from datetime import date


class ColetaCotacoesTest(TestCase):
    @patch('api.utils.requests.get_taxas')
    def test_coleta_dados(self, mock_get):
        # Simulando a VATComply
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'rates': {'BRL': 5.0, 'EUR': 0.9, 'JPY': 150.0}
        }

        fetch_taxas_cambio(date(2025, 10, 1))

        cotacoes = Cotacao.objects.all()
        self.assertEqual(cotacoes.count(), 3)
        self.assertTrue(Cotacao.objects.filter(moeda='BRL').exists())
