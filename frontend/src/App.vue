<template>
  <div class="container">
    <h1>Cotações do Dólar</h1>
    <Chart />
  </div>
</template>

<script setup>
import Chart from './components/Chart.vue'
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background: #f9f9f9;
  padding: 20px;
}
.container {
  max-width: 800px;
  margin: auto;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
</style>
