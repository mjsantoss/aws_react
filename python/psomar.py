# Função que recebe dois parâmetros e retorna a soma
def somar(a, b):
    return a + b

# Função principal que executa o programa
def main():
    # Solicitando entrada do usuário para os dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Chamando a função somar e exibindo o resultado
    resultado = somar(num1, num2)
    
    # Exibindo o resultado da soma
    print(f"A soma de {num1} e {num2} é: {resultado}")

# Executando o programa
if __name__ == "__main__":
    main()
