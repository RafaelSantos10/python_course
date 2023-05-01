"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input('Digite um numero inteiro:')


# try:

#     num_form = int(numero)

#     if num_form % 2 == 0:
#         print('numero é par')
#     elif num_form % 2 == 1:
#         print('numero é impar')

# except:

#     print('Digite um numero inteiro valido')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horas = input('Que horas são? ')

# try:

#     horas_int = int(horas)

#     if horas_int == 0 or horas_int <= 11:
#         print('Bom dia')
#     elif horas_int == 12 or horas_int <= 17:
#         print('Boa tarde')
#     elif horas_int == 18 or horas_int <= 23:
#         print('Boa noite')

# except:
# print('Digite um horario valido')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')

elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal')

elif len(nome) > 6:
    print('Seu nome é grande')
