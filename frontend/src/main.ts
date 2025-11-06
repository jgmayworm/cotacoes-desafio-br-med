import Highcharts from 'highcharts'

// Força idioma padrão global (antes de usar HighchartsVue)
Highcharts.setOptions({
  lang: {
    locale: 'en-US' // 👈 idioma seguro e válido
  }
})

import { createApp } from 'vue'
import App from './App.vue'
import HighchartsVue from 'highcharts-vue'
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';

const app = createApp(App)

app.use(HighchartsVue)
app.use(Toast);

app.mount('#app')
