#CRIANDO UM MÓDULO DE MANIPULAÇÃO DE STRINGS.

def maiuscula(texto):
    return texto.upper()

def contar_ocorrencia(texto, caractere):
    return texto.count(caractere)

def eh_polindromo(texto):
    texto_sem_espacos = texto.replace(" ", "")
    return texto_sem_espacos == texto_sem_espacos[::-1]