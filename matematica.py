# Funções matemática

def media(valores):
    soma = 0
    for i in range(0, len(valores)):
        soma += valores[i]
    return soma/len(valores)

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

def tabuada(x):
    tabuada = []
    for i in range(1, 11):
        tabuada.append(str(x) + ' x ' + str(i) + ' = ' + str(x*i))
    return tabuada

def fat_recursivo(n):
    if n > 1:
        fat = n * fat_recursivo(n - 1)
        return fat
    else:
        return 1

def validadorCPF(cpf):
    # Variáveis
    soma = 0
    cont = 10
    dv = 0

    if (len(cpf) == 11):

        for i in range(0, 9):
            soma += int(cpf[i]) * cont
            cont -= 1

        resto = soma % 11

        if resto >= 2:
            dv = 11 - resto
        else:
            dv = 0

        if int(cpf[9]) == dv:

            # Reinicialização das variáveis
            cont = 11
            soma = 0

            for i in range(0, 10):
                soma += int(cpf[i]) * cont
                cont -= 1

            resto = soma % 11

            if resto >= 2:
                dv = 11 - resto
            else:
                dv = 0

            if int(cpf[10]) == dv:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Teste Validador de CPF
print('CPF válido!') if validadorCPF('54647142949') else print('CPF inválido!')
print('CPF válido!') if validadorCPF('54747142949') else print('CPF inválido!')
print('CPF válido!') if validadorCPF('17824630706') else print('CPF inválido!')
print('CPF válido!') if validadorCPF('17824630806') else print('CPF inválido!')

# Teste Fatorial Recursivo
# print(f'{32}! = {fat_recursivo(32)}')

# Teste tabuada
'''
for x in tabuada(2):
    print(x)
'''

# Teste Fatorial
# print(f'\n {32}! = {fatorial(32)}')

# Teste Média

# Lista de valores
# x = [2, 3, 4, 5, 6]

# Saída
'''
print('A média de ', end='')
for valor in x:
    print(f' {valor} ', end='')
print(' é {:.0f}'.format(media(x)))
'''