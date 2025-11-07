# Desafio BR_MED
Projeto full-stack em Django + Vue.js que consulta as cotações do dólar (USD) frente ao real (BRL), euro (EUR) e iene (JPY) via API do Vatcomply, permite ao usuário selecionar um intervalo de até 5 dias úteis e quais moedas exibe o resultado em um gráfico Highcharts.
Repositorio foi pensado apra deploy(no onrenderespecificamente) mas pode ser executado, em RUINWINDOWS, com o o script start.bat.

OBS: Desenvolvimento não foi considerado em Linux.

## Funcionalidades extras

- Seleção de período de até 5 dias úteis
- Bloqueio de datas futuras
- Filtro de fins de semana
- Gráfico com Highcharts
- Spinner e mensagens toast para feedback

## Tecnologias utilizadas

### Backend
- Python 3.9+
- Django 4.x
- Django REST Framework
- Banco de dados SQLite
- Módulo interno `fetch_taxas_cambio` para coleta de dados da API VatComply
- Django CORS Headers

### Frontend
- Vue 3 + Vite
- Axios
- Highcharts + highcharts-vue
- Vue Toastification

---

## Configuração local

### Crie e ative o ambiente virtual
- python -m venv venv
- source venv/bin/activate      # Linux/Mac
- venv\Scripts\activate         # Windows

### Backend (Django)
- cd backend
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- http://localhost:8000

### Configuração do Frontend
- cd frontend
- npm install
- npm run dev
- http://localhost:5173


# Deploy no Render
- https://cotacoes-desafio-br-med-front.onrender.com/
  
#
