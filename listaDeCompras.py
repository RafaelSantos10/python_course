listaCompras = []

while True:
    print("########### LISTA DE COMPRAS ##########")
    opcao = input("[i]nserir [a]pagar [l]istar: ")

    if opcao == "i":
        item = input("Digite o item: ")
        listaCompras.append(item)
        print("o item foi adicionado com sucesso.")
        continue

    elif opcao == "a":
        index = input("Digite o numero do item que quer remover: ")
        num_index = 0
        item_removido = ""

        try:
            num_index = int(index)
            try:
                item_removido = listaCompras.pop(num_index)
            except:
                print("Numero digitado é maior que a quantidade de items na lista")

        except:
            print("Digite um numero válido")
        if item_removido:
            print(f"o item '{item_removido}' foi removido com sucesso.")
    elif opcao == "l":
        for index, item in enumerate(listaCompras):
            print(f"{index} - {item}")
            continue

    else:
        print(" Porfavor escolha uma opção válida")
