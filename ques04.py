def validar_nome(nome):
    if len(nome) < 4:
        return False
    return True

def validar_idade(idade):
    if idade < 0 or idade > 150:
        return False
    return True

def validar_salario(salario):
    if salario < 0:
        return False
    return True

def validar_sexo(sexo):
    if sexo not in ['f', 'm']:
        return False
    return True

def validar_civil(civil):
    if civil not in ['s', 'c', 'v', 'd']:
        return False
    return True

def validar_informacoes(nome, idade, salario, sexo, civil):
    if not validar_nome(nome):
        return False
    if not validar_idade(idade):
        return False
    if not validar_salario(salario):
        return False
    if not validar_sexo(sexo):
        return False
    if not validar_civil(civil):
        return False
    return True

nome = input("Digite seu nome: ")
while not validar_nome(nome):
    nome = input("Nome inválido! Digite seu nome (mínimo 4 caracteres): ")

idade = int(input("Digite sua idade: "))
while not validar_idade(idade):
    idade = int(input("Idade inválida! Digite sua idade (entre 0 e 150 anos): "))

salario = float(input("Digite seu salário: "))
while not validar_salario(salario):
    salario = float(input("Salário inválido! Digite seu salário: "))

sexo = input("Digite seu sexo (f para feminino ou m para masculino): ").lower()
while not validar_sexo(sexo):
    sexo = input("Sexo inválido! Digite seu sexo (F para feminino ou M para masculino): ").lower()

civil = input("Digite seu estado civil (S para solteiro (a), C para casado(a), V para viúvo(a) ou D para divorciado(a)): ").lower()
while not validar_civil(civil):
    civil = input("Estado civil inválido! Digite seu estado civil (s, c, v ou d): ").lower()
