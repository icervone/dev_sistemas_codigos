# Passagem por Valor
def levelUp(idade):
    raphael += 1
    # O += é a mesma coisa que escrever 
    # raphael = raphael + 1
    print('Idade atual:', idade)

def levelDown(idade):
    idade = idade - 1
    # Mesma coisa de idade -= 1
    return idade

idade = 10
levelUp(idade)
print('Idade depois da função:', idade)