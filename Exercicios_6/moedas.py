'''4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI, mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.  '''

import requests

moeda = input("Digite o código da moeda (ex: USD-BRL): ").upper()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()

    chave = moeda.replace("-", "")
    info = dados[chave]

    print("Moeda:", moeda)
    print("Valor atual:", info["bid"])
    print("Máxima:", info["high"])
    print("Mínima:", info["low"])
    print("Última atualização:", info["create_date"])

except:
    print("Erro ao consultar a moeda ou moeda inexistente.")
