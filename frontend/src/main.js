import Highcharts from 'highcharts';
// Força idioma padrão global (antes de usar HighchartsVue)
Highcharts.setOptions({
    lang: {
        locale: 'en-US' // 👈 idioma seguro e válido
    }
});
import { createApp } from 'vue';
import App from './App.vue';
import HighchartsVue from 'highcharts-vue';
const app = createApp(App);
app.use(HighchartsVue);
app.mount('#app');
