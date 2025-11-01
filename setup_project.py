import os, textwrap

BASE = "cotacoes_usd_exemplo"

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(textwrap.dedent(content).lstrip())

def main():
    print("📦 Criando estrutura do projeto...")

    # --- Estrutura de diretórios
    os.makedirs(f"{BASE}/backend/exchange/migrations", exist_ok=True)
    os.makedirs(f"{BASE}/frontend/src/components", exist_ok=True)

    # --- Backend: manage.py
    write_file(f"{BASE}/backend/manage.py", """
        #!/usr/bin/env python
        import os, sys
        def main():
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
            from django.core.management import execute_from_command_line
            execute_from_command_line(sys.argv)
        if __name__ == '__main__':
            main()
    """)

    # --- Backend: settings.py
    write_file(f"{BASE}/backend/backend/settings.py", """
        import os
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        SECRET_KEY = 'django-insecure-key'
        DEBUG = True
        ALLOWED_HOSTS = ['*']

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'rest_framework',
            'exchange',
        ]

        MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

        ROOT_URLCONF = 'backend.urls'

        TEMPLATES = [{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        }]

        WSGI_APPLICATION = 'backend.wsgi.application'

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

        LANGUAGE_CODE = 'pt-br'
        TIME_ZONE = 'America/Sao_Paulo'
        USE_I18N = True
        USE_TZ = True

        STATIC_URL = '/static/'
    """)

    # --- Backend: urls.py
    write_file(f"{BASE}/backend/backend/urls.py", """
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('api/', include('exchange.urls')),
        ]
    """)

    # --- Exchange app
    write_file(f"{BASE}/backend/exchange/models.py", """
        from django.db import models

        class ExchangeRate(models.Model):
            date = models.DateField()
            currency = models.CharField(max_length=3)
            rate = models.DecimalField(max_digits=10, decimal_places=4)

            class Meta:
                unique_together = ('date', 'currency')
    """)

    write_file(f"{BASE}/backend/exchange/views.py", """
        import requests
        from datetime import datetime, timedelta
        from django.http import JsonResponse
        from .models import ExchangeRate

        API_URL = "https://api.vatcomply.com/rates"

        def fetch_from_api(date):
            resp = requests.get(f"{API_URL}?base=USD&date={date}")
            return resp.json().get("rates", {})

        def get_rates(request):
            start = request.GET.get("start")
            end = request.GET.get("end")
            currencies = request.GET.get("currencies", "").split(",")

            if not start or not end:
                return JsonResponse({"error": "Parâmetros ausentes."}, status=400)

            start_date = datetime.strptime(start, "%Y-%m-%d").date()
            end_date = datetime.strptime(end, "%Y-%m-%d").date()

            if (end_date - start_date).days > 7:
                return JsonResponse({"error": "Máximo de 5 dias úteis."}, status=400)

            data = {}
            current = start_date
            while current <= end_date:
                rates = fetch_from_api(current)
                for curr in currencies:
                    if curr not in ['BRL', 'EUR', 'JPY']:
                        continue
                    rate_obj, created = ExchangeRate.objects.get_or_create(
                        date=current, currency=curr,
                        defaults={"rate": rates.get(curr)}
                    )
                    data.setdefault(curr, []).append({
                        "date": str(current),
                        "rate": float(rate_obj.rate)
                    })
                current += timedelta(days=1)
            return JsonResponse(data)
    """)

    write_file(f"{BASE}/backend/exchange/urls.py", """
        from django.urls import path
        from . import views
        urlpatterns = [path('rates/', views.get_rates, name='get_rates')]
    """)

    # --- Frontend: package.json
    write_file(f"{BASE}/frontend/package.json", """
        {
          "name": "cotacoes_usd_exemplo",
          "version": "1.0.0",
          "scripts": {
            "dev": "vite",
            "build": "vite build",
            "preview": "vite preview"
          },
          "dependencies": {
            "axios": "^1.7.2",
            "highcharts": "^11.4.0",
            "vue": "^3.4.0"
          },
          "devDependencies": {
            "@vitejs/plugin-vue": "^5.0.0",
            "vite": "^5.0.0"
          }
        }
    """)

    # --- vite.config.js
    write_file(f"{BASE}/frontend/vite.config.js", """
        import { defineConfig } from 'vite'
        import vue from '@vitejs/plugin-vue'

        export default defineConfig({
          plugins: [vue()],
          server: {
            proxy: {
              '/api': 'http://127.0.0.1:8000'
            }
          }
        })
    """)

    # --- Vue src files
    write_file(f"{BASE}/frontend/src/main.js", """
        import { createApp } from 'vue'
        import App from './App.vue'
        createApp(App).mount('#app')
    """)

    write_file(f"{BASE}/frontend/src/App.vue", """
        <template>
          <div>
            <h1>Cotações USD</h1>
            <ChartView />
          </div>
        </template>

        <script setup>
        import ChartView from './components/ChartView.vue'
        </script>
    """)

    write_file(f"{BASE}/frontend/src/components/ChartView.vue", """
        <template>
          <div>
            <div>
              <label>Início: <input type="date" v-model="startDate" /></label>
              <label>Fim: <input type="date" v-model="endDate" /></label>
            </div>
            <div>
              <label><input type="checkbox" value="BRL" v-model="selected" /> BRL</label>
              <label><input type="checkbox" value="EUR" v-model="selected" /> EUR</label>
              <label><input type="checkbox" value="JPY" v-model="selected" /> JPY</label>
            </div>
            <button @click="fetchData">Buscar</button>
            <div id="chart" style="margin-top:20px;"></div>
          </div>
        </template>

        <script setup>
        import axios from 'axios'
        import Highcharts from 'highcharts'
        import { ref } from 'vue'

        const startDate = ref('')
        const endDate = ref('')
        const selected = ref(['BRL'])

        async function fetchData() {
          if (!startDate.value || !endDate.value) return alert('Selecione datas.')
          const res = await axios.get('/api/rates/', {
            params: {
              start: startDate.value,
              end: endDate.value,
              currencies: selected.value.join(',')
            }
          })
          drawChart(res.data)
        }

        function drawChart(data) {
          const series = Object.keys(data).map(c => ({
            name: c,
            data: data[c].map(r => [r.date, parseFloat(r.rate)])
          }))
          Highcharts.chart('chart', {
            title: { text: 'Cotações USD vs Outras Moedas' },
            xAxis: { type: 'category' },
            yAxis: { title: { text: 'Taxa de câmbio' } },
            series
          })
        }
        </script>
    """)

    # --- Scripts de execução
    write_file(f"{BASE}/run_backend.bat", """
        @echo off
        cd backend
        python -m venv venv
        call venv\\Scripts\\activate
        pip install django djangorestframework requests
        python manage.py migrate
        python manage.py runserver
    """)

    write_file(f"{BASE}/run_frontend.bat", """
        @echo off
        cd frontend
        npm install
        npm run dev
    """)

    # --- README
    write_file(f"{BASE}/README.md", """
        # 💵 Projeto cotacoes_usd_exemplo

        Sistema Django + Vue.js para exibir cotações do Dólar (USD) frente a BRL, EUR e JPY.

        ## 🔧 Como rodar no Windows

        1. Execute:
           ```
           python setup_project.py
           ```
        2. Depois entre na pasta criada:
           ```
           cd cotacoes_usd_exemplo
           ```
        3. Inicie o backend:
           ```
           run_backend.bat
           ```
        4. Em outro terminal, inicie o frontend:
           ```
           run_frontend.bat
           ```
        5. Abra no navegador: **http://localhost:5173**
    """)

    print("✅ Projeto 'cotacoes_usd_exemplo' criado com sucesso!")
    print("➡️ Agora basta rodar os scripts 'run_backend.bat' e 'run_frontend.bat'.")

if __name__ == "__main__":
    main()
