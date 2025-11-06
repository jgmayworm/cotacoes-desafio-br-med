from django.urls import reverse
from rest_framework.test import APITestCase
from datetime import date, timedelta
from unittest.mock import patch


class CotacoesAPITest(APITestCase):

    @patch('cotacoes_api.views.fetch_taxas_cambio')
    def test_per_valido(self, mock_coleta):
        url = reverse('get_taxas')
        inicio = date(2025, 10, 1)
        fim = inicio + timedelta(days=3)
        response = self.client.get(url, {
            'inicio': inicio,
            'fim': fim
        })
        self.assertEqual(response.status_code, 200)
        mock_coleta.assert_called()

    def test_per_maior_cinco_dias(self):
        url = reverse('get_taxas')
        inicio = date(2025, 10, 1)
        fim = inicio + timedelta(days=10)
        response = self.client.get(url, {'inicio': inicio, 'fim': fim})
        self.assertEqual(response.status_code, 400)
