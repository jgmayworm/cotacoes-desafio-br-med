<template>
  <div>
    <h2>Cotações USD / {{ moeda_cambial }}</h2>

    <form @submit.prevent="loadData">
      <label>Data início: <input type="date" v-model="data_inicio" /></label>
      <label>Data fim: <input type="date" v-model="data_fim" /></label>
      <select v-model="moeda_cambial">
        <option value="BRL">BRL</option>
        <option value="EUR">EUR</option>
        <option value="JPY">JPY</option>
      </select>
      <button type="submit">Buscar</button>
    </form>

    <Chart :options="chartOptions" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import Highcharts from 'highcharts'
import { Chart } from 'highcharts-vue'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api/cotacoes/";
const data_inicio = ref('')
const data_fim= ref('')
const moeda_cambial = ref('BRL')
const chartOptions = ref({
  title: { text: 'Cotações' },
  xAxis: { categories: [] },
  series: [{ name: 'Cotação', data: [] }]
})

async function loadData() {
  const res = await axios.get(API_BASE_URL, {
    params: { inicio: data_inicio.value, fim: data_fim.value, moeda: moeda_cambial.value }
  })

  const dados = res.data

  console.log('Datas:', dados.map(r => r.data))
  console.log('Valores:', dados.map(r => parseFloat(r.taxa)))

  chartOptions.value = {
    chart: { type: 'line' },
    title: { text: `USD/${moeda_cambial.value}` },
    xAxis: {
      type: 'category',
      categories: dados.map(r => r.data)
    },
    yAxis: { title: { text: 'Taxa de câmbio' } },
    series: [{
      name: `USD/${moeda_cambial.value}`,
      data: dados.map(r => parseFloat(r.taxa) || 0)
    }]
  }
}
</script>
