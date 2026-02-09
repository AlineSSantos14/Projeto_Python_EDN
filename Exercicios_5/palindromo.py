'''2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo'''

def eh_palindromo(texto):
    texto_limpo = "".join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]

frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")
