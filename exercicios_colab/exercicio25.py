n1, n2 = 0, 1
print(n1)
print(n2)
for _ in range(8):  # Já imprimi os dois primeiros números
    n3 = n1 + n2
    print(n3)
    n1, n2 = n2, n3
