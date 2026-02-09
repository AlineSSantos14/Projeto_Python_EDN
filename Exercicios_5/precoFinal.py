'''3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
'''

def calcular_desconto(preco, porcentagem):
    return preco * (porcentagem / 100)

def preco_final(preco, porcentagem):
    desconto = calcular_desconto(preco, porcentagem)
    return round(preco - desconto, 2)

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

final = preco_final(preco, desconto)

print(f"Preço final com desconto: R$ {final:.2f}")
