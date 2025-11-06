<template>
  <div class="p-4">

    <Loading :active="loading" :is-full-page="true" text="Carregando..." />
    <h2>Cotações USD / {{ moeda_cambial }}</h2>

     <form @submit.prevent="loadData">
      <label>Data início: <input type="date" v-model="data_inicio" /></label>
      &nbsp;
      <label>Data fim: <input type="date" v-model="data_fim" /></label>
      &nbsp;
      <select v-model="moeda_cambial">
        <option value="BRL">BRL</option>
        <option value="EUR">EUR</option>
        <option value="JPY">JPY</option>
      </select>
      &nbsp;
      <button type="submit">Buscar</button>
      {{ loading ? "..." : "" }}
    </form>

    <!-- Gráfico -->
     <br><br>
    <Chart v-if="!loading" :options="chartOptions" class="mt-4" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import Highcharts from 'highcharts'
import { Chart } from 'highcharts-vue'
import { useToast } from 'vue-toastification'
import Loading from 'vue3-loading-overlay'
import 'vue3-loading-overlay/dist/vue3-loading-overlay.css'

// // Configurações
// const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api/cotacoes/"
const API_BASE_URL = "http://localhost:8000/api/cotacoes/"
const toast = useToast()
const loading = ref(false)

// --------------
const data_inicio = ref('')
const data_fim = ref('')
const moeda_cambial = ref('BRL')
const erro = ref('')
const chartOptions = ref({
  title: { text: 'Cotações' },
  xAxis: { categories: [] },
  series: [{ name: 'Cotação', data: [] }]
})

async function loadData() {
  erro.value = ''
  loading.value = true

  // Validação de datas no frontend
  if (!data_inicio.value || !data_fim.value) {
    toast.error('Selecione as duas datas antes de buscar.')
    loading.value = false
    return
  }

  const diffDias = (new Date(data_fim.value) - new Date(data_inicio.value)) / (1000 * 60 * 60 * 24)
  if (diffDias > 5) {
    toast.error('O intervalo máximo é de 5 dias.')
    loading.value = false
    return
  }

  try {
    const res = await axios.get(API_BASE_URL, {
      params: {
        inicio: data_inicio.value,
        fim: data_fim.value,
        moeda: moeda_cambial.value
      }
    })

    const dados = res.data

    if (!dados.length) {
      toast.warning('Nenhuma cotação encontrada para o período selecionado.')
      chartOptions.value.series[0].data = []
    }

    // Atualizando o gráfico
    chartOptions.value = {
      chart: { type: 'line' },
      title: { text: `USD/${moeda_cambial.value}` },
      xAxis: { type: 'category', categories: dados.map(r => r.data) },
      yAxis: { title: { text: 'Taxa de câmbio' } },
      series: [{
        name: `USD/${moeda_cambial.value}`,
        data: dados.map(r => parseFloat(r.taxa) || 0)
      }]
    }

  } catch (erro) {
    console.log(erro)
    erro.value = 'Erro ao buscar dados...'
    toast.error(erro.value)
  } finally {
    console.log('cheguei')
    loading.value = false
  }
}
</script>
