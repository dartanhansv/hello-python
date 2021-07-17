'''
- Slice
Cortar/fatiar variável
Utilizar parte do valor atribuído
Buscar a valor desejado pela posição na variável
A primeira posição é o zero. Index = 012343...
'''

hostname = 'XPTO-SPO-RTD01'

# Exibir valor da variável
print(hostname)

# Exibir o valor do index zero; o primeiro caractere
print(hostname[0])

# Exibir o valor do index -1; a último caractere
print(hostname[-1])

# Exibir os três primeiros caracteres
print(hostname[0:4])

# Exibir os 5 últimos caracteres
print(hostname[-5:])

# Caracteres da 5ª a 7ª index (Lembrete: index começa no 0)
print(hostname[5:8])

# Necessário mudar tipo da variável de integer para string
price = 12.34
price = str(price)
print(price[-2:])