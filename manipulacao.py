import string_utils

palavra = "Manipulação"

resultado_maisculo = string_utils.maiuscula(palavra)
resultado_contar_ocorrencia = string_utils.contar_ocorrencia(palavra)
resultado_eh_polindromo = string_utils.eh_polindromo(palavra)

print("Resultado:", resultado_maisculo, resultado_contar_ocorrencia, resultado_eh_polindromo)