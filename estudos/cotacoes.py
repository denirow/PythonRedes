from typing import Concatenate
import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
dolar = cotacoes['USDBRL']['bid']
print(dolar)
euro = cotacoes['EURBRL']['bid']
print(euro)