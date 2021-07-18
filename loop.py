
# Looping

# For Loop
# Print from 1 to 100
# Remember: starts with Zero in Python
#1
'''
for i in range(101):
    print(i)

#2 To exclude Zero
for i in range(1, 101):
    print(i)


#3 Step - Determine the increment
# Print odd numbers from 0 to 100
for i in range(1, 101, 2):
    print(i)



# For loop with strings
# 1.
palavra = ('Python')
for letras in palavra:
    print(letras)


# 2.
palavra = ('Python')
for letras in palavra:
    print(f'{letras} is within the word {palavra}')



# Foor Loop with conditional statements

compra_confirmada = True
dados_compra = 'Compra no valor de de R$12.50 e entrega confirmada'

for i in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
        break
    else:
        print('Falha na compra')


# Nested Loops - a loop (inner) inside a loop (outer)
# THe inner loop wil be executed one time for each round of the outer loop

for number1 in range(1, 6):
    print('Product ' + str(number1))
    for number2 in range(1, 11):
        print(number1, number2)


headline = ('headline')

for k in headline:
    print(k, end=" ")



# For fun - Print a rectangle/square pattern

line = 6
row = 6
symbol = '$'

for l in range(line):
    for r in range(row):
        print(symbol, end="") 
    print('')    


# While Loop

custo = 20
valor = 100
valor = float(valor)
dia = 1

while valor > custo:
    print(f' O valor no {dia} será: R${valor}')
    valor -=5
    dia +=1

'''
valor = int(input('Digite o valor do seu Produto: '))

while valor > 20:
    valor = (valor * 0.1) + valor
    print(f' O valor do produto + 10% é igual a: R${valor}')
    break





# if/else Basic True or False
# For Loop = is better when you know how many times it shall run: "Do it for 5 times"
# While Loop = you don't know how many times, you have a goal. "Do it until 'it' happens"