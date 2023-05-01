nome = input("Qual o é seu nome? ")
newName = ""
i = 0

while i < len(nome):
    newName += nome[i] + "*"

    i += 1

print(newName)
