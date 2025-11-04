from django.test import TestCase
from cotacoes_api.models import Cotacao
from datetime import date


class CotacaoModelTest(TestCase):

    def test_create_cotacao(self):
        cotacao = Cotacao.objects.create(data=date(2025, 10, 1),
                                         moeda_tgt='BRL',
                                         taxa=5.0)

        recuperada = Cotacao.objects.get(data=date(2025, 10, 1),
                                         moeda_tgt='BRL')

        self.assertEqual(recuperada.taxa, 5.0)
        self.assertEqual(str(recuperada.moeda_base), 'USD')
        self.assertEqual(str(recuperada.moeda_tgt), 'BRL')
