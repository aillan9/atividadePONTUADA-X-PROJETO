import os
os.system ("cls || clear")

 # ATIVIDADE FEITA POR: FÁBIO DE CARVALHO, RUAN DUARTE E AILLAN LIMA
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor, ano):
        self.livros.append({'titulo': titulo, 'autor': autor, 'ano': ano, 'vendido': False})

    def mostrar_livros(self):
        return self.livros

    def remover_livro(self, titulo):
        self.livros = [livro for livro in self.livros if livro['titulo'] != titulo]

    def comprar_livro(self, titulo):
        for livro in self.livros:
            if livro['titulo'] == titulo:
                livro['vendido'] = True
                break

    def menu(self):
        while True:
            print("\n1. Adicionar Livro\n2. Mostrar Livros\n3. Remover Livro\n4. Comprar Livro\n5. Sair")
            escolha = input("Escolha uma opção: ")
            if escolha == '1':
                titulo = input("Título: ")
                autor = input("Autor: ")
                ano = input("Ano: ")
                self.adicionar_livro(titulo, autor, ano)
            elif escolha == '2':
                livros = self.mostrar_livros()
                for livro in livros:
                    status = "Vendido" if livro['vendido'] else "Disponível"
                    print(f"{livro['titulo']} por {livro['autor']} ({livro['ano']}) - {status}")
            elif escolha == '3':
                titulo = input("Título do livro a remover: ")
                self.remover_livro(titulo)
            elif escolha == '4':
                titulo = input("Título do livro a comprar: ")
                self.comprar_livro(titulo)
            elif escolha == '5':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    sistema = Biblioteca()
    sistema.menu()