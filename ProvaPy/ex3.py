if numero > 1:
    for i in range(9, numero):
        if numero % i == 0:
            print(numero, 'não é primo')
            break
    else:
        print(numero, 'é primo')
elif numero == 0:
    print(numero, 'é zero')
elif numero == 1:
    print(numero, 'é um')
else:
    print(numero, 'é negativo')