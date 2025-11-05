/// <reference types="C:/Projects/cotacoes/frontend/node_modules/.vue-global-types/vue_3.5_0.d.ts" />
import { ref } from 'vue';
import axios from 'axios';
import Highcharts from 'highcharts';
import { Chart } from 'highcharts-vue';
const data_inicio = ref('');
const data_fim = ref('');
const moeda_cambial = ref('BRL');
const chartOptions = ref({
    title: { text: 'Cotações' },
    xAxis: { categories: [] },
    series: [{ name: 'Cotação', data: [] }]
});
async function loadData() {
    const res = await axios.get(`http://localhost:8000/api/cotacoes/`, {
        params: { inicio: data_inicio.value, fim: data_fim.value, moeda: moeda_cambial.value }
    });
    const dados = res.data;
    console.log('Datas:', dados.map(r => r.data));
    console.log('Valores:', dados.map(r => parseFloat(r.taxa)));
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
    };
}
debugger; /* PartiallyEnd: #3632/scriptSetup.vue */
const __VLS_ctx = {
    ...{},
    ...{},
};
let __VLS_components;
let __VLS_directives;
__VLS_asFunctionalElement(__VLS_intrinsics.div, __VLS_intrinsics.div)({});
__VLS_asFunctionalElement(__VLS_intrinsics.h2, __VLS_intrinsics.h2)({});
(__VLS_ctx.moeda_cambial);
// @ts-ignore
[moeda_cambial,];
__VLS_asFunctionalElement(__VLS_intrinsics.form, __VLS_intrinsics.form)({
    ...{ onSubmit: (__VLS_ctx.loadData) },
});
// @ts-ignore
[loadData,];
__VLS_asFunctionalElement(__VLS_intrinsics.label, __VLS_intrinsics.label)({});
__VLS_asFunctionalElement(__VLS_intrinsics.input)({
    type: "date",
});
(__VLS_ctx.data_inicio);
// @ts-ignore
[data_inicio,];
__VLS_asFunctionalElement(__VLS_intrinsics.label, __VLS_intrinsics.label)({});
__VLS_asFunctionalElement(__VLS_intrinsics.input)({
    type: "date",
});
(__VLS_ctx.data_fim);
// @ts-ignore
[data_fim,];
__VLS_asFunctionalElement(__VLS_intrinsics.select, __VLS_intrinsics.select)({
    value: (__VLS_ctx.moeda_cambial),
});
// @ts-ignore
[moeda_cambial,];
__VLS_asFunctionalElement(__VLS_intrinsics.option, __VLS_intrinsics.option)({
    value: "BRL",
});
__VLS_asFunctionalElement(__VLS_intrinsics.option, __VLS_intrinsics.option)({
    value: "EUR",
});
__VLS_asFunctionalElement(__VLS_intrinsics.option, __VLS_intrinsics.option)({
    value: "JPY",
});
__VLS_asFunctionalElement(__VLS_intrinsics.button, __VLS_intrinsics.button)({
    type: "submit",
});
const __VLS_0 = {}.Chart;
/** @type {[typeof __VLS_components.Chart, ]} */ ;
// @ts-ignore
Chart;
// @ts-ignore
const __VLS_1 = __VLS_asFunctionalComponent(__VLS_0, new __VLS_0({
    options: (__VLS_ctx.chartOptions),
}));
const __VLS_2 = __VLS_1({
    options: (__VLS_ctx.chartOptions),
}, ...__VLS_functionalComponentArgsRest(__VLS_1));
// @ts-ignore
[chartOptions,];
const __VLS_export = (await import('vue')).defineComponent({});
export default {};
