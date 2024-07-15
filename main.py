def boolean(VorF):
    VorF = VorF.lower()
    if VorF == "sim":
        return True
    elif VorF == "não":
        return False
    else:
        raise ValueError("Entrada inválida. Por favor, insira 'sim' ou 'não'.")

produtos = []

while True:
    Nome = input("Nome do produto: ")
    Desc = input("Descrição do produto: ")
    Valor = input("Qual o valor do produto: ")

    while True:
        Disp = input("Disponível para venda (sim/não): ")
        try:
            Disponivel = boolean(Disp)
            break
        except ValueError as e:
            print(e)

    produto = {
        "Nome": Nome,
        "Desc": Desc,
        "Valor": float(Valor),
        "Disp": Disponivel
    }
    produtos.append(produto)

    produtos_ordenados = sorted(produtos, key=lambda x: x["Valor"])

    print("\nProdutos cadastrados até agora:")
    print("\nOrdem Crescente")
    for produto in produtos:
        print("Nome: ", produto["Nome"])
        #print("Desc: ", produto["Desc"])
        print("Valor: ", produto["Valor"])
        #print("Disponivel: ", "Sim" if produto["Disp"] else "Não")

    continuar = input("Deseja cadastrar outro produto? (sim/não): ")
    if continuar.lower() != "sim":
        break

#Bloco opcional
"""
produtos_ordenados = sorted(produtos, key=lambda x: x["Valor"])

print("\nCadastro finalizado:")
print("\nOrdem Crescente")
for produto in produtos:
    print("Nome: ", produto["Nome"])
    print("Desc: ", produto["Desc"])
    print("Valor: ", produto["Valor"])
    print("Disponivel: ", "Sim" if produto["Disp"] else "Não")
"""
