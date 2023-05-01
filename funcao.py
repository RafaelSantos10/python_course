def mult(*args):
    total = 1

    for num in args:
        total *= num
    return total


def isPar(num):
    return num % 2 == 0


def result():
    num = mult(1, 3, 5, 7)
    print(num)
    if isPar(num):
        print("O resultado é par")
    else:
        print("O resultado é ímpar")


result()
