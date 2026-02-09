'''2 -  Crie um programa que  acesse a API Random User Generator para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.'''

import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()
    usuario = dados["results"][0]

    nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Nome:", nome)
    print("E-mail:", email)
    print("País:", pais)

except:
    print("Falha ao acessar a API Random User.")