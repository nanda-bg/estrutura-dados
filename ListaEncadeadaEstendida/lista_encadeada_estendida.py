class Nó:
    def __init__(self):
        """
        Inicializa um nó com um array de 8 elementos,
        um ponteiro para o próximo nó None
        e um contador de elementos 0
        """
        self.prox = None
        self.array = [None for _ in range(8)]
        self.contador = 0

    def está_cheio(self):
        """
        Verifica se o nó está cheio

        Retorna True se o nó contiver 8 elementos, caso contrário, retorna False
        """
        return self.contador == 8
    
    def inserir_ordenado(self, valor):
        """
        Insere o valor no array mantendo ordem crescente

        Se o valor for ser inserido no meio, desloca os elementos maiores para a direita
        """
        pos = 0
        while pos < self.contador and self.array[pos] is not None and self.array[pos] < valor:
            pos += 1

        for i in range(self.contador, pos, -1):
            self.array[i] = self.array[i-1]

        self.array[pos] = valor
        self.contador += 1

        return True
    
    def remover(self, valor):
        """
        Remove o valor do array, se existir

        Se o valor for ser removido do meio, desloca os elementos restantes para a esquerda
        """
        for i in range(self.contador):
            if self.array[i] == valor:
                for j in range(i, self.contador - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.contador - 1] = None
                self.contador -= 1
                return True
            
        return False
    
    def __str__(self):
        """
        Retorna uma representação do nó como uma string 
        no formato `[valor1, valor2, ..., valorN]`
        """
        return str([v for v in self.array])

class ListaEncadeadaEstendida:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.atual = None

    def inserir(self, valor):
        """
        Inicializa a lista se ela estiver vazia e chama a função de inserção de elemento
        """
        if self.primeiro is None:
            self._inicializar()

        self._inserir_elemento(valor)

    def remover(self, valor):
        """
        Remove o valor da lista.
        Se o nó ficar vazio após a remoção, o nó é excluído da lista, 
        ou seja, com o nó atual sendo removido, o ponteiro do nó anterior é atualizado para apontar para o próximo nó. 
        """
        anterior = None
        self._ir_para_primeiro_nó()

        while self.atual is not None:
            if valor in self.atual.array[:self.atual.contador]:
                removido = self.atual.remover(valor)
                if removido:
                    if self.atual.contador == 0:
                        if anterior is None:
                            self.primeiro = self.atual.prox

                            if self.primeiro is None:
                                self.ultimo = None
                        else:
                            anterior.prox = self.atual.prox
                            if self.atual == self.ultimo:
                                self.ultimo = anterior
                    return True

            anterior = self.atual
            self.atual = self.atual.prox

        return False

    def contar_elementos(self):
        """
        Percorre todos os nós e soma o contador de cada nó.

        Retorna o total de elementos na lista
        """
        contador = 0

        self._ir_para_primeiro_nó()

        while self.atual is not None:
            contador += self.atual.contador
            self.atual = self.atual.prox
        
        return contador 

    def buscar_na_posição(self, pos):
        """
        Retorna o elemento na posição especificada
        """
        if pos < 0:
            raise IndexError("Posição não pode ser negativa")
        
        atual = self.primeiro
        posição_acumulada = 0

        while atual is not None:
            if pos < posição_acumulada + atual.contador:
                índice_local = pos - posição_acumulada
                return atual.array[índice_local]
            posição_acumulada += atual.contador
            atual = atual.prox

        raise IndexError("Posição fora do intervalo")


    def _inicializar(self):
        """
        Inicializa a lista encadeada estendida criando o primeiro nó e apontando o primeiro e último ponteiros para ele.
        """
        self.primeiro = Nó()
        self.ultimo = self.primeiro

    def _ir_para_primeiro_nó(self):
        """
        Posiciona o cursor no primeiro nó da lista
        """
        self.atual = self.primeiro

    def _ir_para_ultimo_nó(self):
        """
        Posiciona o cursor no último nó da lista
        """
        self.atual = self.ultimo    

    def _inserir_elemento(self, valor):
        """
        Insere um valor na lista encadeada estendida.

        Primeiro, procura o nó onde o valor deve ser inserido.
        Se o nó estiver cheio, divide o nó e insere o valor no nó correto, mantendo a ordem crescente.
        """
        self._achar_nó(valor)

        if not self.atual.está_cheio():
            self.atual.inserir_ordenado(valor)

        else:
            self._split()

            if valor <= self.atual.array[self.atual.contador-1]:
                self.atual.inserir_ordenado(valor)
            else:
                self.atual.prox.inserir_ordenado(valor)

    def _achar_nó(self, valor):
        """
        Procura o nó no qual o valor deve ser inserido e posiciona o cursor nesse nó
        """
        self._ir_para_primeiro_nó()

        while self.atual is not None:
            if self.atual.contador > 0:
                if valor <= self.atual.array[self.atual.contador - 1]:
                    break

                if self.atual.prox is not None and self.atual.prox.contador > 0:
                    if valor > self.atual.array[self.atual.contador - 1] and valor <= self.atual.prox.array[0]:
                        self.atual = self.atual.prox
                        break

            if self.atual.prox is None:
                break
            self.atual = self.atual.prox

    def _split(self):
        """
        Divide a lista em duas partes, criando um novo nó para cada parte.
        """
        novo_nó = Nó()
        for valor in self.atual.array[4:]:
            if valor is not None:
                novo_nó.inserir_ordenado(valor)
                self.atual.remover(valor)

        novo_nó.prox, self.atual.prox = self.atual.prox, novo_nó

    def __str__(self):
        """
        Retorna uma representação da lista como uma string 
        no formato `[valor1, valor2, ..., valorN] -> [valor1, valor2, ..., valorN] -> ...`
        """
        self._ir_para_primeiro_nó()
        partes = []
        while self.atual is not None:
            elementos = [str(v) if v is not None else 'X' for v in self.atual.array[:self.atual.contador]]
            partes.append('[' + ', '.join(elementos) + ']')
            self.atual = self.atual.prox
        return ' -> '.join(partes)