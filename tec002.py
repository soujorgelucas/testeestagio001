# Função que verifica a presença e contagem da letra 'a' ou 'A' com entrada via input
def verificar_letra_a_input():
    # Solicita ao usuário que insira uma string
    string = input("Informe um texto para verificar a presença da letra 'a' ou 'A': ")
    
    # Verifica quantas vezes a letra 'a' ou 'A' aparece na string
    count_a = string.lower().count('a')
    
    # Retorna o resultado ao usuário
    if count_a > 0:
        return f"A letra 'a' ou 'A' aparece {count_a} vezes na string."
    else:
        return "A letra 'a' ou 'A' não foi encontrada na string."

# Chamando a função
print(verificar_letra_a_input())
