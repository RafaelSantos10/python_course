# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]

acertos = 0
erros = 0
qtd_perguntas = 0


for index, pergunta in enumerate(perguntas):
    qtd_perguntas = len(perguntas)
    print(f"Questão 0{index + 1}:", pergunta["Pergunta"])
    print()
    for index, option in enumerate(pergunta["Opções"]):
        print(f"{index})", option)

    print()
    resposta_quest = input("Escolha uma opção: ")
    if resposta_quest == pergunta["Resposta"]:
        print("Você acertou !!!")
        acertos += 1
        print()

    else:
        print("Você errou !!!")
        erros += 1
        print()


if acertos > erros:
    print(f"Parabéns, você acertou {acertos} de {qtd_perguntas} perguntas")
else:
    print(f"Você é muito burro, errou {erros} de {qtd_perguntas} perguntas")
