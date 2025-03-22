import os
import time
lista = []
i = 0
def adicionar_item():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=========== Supermercado Bora Bill ===========\n")
    print("   Adicione itens à lista de supermercado :\n")
    lista.append(input("   Digite o item: "))
def mostrar_lista():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=========== Supermercado Bora Bill ===========\n")
    print("         A lista de supermercado é:\n")
    for i in range(len(lista)):
        print(f"     {i+1}. {lista[i]}\n")
    print("==============================================\n")
def alterar_item():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=========== Supermercado Bora Bill ===========\n")
        print("         A lista de supermercado é:\n")
        for i in range(len(lista)):
            print(f"     {i+1}. {lista[i]}\n")
        item_alt = int(input(" Digite o número do item que deseja alterar: "))
        if item_alt > len(lista) or item_alt < 1:
            print(" Opção inválida! Tente novamente.")
            time.sleep(1)
            continue
        else:
            item_alt -= 1
            lista[item_alt] = input("\n Digite o novo item: ")
            break
def remover_item():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=========== Supermercado Bora Bill ===========\n")
        print("         A lista de supermercado é:\n")
        for i in range(len(lista)):
            print(f"     {i+1}. {lista[i]}\n")
        item_del = int(input(" Digite o número do item que deseja remover: "))
        item_del -= 1
        if item_del > len(lista) or item_del < 1:
            print(" Opção inválida! Tente novamente.")
            time.sleep(1)
            continue
        else:
            del lista[item_del]
            break
def salvar_lista():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=========== Supermercado Bora Bill ===========\n")
    nome_arquivo = input("Qual nome deseja salvar a lista: ")
    if not nome_arquivo.endswith('.txt'):
        nome_arquivo += '.txt'
    arquivo = open(nome_arquivo, 'w')
    arquivo.write("=========== Supermercado Bora Bill ===========\n")
    for i in range(len(lista)):
        arquivo.write(f"     {i+1}. {lista[i]}\n")
    arquivo.write("==============================================")
    arquivo.close()
while True:
    adicionar_item()
    novo_item = input("\n   Deseja adicionar outro item? (s/n): ")
    if novo_item.lower() == 's':
        continue
    elif novo_item.lower() == 'n':
        while True:
            mostrar_lista()
            escolha = int(input("\tAlterar(1)\tAdicionar(2)\n\n\tRemover(3)\t   Salvar(4)\n\nOque deseja fazer?"))
            match escolha:
                case 1:
                    alterar_item()
                case 2:
                    break
                case 3:
                    remover_item()
                case 4:
                    salvar_lista()
                    i = 1
                    break
                case _:
                    print("   Opção inválida! Tente novamente.")
                    time.sleep(1)
    else:
        print("   Opção inválida! Tente novamente.")
        time.sleep(1)
        continue
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Lista salva com sucesso!")
