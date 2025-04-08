n=input("Introduce un número: ")
factorial=1
cont = 1
while cont <= int(n):
    factorial = factorial * cont
    cont += 1
print(f"El factorial de {n} es {factorial}")