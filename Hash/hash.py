import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ListaEncadeada.lista_encadeada import ListaEncadeada
 
class Hash:
    def __init__(self, size):
        self.size = size
        self.table = [ListaEncadeada() for _ in range(size)]

    def funcao_hash(self, key):
        """
        Função hash simples que calcula o índice da tabela hash.
        """

        return key % self.size

    def inserir(self, key):
        """
        Insere uma chave na tabela hash.
        Se a posição já estiver ocupada, utiliza o método de encadeamento para lidar com colisões.
        """

        index = self.funcao_hash(key)
        

        if self.table[index] is None:
            self.table[index] = [key]
        else:
            self.table[index].inserir_como_ultimo(key)  

    def imprimir_tabela(self):
        """
        Cada índice da tabela é impresso com seus elementos encadeados.
        """
        for i, lista in enumerate(self.table):
            print(f"Índice {i}:", end=" ")
            lista.imprimir()

def main():
    tabela = Hash(5)

    tabela.inserir(10)
    tabela.imprimir_tabela()
    print()
    print()

    tabela.inserir(15)
    tabela.imprimir_tabela()
    print()
    print()

    tabela.inserir(20)
    tabela.imprimir_tabela()
    print()
    print()

    tabela.inserir(7)
    tabela.imprimir_tabela()
    print()
    print()

    tabela.inserir(3)
    tabela.imprimir_tabela()          
