'''
No Python diferente da maioria das demais linguagens, não há necessidade de declarar o tipo da variável,
basta atribuir o valor com simbolo "="
'''

# Exemplos de Variáveis

# Tipo string - Texto
nome = "D'Artagnan"
profissao = 'Mosqueteiro'


# Tipo float
altura = 1.80

# Tipo inteiro
idade = 32

# Tipo complex - estatística
complexo = 1+3j

# Tipo bool - Booleano
casado = True
filhos = False


# LISTAS
#Tipo Array
equipe = ['Athos', 'Porthos']

# Operações com arrays
equipe.append('Aramis') # Adiciona um objeto na última posição do Array
equipe.insert(0, 'Tréville') # Insere um objeto em uma posição específica do Array
# a primeira posição do array é o Zero

equipe.append('Tréville')

# Remove um objeto no array pelo nome
equipe.remove('Tréville')

# Remove um objeto no array pela posição
equipe.pop(3)



# Listas tipo chave:valor - dict(dicionário)

livros = {}

livros['titulo'] = 'A Arte da Prudência'
livros['ano'] = 1647

pessoa = {'nome':'José da Silva', 'idade':30, 'altura': 1.8, 'peso': 93}
'''
 Os métodos do dicionário são parecidos com uma função, 
 possuem parametros e retornam valores, mas a sintaxe é diferente.
'''

pessoa.keys() # Retorna a lista com os índices

pessoa.values() # Retorna a lista com os valores