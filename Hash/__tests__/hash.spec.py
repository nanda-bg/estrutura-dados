import unittest

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hash import Hash

class TestHash(unittest.TestCase):

    def setUp(self):
        self.tabela = Hash(5)

    def test_funcao_hash(self):
        self.assertEqual(self.tabela.funcao_hash(10), 0)
        self.assertEqual(self.tabela.funcao_hash(15), 0)
        self.assertEqual(self.tabela.funcao_hash(20), 0)
        self.assertEqual(self.tabela.funcao_hash(7), 2)
        self.assertEqual(self.tabela.funcao_hash(3), 3)

    def test_inserir_sem_colisao(self):
        self.tabela.inserir(7)
        self.tabela.inserir(3)
        self.assertEqual(self._get_bucket_elements(2), [7])
        self.assertEqual(self._get_bucket_elements(3), [3])
        self.assertTrue(self._bucket_vazia(0))
        self.assertTrue(self._bucket_vazia(1))
        self.assertTrue(self._bucket_vazia(4))

    def test_inserir_com_colisao(self):
        self.tabela.inserir(10)
        self.tabela.inserir(15)
        self.tabela.inserir(20)
        self.assertEqual(self._get_bucket_elements(0), [10, 15, 20])

    def test_inserir_multiplos_buckets(self):
        valores = [10, 15, 20, 7, 3]
        for v in valores:
            self.tabela.inserir(v)
        
        self.assertEqual(self._get_bucket_elements(0), [10, 15, 20])
        self.assertEqual(self._get_bucket_elements(2), [7])
        self.assertEqual(self._get_bucket_elements(3), [3])
        self.assertTrue(self._bucket_vazia(1))
        self.assertTrue(self._bucket_vazia(4))

    def _get_bucket_elements(self, index):
        elementos = []
        atual = self.tabela.table[index]._primeiro

        while atual:
            elementos.append(atual.valor)
            atual = atual.prox

        return elementos

    def _bucket_vazia(self, index):
        return self.tabela.table[index]._primeiro is None

if __name__ == '__main__':
    unittest.main()
