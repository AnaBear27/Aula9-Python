#CRIANDO UM MÓDULO DE CÁLCULOS MATEMÁTIOS.

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Divisão por zero não é permitida.")