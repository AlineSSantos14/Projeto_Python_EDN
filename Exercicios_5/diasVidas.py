'''4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.'''

from datetime import datetime

dia = int(input("Dia de nascimento: "))
mes = int(input("Mês de nascimento: "))
ano = int(input("Ano de nascimento: "))

data_nascimento = datetime(ano, mes, dia)
hoje = datetime.now()

dias_vivo = (hoje - data_nascimento).days

print("Você está vivo há", dias_vivo, "dias.")
