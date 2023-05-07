from datetime import date


'''
Solicitar dado ao usuário 
Atribuir a resposta à uma variável
'''
born = input('Em que ano você nasceu? ')
today = date.today()

print("Então você tem ", today.year - int(born), "anos. Jovem ainda, mas amanhã velho será!")