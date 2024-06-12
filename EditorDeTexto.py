import os

# Implementação da Pilha
class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return self.itens == []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            print("A pilha está vazia")

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            print("A pilha está vazia")
    
    def tamanho(self):
        return len(self.itens)

# Implementação da Fila
class Fila:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return self.itens == []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        else:
            print("A fila está vazia")

    def frente(self):
        if not self.esta_vazia():
            return self.itens[0]
        else:
            print("A fila está vazia")
    
    def tamanho(self):
        return len(self.itens)

# Implementação da Árvore Binária
class NoArvore:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.chave = chave

def inserir(raiz, chave):
    if raiz is None:
        return NoArvore(chave)
    else:
        if raiz.chave < chave:
            raiz.direita = inserir(raiz.direita, chave)
        else:
            raiz.esquerda = inserir(raiz.esquerda, chave)
    return raiz

def inorder(raiz):
    if raiz:
        inorder(raiz.esquerda)
        print(raiz.chave, end=" ")
        inorder(raiz.direita)

# Funções do Editor de Texto
def exibir_menu():
    print("\nEditor de Texto")
    print("1. Criar novo arquivo")
    print("2. Abrir arquivo existente")
    print("3. Salvar arquivo")
    print("4. Editar arquivo")
    print("5. Sair")

def criar_arquivo():
    nome = input("Digite o nome do novo arquivo: ")
    with open(nome, 'w', encoding='utf-8') as arquivo:
        conteudo = input("Digite o conteúdo do arquivo: ")
        arquivo.write(conteudo)
    print(f"Arquivo '{nome}' criado com sucesso.")

def abrir_arquivo():
    nome = input("Digite o nome do arquivo a ser aberto: ")
    if os.path.exists(nome):
        with open(nome, 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())
    else:
        print("Arquivo não encontrado.")

def salvar_arquivo():
    nome = input("Digite o nome do arquivo a ser salvo: ")
    conteudo = input("Digite o conteúdo a ser salvo: ")
    with open(nome, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
    print(f"Arquivo '{nome}' salvo com sucesso.")

def editar_arquivo():
    nome = input("Digite o nome do arquivo a ser editado: ")
    if os.path.exists(nome):
        with open(nome, 'r', encoding='utf-8') as arquivo:
            conteudo_atual = arquivo.read()
        print("Conteúdo atual do arquivo:")
        print(conteudo_atual)
        novo_conteudo = input("Digite o novo conteúdo do arquivo: ")
        with open(nome, 'w', encoding='utf-8') as arquivo:
            arquivo.write(novo_conteudo)
        print(f"Arquivo '{nome}' editado com sucesso.")
    else:
        print("Arquivo não encontrado.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            criar_arquivo()
        elif opcao == '2':
            abrir_arquivo()
        elif opcao == '3':
            salvar_arquivo()
        elif opcao == '4':
            editar_arquivo()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
