print ("[]=======================[]")
print ("[]                       []")
print ("[]   um monte de coisa   []")
print ("[]        nada ve        []")
print ("[]                       []")
print ("[]   por: O_MARQUEZINI   []")
print ("[]                       []")
print ("[]=======================[]")

entrada = int(input("você quer sair? (1 para SIM) (2 para NÃO): "))

if entrada == 1:
        print("OK.")
else:
     print("infeismente você não tem escolha.")
   
print("")
print("=== QUAL A SUA IDADE? ===")
print("")

anoAtual = int(input("qual ano que você está: "))

niver = int(input("qual ano você naceu: "))

idade = (anoAtual - niver)

print(f"sua idade aproximada é: {idade}")



itens = int(input("qual o numero de itens: "))

total = 0

print("")
print("=== QUAL O PRESSO DO SEUS ITENS? ===")
print("")

while True:

    preco = float(input("digite o preço do seu iten: "))
    total += preco
    itens -= 1

    precoFIN = preco 

    if itens == 0:
        print(f"R${total}")
        break
    else:
        True

print("")
print("=== QUAL O SEU FINAL??? ===")
print("")

while True:
    saida = int(input("Você quer sair? (1 para SIM) (2 para NÃO): "))

    if saida == 1:
        print("OK, tchau.")
        break
    elif saida == 2:
        print("OK...")
    else:
        print("Número incorreto...idiota.")