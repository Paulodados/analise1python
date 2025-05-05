numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(5)]
numeros_pares = [num for num in numeros if num % 2 == 0]
print("Os números pares são:", numeros_pares)