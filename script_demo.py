import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

VATCOMPly_BASE = 'https://api.vatcomply.com'  # endpoint base

# List of dates you want to compare
dates = ["2025-10-26", "2025-10-27", "2025-10-28",  "2025-10-29", "2025-10-30"]
cotacoes = []

# Usa endpoint /history?base=USD&date=YYYY-MM-DD&symbols=BRL,EUR,JPY
url = f"{VATCOMPly_BASE}/rates"
for d in dates:
    params = {'base': 'USD', 'date': f"{d}", 'symbols': 'BRL,EUR,JPY'}
    resp = requests.get(url, params=params, timeout=10)
    time.sleep(2)
    resp.raise_for_status()
    dados = resp.json()
    row = {
        "data": d,
        "USD/BRL": dados["rates"]["BRL"],
        "USD/EUR": dados["rates"]["EUR"],
        "USD/JPY": dados["rates"]["JPY"]
    }
    cotacoes.append(row)


df = pd.DataFrame(cotacoes)

print(df)

plt.figure(figsize=(10, 6))
plt.plot(df["data"], df["USD/BRL"], label="USD/BRL")
plt.plot(df["data"], df["USD/EUR"], label="USD/EUR")
plt.plot(df["data"], df["USD/JPY"], label="USD/JPY")

plt.yscale("log")
plt.title("Histórico de Cotações do Dólar (USD)")
plt.xlabel("Data")
plt.ylabel("Valor")
plt.legend()
plt.grid(True, which="both", linestyle="--")
plt.show()
os.system("pause")
