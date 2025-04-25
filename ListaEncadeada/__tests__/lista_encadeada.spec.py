import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lista_encadeada import ListaEncadeada

class TestListaEncadeada(unittest.TestCase):

    def setUp(self):
        self.lista = ListaEncadeada()

    def test_inserir_como_primeiro(self):
        self.lista.inserir_como_primeiro(10)
        self.lista.inserir_como_primeiro(20)
        self.assertEqual(self.lista.get_lista(), [20, 10])

    def test_inserir_como_ultimo(self):
        self.lista.inserir_como_ultimo(30)
        self.lista.inserir_como_ultimo(40)
        self.assertEqual(self.lista.get_lista(), [30, 40])

    def test_inserir_na_posicao(self):
        self.lista.inserir_como_ultimo(1)
        self.lista.inserir_como_ultimo(3)
        self.lista.inserir_na_posicao(1, 2)
        self.assertEqual(self.lista.get_lista(), [1, 2, 3])

    def test_inserir_antes_depois_de(self):
        self.lista.inserir_como_ultimo(1)
        self.lista.inserir_como_ultimo(3)
        self.lista.inserir_depois_de(1, 2)
        self.lista.inserir_antes_de(3, 2.5)
        self.assertEqual(self.lista.get_lista(), [1, 2, 2.5, 3])

    def test_remover_primeiro_ultimo(self):
        self.lista.inserir_como_ultimo(1)
        self.lista.inserir_como_ultimo(2)
        self.lista.inserir_como_ultimo(3)
        self.lista.remover_primeiro()
        self.assertEqual(self.lista.get_lista(), [2, 3])
        self.lista.remover_ultimo()
        self.assertEqual(self.lista.get_lista(), [2])

    def test_removerDaPosicao(self):
        for i in range(5):
            self.lista.inserir_como_ultimo(i)
        self.lista.remover_da_posicao(2)
        self.assertEqual(self.lista.get_lista(), [0, 1, 3, 4])

    def test_remover(self):
        for i in [10, 20, 30, 40]:
            self.lista.inserir_como_ultimo(i)
        self.lista.remover(30)
        self.assertEqual(self.lista.get_lista(), [10, 20, 40])
        self.lista.remover(10)
        self.assertEqual(self.lista.get_lista(), [20, 40])
        self.lista.remover(40)
        self.assertEqual(self.lista.get_lista(), [20])

    def test_busca(self):
        for i in [5, 6, 7]:
            self.lista.inserir_como_ultimo(i)
        self.lista.busca(6)

        self.assertEqual(self.lista._cursor.valor, 6)
        self.lista.busca(10)
        self.assertIsNone(self.lista._cursor)

if __name__ == '__main__':
    unittest.main()
