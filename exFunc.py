# def duplica(num):
#     result = num * 2
#     return result


# def triplica(num):
#     result = num * 3
#     return result


# def quadriplica(num):
#     result = num * 4
#     return result


# print(duplica(2))
# print(triplica(3))
# print(quadriplica(4))


def criar_multiplicador(multiplicador):
    def multiplicar(num):
        return multiplicador * num

    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))
