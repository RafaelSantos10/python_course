import os

palavra_secreta = "dinossauro"
letras_certas = ""
numero_tenativas = 0


while True:
    letra = input("Digite uma letra: ")
    numero_tenativas += 1

    if len(letra) > 1:
        print("Digite apenas uma letra")
        continue

    if letra in palavra_secreta:
        letras_certas += letra

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("clear")
        print("VOCÊ GANHOU PARABÉNS !!!")
        print(f"A palavra secreta era, {palavra_secreta}")
        print(f"Numero de tentativs: {numero_tenativas}")
        letras_certas = ""
        numero_tenativas = 0
        break
