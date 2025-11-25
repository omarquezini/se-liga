print ("[]=======================[]")
print ("[]                       []")
print ("[]   um monte de coisa   []")
print ("[]        nada ve        []")
print ("[]                       []")
print ("[]   por: O_MARQUEZINI   []")
print ("[]                       []")
print ("[]=======================[]")

entrada = int(input("Oque você quer fazer (1 para SIM) (2 para NÃO): "))

if entrada == 1:
        print("OK.")

        print("")
        print("=== QUAL A SUA IDADE? ===")
        print("")

        anoAtual = int(input("qual ano que você está: "))

        niver = int(input("qual ano você naceu: "))

        idade = (anoAtual - niver)

elif entrada == 2:
    print("infeismente você não tem escolha.")

    print("")
    print("=== QUAL O PRESSO DO SEUS ITENS? ===")
    print("")

    itens = int(input("qual o numero de itens: "))

    total = 0


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

else:
     print("numero incorreto ** ATIVAR ALTO DESTRUIÇÂO **")
     print("")
     print("3...")
     print("")
     print("")
     print("2..")
     print("")
     print("")
     print("1.")
     print("")
     exit()
   

print("")
print("=== QUAL O PRESSO DO SEUS ITENS? ===")
print("")

itens = int(input("qual o numero de itens: "))

total = 0


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