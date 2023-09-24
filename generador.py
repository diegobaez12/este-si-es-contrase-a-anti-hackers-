import random

long = int(input("dime la longitud de tu contraseña:"))
char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
while True:
    for i in range(long):
        element = random.choice(char)
        print(element)
        password += element
    print("tu contraseña generada es:",password)
    pregunta = input("quieres crear otra contra?:")
    if pregunta == "si":
        print("ok!")
    elif pregunta == "no":
        print("ok!")
        break
