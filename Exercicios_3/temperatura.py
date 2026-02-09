'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

temperatura = float (input("Digite a temperatura: "))
origem = input("Digite a origem,(C) Celsius, (F) Fahrenheit e (K) Kelvin: ").upper()
destino = input("Digite a digite, (C) Celsius, (F) Fahrenheit e (k) Kelvin: ").upper()
if origem == "C" and destino =="F":
    resultado = (temperatura * 9/5) + 32
elif origem == "C" and destino == "K":
    resultado = temperatura + 273.15 
elif origem == "F" and destino =="C":
    resultado = (temperatura -32) * 5/9
    