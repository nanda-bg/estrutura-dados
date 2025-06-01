import os
import unittest
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lista_encadeada_estendida import ListaEncadeadaEstendida, Nó

class TestNó(unittest.TestCase):
    """Testes para a classe Nó"""
    
    def setUp(self):
        """Configuração executada antes de cada teste"""
        self.no = Nó()
    
    def test_inicializacao(self):
        """Testa se o nó é inicializado corretamente"""
        self.assertIsNone(self.no.prox)
        self.assertEqual(self.no.contador, 0)
        self.assertEqual(len(self.no.array), 8)
        self.assertTrue(all(item is None for item in self.no.array))
    
    def test_esta_cheio_no_vazio(self):
        """Testa está_cheio() com nó vazio"""
        self.assertFalse(self.no.está_cheio())
    
    def test_esta_cheio_no_parcialmente_preenchido(self):
        """Testa está_cheio() com nó parcialmente preenchido"""
        self.no.inserir_ordenado(5)
        self.no.inserir_ordenado(10)
        self.assertFalse(self.no.está_cheio())
    
    def test_esta_cheio_no_completo(self):
        """Testa está_cheio() com nó completamente preenchido"""
        for i in range(8):
            self.no.inserir_ordenado(i)

        self.assertTrue(self.no.está_cheio())
    
    def test_inserir_ordenado_primeiro_elemento(self):
        """Testa inserção do primeiro elemento"""
        resultado = self.no.inserir_ordenado(5)

        self.assertTrue(resultado)
        self.assertEqual(self.no.array[0], 5)
        self.assertEqual(self.no.contador, 1)
    
    def test_inserir_ordenado_ordem_crescente(self):
        """Testa inserção mantendo ordem crescente"""
        valores = [3, 1, 4, 2]

        for valor in valores:
            self.no.inserir_ordenado(valor)

        elementos_ordenados = [1, 2, 3, 4]

        for i in range(4):
            self.assertEqual(self.no.array[i], elementos_ordenados[i])

        self.assertEqual(self.no.contador, 4)
    
    def test_inserir_ordenado_valores_duplicados(self):
        """Testa inserção de valores duplicados"""
        self.no.inserir_ordenado(5)
        self.no.inserir_ordenado(5)
        self.no.inserir_ordenado(3)
        
        self.assertEqual(self.no.array[0], 3)
        self.assertEqual(self.no.array[1], 5)
        self.assertEqual(self.no.array[2], 5)
        self.assertEqual(self.no.contador, 3)
    
    def test_inserir_ordenado_sequencia_completa(self):
        """Testa inserção até completar o array"""
        valores = [8, 1, 6, 3, 7, 2, 5, 4]

        for valor in valores:
            self.no.inserir_ordenado(valor)
        
        for i in range(8):
            self.assertEqual(self.no.array[i], i + 1)

        self.assertTrue(self.no.está_cheio())
    
    def test_remover_elemento_existente(self):
        """Testa remoção de elemento existente"""
        valores = [1, 3, 5, 7]

        for valor in valores:
            self.no.inserir_ordenado(valor)
        
        self.assertEqual(self.no.contador, 4)

        resultado = self.no.remover(3)

        self.assertTrue(resultado)
        self.assertEqual(self.no.contador, 3)
        self.assertEqual(self.no.array[0], 1)
        self.assertEqual(self.no.array[1], 5)
        self.assertEqual(self.no.array[2], 7)
        self.assertIsNone(self.no.array[3])
    
    def test_remover_elemento_inexistente(self):
        """Testa remoção de elemento que não existe"""
        self.no.inserir_ordenado(1)
        self.no.inserir_ordenado(3)
        
        resultado = self.no.remover(5)

        self.assertFalse(resultado)
        self.assertEqual(self.no.contador, 2)
    
    def test_remover_primeiro_elemento(self):
        """Testa remoção do primeiro elemento"""
        valores = [1, 2, 3]

        for valor in valores:
            self.no.inserir_ordenado(valor)
        
        resultado = self.no.remover(1)

        self.assertTrue(resultado)
        self.assertEqual(self.no.array[0], 2)
        self.assertEqual(self.no.array[1], 3)
        self.assertEqual(self.no.contador, 2)
    
    def test_remover_ultimo_elemento(self):
        """Testa remoção do último elemento"""
        valores = [1, 2, 3]

        for valor in valores:
            self.no.inserir_ordenado(valor)
        
        resultado = self.no.remover(3)

        self.assertTrue(resultado)
        self.assertEqual(self.no.contador, 2)
        self.assertIsNone(self.no.array[2])


class TestInserçãoListaEncadeadaEstendida(unittest.TestCase):
    def setUp(self):
        self.lista = ListaEncadeadaEstendida()

    def test_inicializacao(self):
        """Testa inicialização da lista"""
        self.assertIsNone(self.lista.primeiro)
        self.assertIsNone(self.lista.ultimo)
        self.assertIsNone(self.lista.atual)

    def test_inserir_primeiro_elemento(self):
        """Testa inserção do primeiro elemento na lista vazia"""
        self.lista.inserir(5)
        self.assertIsNotNone(self.lista.primeiro)
        self.assertEqual(self.lista.primeiro.array[0], 5)
        self.assertEqual(self.lista.primeiro.contador, 1)

    def test_inserir_multiplos_elementos_mesmo_no(self):
        """Testa inserção de múltiplos elementos no mesmo nó"""
        valores = [3, 1, 4, 2]
        for valor in valores:
            self.lista.inserir(valor)
        primeiro_no = self.lista.primeiro
        self.assertEqual(primeiro_no.contador, 4)
        self.assertEqual(primeiro_no.array[0], 1)
        self.assertEqual(primeiro_no.array[1], 2)
        self.assertEqual(primeiro_no.array[2], 3)
        self.assertEqual(primeiro_no.array[3], 4)

    def test_inserir_provocando_split(self):
        """Testa inserção que provoca split do nó"""
        for i in range(1, 9):
            self.lista.inserir(i)
        self.assertTrue(self.lista.primeiro.está_cheio())
        self.lista.inserir(5)
        self.assertIsNotNone(self.lista.primeiro.prox)
        primeiro_no = self.lista.primeiro
        segundo_no = self.lista.primeiro.prox
        self.assertEqual(primeiro_no.contador, 4)
        self.assertEqual(primeiro_no.array[0], 1)
        self.assertEqual(primeiro_no.array[3], 4)
        self.assertEqual(segundo_no.contador, 5)

    def test_achar_no_primeiro_no(self):
        """Testa _achar_nó quando o valor deve ir no primeiro nó"""
        for i in [3, 7, 10]:
            self.lista.inserir(i)
        self.lista._achar_nó(5)
        self.assertEqual(self.lista.atual, self.lista.primeiro)

    def test_achar_no_com_multiplos_nos(self):
        """Testa _achar_nó com múltiplos nós"""
        for i in range(1, 17):
            self.lista.inserir(i)
        self.lista._achar_nó(10)
        self.assertIsNotNone(self.lista.atual)

    def test_ir_para_primeiro_no(self):
        """Testa navegação para o primeiro nó"""
        self.lista.inserir(5)
        self.lista._ir_para_primeiro_nó()
        self.assertEqual(self.lista.atual, self.lista.primeiro)

    def test_ir_para_ultimo_no(self):
        """Testa navegação para o último nó"""
        self.lista.inserir(5)
        self.lista._ir_para_ultimo_nó()
        self.assertEqual(self.lista.atual, self.lista.ultimo)

    def test_split_distribui_elementos_corretamente(self):
        """Testa se o split distribui os elementos corretamente"""
        valores = [1, 2, 3, 4, 5, 6, 7, 8]
        for valor in valores:
            self.lista.inserir(valor)
        self.lista.inserir(9)
        primeiro_no = self.lista.primeiro
        segundo_no = self.lista.primeiro.prox
        self.assertLessEqual(primeiro_no.contador, 4)
        self.assertGreaterEqual(segundo_no.contador, 4)
        self.assertLessEqual(primeiro_no.array[primeiro_no.contador-1], segundo_no.array[0])

    def test_sequencia_insercoes_complexa(self):
        """Testa uma sequência complexa de inserções"""
        valores = [15, 3, 8, 1, 12, 20, 7, 25, 2, 18, 9, 30, 5, 14, 22, 11]
        for valor in valores:
            self.lista.inserir(valor)
        self.assertIsNotNone(self.lista.primeiro)
        self.assertIsNotNone(self.lista.primeiro.prox)


class TestRemoçãoListaEncadeadaEstendida(unittest.TestCase):
    def setUp(self):
        self.lista = ListaEncadeadaEstendida()

    def test_remover_elemento_existente(self):
        valores = [5, 2, 8, 1, 9]
        for v in valores:
            self.lista.inserir(v)
        self.assertTrue(self.lista.remover(5))
        self.assertEqual(str(self.lista), "[1, 2, 8, 9]")
        self.assertTrue(self.lista.remover(9))
        self.assertEqual(str(self.lista), "[1, 2, 8]")
        self.assertTrue(self.lista.remover(1))
        self.assertEqual(str(self.lista), "[2, 8]")

    def test_remover_elemento_inexistente(self):
        valores = [3, 7, 9]
        for v in valores:
            self.lista.inserir(v)
        self.assertFalse(self.lista.remover(5))
        self.assertEqual(self.lista.contar_elementos(), 3)

    def test_remover_elemento_e_excluir_no_vazio(self):
        for v in [4, 1, 6]:
            self.lista.inserir(v)
        self.lista.remover(1)
        self.lista.remover(4)
        self.lista.remover(6)
        self.assertEqual(self.lista.contar_elementos(), 0)
        self.assertIsNone(self.lista.primeiro)
        self.assertIsNone(self.lista.ultimo)

    def test_remover_elemento_em_no_cheio(self):
        for v in range(10):
            self.lista.inserir(v)
        self.assertTrue(self.lista.remover(8))
        self.assertEqual(str(self.lista), "[0, 1, 2, 3] -> [4, 5, 6, 7, 9]")
        self.assertEqual(self.lista.contar_elementos(), 9)

    def test_remover_unico_elemento(self):
        self.lista.inserir(7)
        self.assertTrue(self.lista.remover(7))
        self.assertEqual(str(self.lista), "")
        self.assertEqual(self.lista.contar_elementos(), 0)


class TestBuscaListaEncadeadaEstendida(unittest.TestCase):
    def setUp(self):
        self.lista = ListaEncadeadaEstendida()

    def test_buscar_na_posição(self):
        valores = [3, 7, 9, 11, 18, 20, 21, 25, 27]
        for v in valores:
            self.lista.inserir(v)
        self.assertEqual(self.lista.buscar_na_posição(0), 3)
        self.assertEqual(self.lista.buscar_na_posição(3), 11)
        self.assertEqual(self.lista.buscar_na_posição(4), 18)
        self.assertEqual(self.lista.buscar_na_posição(8), 27)

    def test_posição_invalida_negativa(self):
        valores = [3, 7, 9, 11, 18, 20, 21, 25, 27]
        for v in valores:
            self.lista.inserir(v)
        with self.assertRaises(IndexError):
            self.lista.buscar_na_posição(-1)

    def test_posição_invalida_maior(self):
        valores = [3, 7, 9, 11, 18, 20, 21, 25, 27]
        for v in valores:
            self.lista.inserir(v)
        with self.assertRaises(IndexError):
            self.lista.buscar_na_posição(9)


class TestContagemListaEncadeadaEstendida(unittest.TestCase):
    def setUp(self):
        self.lista = ListaEncadeadaEstendida()

    def test_contar_elementos(self):
        elementos = [i for i in range(15)]
        for v in elementos:
            self.lista.inserir(v)
        self.assertEqual(self.lista.contar_elementos(), 15)
        self.lista.remover(5)
        self.lista.remover(10)
        self.assertEqual(self.lista.contar_elementos(), 13)

    def test_contar_elementos_lista_vazia(self):
        self.assertEqual(self.lista.contar_elementos(), 0)
        self.lista.inserir(5)
        self.lista.remover(5)
        self.assertEqual(self.lista.contar_elementos(), 0)



class TestIntegração(unittest.TestCase):
    """Testes de integração entre as classes"""
    
    def test_cenario_exemplo_do_enunciado(self):
        """Testa o cenário específico do exemplo dado"""
        lista = ListaEncadeadaEstendida()
        
        valores_iniciais = [1, 3, 4, 7, 12, 13, 17, 20, 22, 26]

        for valor in valores_iniciais:
            lista.inserir(valor)
        
        lista.inserir(25)
        
        self.assertIsNotNone(lista.primeiro)
        
        no_atual = lista.primeiro
        valores_encontrados = []

        while no_atual is not None:
            for i in range(no_atual.contador):
                valores_encontrados.append(no_atual.array[i])

            no_atual = no_atual.prox
        
        self.assertEqual(valores_encontrados, sorted(valores_encontrados))
        self.assertIn(25, valores_encontrados)


if __name__ == '__main__':
    unittest.main(verbosity=2)
