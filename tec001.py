# Função para verificar se um número pertence à sequência de Fibonacci com entrada via input
def pertence_fibonacci_input():
    # Solicitando ao usuário que insira um número
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    
    # Inicializando a sequência de Fibonacci
    fibonacci = [0, 1]
    
    # Gerando a sequência até que o último número seja maior ou igual ao número informado
    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    # Verificando se o número informado pertence à sequência
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência dgite Fibonacci."

# Chamando a função para verificar
print(pertence_fibonacci_input())
