import os
os.system('cls')

estoque = {}

def adicionar_produto(nome, quantidade, preco):
    estoque[nome] = {'quantidade': quantidade, 'preco': preco}

def atualizar_preco(nome, novo_preco):
    if nome in estoque:
        estoque[nome]['preco'] = novo_preco
    else:
        print(f"Produto '{nome}' não encontrado no inventário.")
 
def listar_produtos():
    print('novo valor dos produtos do estoque:')
    for nome, info in estoque.items():
        print(f"Nome: {nome}, Quantidade: {info['quantidade']}, Preço: {info['preco']:.2f}")

def valor_total_estoque():
    total = sum(info['quantidade'] * info['preco'] for info in estoque.values())
    return total

adicionar_produto('banana', 7, 2.00)
adicionar_produto('limao', 9, 1.20)
adicionar_produto('laranja', 10, 2.30)
adicionar_produto('maça', 12, 1.80)
adicionar_produto('mamao', 5, 3.00)

listar_produtos()

atualizar_preco('banana', 2.20)
atualizar_preco('limao', 1.60)
atualizar_preco('laranja', 2.50)
atualizar_preco('maça', 2.00)
atualizar_preco('mamao', 2.90)

listar_produtos()

total_estoque = valor_total_estoque()
print(f'Valor total em estoque: {total_estoque:.2f}')
