n = int(input("Digite a quantidade de valores que serão determinados: "))
maior = menor = soma = 0

for i in range(n):
  numero = float(input(f"Digite o {i+1}º número: "))
  
  if i == 0:
      maior = menor = numero
  else:
      if numero > maior:
          maior = numero
      if numero < menor:
          menor = numero
      
  soma += numero

print(f"O maior valor é {maior}, o menor valor é {menor} e a soma é {soma}.")