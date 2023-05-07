
# Modules
# fuction > module > package > library

# Functions
    # DRY - Don't repeat yourself

# In Python a fuction is defined using the 'def' keyword


'''
# Função para executar uma tarefa específica (print, por exemplo)
def boas_vindas(nome, quantidade):
    print(f'Olá {nome}!')
    print(f'Temos {str(quantidade)} notebooks em estoque.')


boas_vindas('João', 5)
boas_vindas('Maria', 3)
boas_vindas('José', 2)

# argumentos com valor definidos(default) após argumentos sem valor definido
def boas_vindas(quantidade, nome='Juca'):
    print(f'Olá {nome}!')
    print(f'Temos {str(quantidade)} notebooks em estoque.')

boas_vindas(5)

# Função para gerar valor de retorno que pode ser atribuiado a uma var
def salario(valor_hr,hr_trabalho):
    return valor_hr * hr_trabalho

gerente = salario(97, 200)
print(gerente)

gerente_ano = gerente * 12
print(gerente_ano)


# função com N argumentos - xargs
# O '*' indica que o numero total de argumentos não é definido
def soma(*numeros):
    resultado = 0 #valor inicial
    for k in numeros:.0
        resultado += k
    return resultado

x = soma(1, 2, 3)
print(x)

'''
# Identificar/nomear paramentros dos n argumentos xargs

def agencia(**carro):
    return carro

print(agencia(modelo='gol', cor='branco', motor=1.0))
print(agencia(modelo='celta', cor='preto'))
print(agencia(modelo='corsa', motor=1.0))
print(agencia(modelo='golf', cor='prata', motor=2.0))




