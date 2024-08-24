import random

print("AngelPass")
letras = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(']

letra_usuario = int(input("Elige la cantidad de letras: "))
numero_usuario = int(input("Elige la cantidad de numeros: "))
simbolo_usuario = int(input("Elige la cantidad de simbolos: "))
password_list = []
for letra in range(0, letra_usuario):
    password_list.append(random.choice(letras))

for numero in range(0, numero_usuario):
    password_list.append(random.choice(numeros))

for simbolo in range(0, simbolo_usuario):
    password_list.append(random.choice(simbolos))

random.shuffle(password_list)
password = ""
for i in password_list:
    password += i

print(password)