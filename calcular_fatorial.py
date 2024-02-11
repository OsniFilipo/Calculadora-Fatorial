def calcular_fatorial(numero):
    if numero < 0:
        return "Erro: Não é possível calcular o fatorial de um número negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

def main():
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))
    resultado = calcular_fatorial(numero)
    if isinstance(resultado, int):
        print(f"O fatorial de {numero} é {resultado}.")
    else:
        print(resultado)

if __name__ == "__main__":
    main()
