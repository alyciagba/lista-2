n = int(input("Digite a quantidade de valores que serão determinados: "))
maior = menor = soma = 0

for i in range(n):
 numero = int(input(f"Digite o {i+1}º número: "))
 
 if 0 <= numero <= 1000:
     if i == 0:
         maior = menor = numero
     else:
         if numero > maior:
             maior = numero
         if numero < menor:
             menor = numero
     
     soma += numero
 else:
     print(f"O número {numero} não está entre 0 e 1000. Tente novamente.")
     i -= 1

print(f"O maior valor é {maior}, o menor valor é {menor} e a soma é {soma}.")

