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