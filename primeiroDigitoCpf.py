coletando = input("Digite o CPF: ")
cpf = 0
multiplicador = 10

for n in coletando:
    if n.isdigit():
        for digito in n:
            cpf = int(digito)
            print(cpf * multiplicador, end=" ")
            multiplicador -= 1
