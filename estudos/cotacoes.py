from typing import Concatenate
import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
dolar = cotacoes['USDBRL']['bid']
print(dolar)
euro = cotacoes['EURBRL']['bid']
print(euro)

testa_site = requests.get('http://www.uol.com.br')
print(testa_site)

if str(testa_site) == '<Response [200]>':
    print('teste foi ok')
else:
    print('teste n ok')