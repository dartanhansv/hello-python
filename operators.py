
# Operators
'''
# Comparison
==  Equal
!=  Not equal
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to



# Assignment

Atribuir valor:
x = 10

Somar 5 ou valor existente - "modo tradicional"
x = x + 5

Outra forma de alterar valor existente
x += 5
x -= 5
x *= 5
x /= 5

"O resto da divisão"
x %= 5



x = 10
y = 3
z = x % y
w = f' o resto de {x}/{y} é {z}'
print(w)



# Conditional Statements if/else
velocidade = float(input('Velocidade atual: '))

if velocidade > 110:
    print('Acima da Velocidade Permitida!')
    print("Favor Reduzir a sua velocidade!")
elif velocidade < 60:
    print('Favor dirigir acima de 80km/h!')
else:
    print('Velocidade OK!')



# Logical  and, or, not
# 1. and
renda_acima_5mil = True
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento Negado')


# 2. or
renda_acima_5mil = False
nome_limpo = True

if renda_acima_5mil or nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento Negado')


# Ternary Operators - Conditional Expressions

idade = int(input('Informe a sua idade: '))
resultado = 'Voto Permitido' if idade >= 16 else 'Voto não Permitido'
print(resultado)



# Multiple Comparison Operators

# 1.
valor = 30
if valor >= 20 and valor < 40:
    print('Produto Aceito')
else:
    print('Produto Recusado')

'''

# 2.
valor = 20
if 20 <= valor < 40:
        print('Produto Aceito')
else:
    print('Produto Recusado')

