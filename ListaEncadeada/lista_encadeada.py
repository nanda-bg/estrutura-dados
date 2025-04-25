class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        """
        Cria uma nova lista encadeada vazia.
        Inicializa os ponteiros internos para o primeiro, último e cursor como None.
        """

        self._primeiro = None
        self._ultimo = None
        self._cursor = None

    def busca(self, referencia):
        """
        Busca pelo elemento que possui o valor igual à referência.
        Se encontrado, posiciona o cursor nesse elemento.
        Se não encontrar, o cursor será None.
        """

        atual = self._primeiro

        while atual != None and atual.valor != referencia:
            atual = atual.prox

        self._cursor = atual
    
    def busca_anterior(self, referencia):
        """
        Busca pelo elemento anterior ao que possui o valor igual à referência.
        Posiciona o cursor nesse elemento.
        Se não encontrar, o cursor será None.
        """

        atual = self._primeiro
        anterior = None

        while atual != None and atual.valor != referencia:
            anterior = atual
            atual = atual.prox

        self._cursor = anterior
    
    def acessa_primeiro(self):
        """
        Posiciona o cursor no primeiro elemento da lista.
        """
        self._cursor = self._primeiro
    
    def acessa_ultimo(self):
        """
        Posiciona o cursor no último elemento da lista.
        """
        self._cursor = self._ultimo
    
    def acessa_posicao(self, posição):
        """
        Posiciona o cursor no elemento da posição indicada (começando do zero).
        Se a posição não existir, o cursor será None.
        """

        atual = self._primeiro
        contador = 0

        while atual != None and contador < posição:
            atual = atual.prox
            contador += 1

        self._cursor = atual
    
    def inserir_como_primeiro(self, valor):
        """
        Insere um novo elemento com o valor fornecido no início da lista.
        Se a lista estiver vazia, o novo elemento será também o último.
        """

        novo_elemento = Elemento(valor)

        if self._primeiro is None:
            self._primeiro = novo_elemento
            self._ultimo = novo_elemento

        else:
            novo_elemento.prox = self._primeiro
            self._primeiro = novo_elemento

    def inserir_como_ultimo(self, valor):
        """
        Insere um novo elemento com o valor fornecido no final da lista.
        Se a lista estiver vazia, o novo elemento será também o primeiro.
        """

        novo_elemento = Elemento(valor)

        if self._primeiro is None:
            self._primeiro = novo_elemento
            self._ultimo = novo_elemento

            return

        self._ultimo.prox = novo_elemento
        self._ultimo = novo_elemento

    def inserir_na_posicao(self, posição, valor):
        """
        Insere um novo elemento com o valor fornecido na posição indicada.
        Se a posição for 0, insere como primeiro.
        Se a posição não existir na lista, não insere.
        """

        if posição == 0:
            self.inserir_como_primeiro(valor)
            return
        
        self.acessa_posicao(posição - 1)

        if self._cursor is None:
            print("Não foi possível inserir o elemento na posição desejada.")
            return

        self.inserir_depois_de(self._cursor.valor, valor)

    def inserir_antes_de(self, referencia, valor):
        """
        Insere um novo elemento com o valor fornecido antes do elemento de referência.
        Se a referência não existir, não insere.
        """

        self.busca(referencia)

        if self._cursor is None:
            print("O elemento de referencia não foi encontrado.")
            return

        if self._cursor == self._primeiro:
            self.inserir_como_primeiro(valor)
            return

        self.busca_anterior(referencia)
        self.inserir_depois_de(self._cursor.valor, valor)

    def inserir_depois_de(self, referencia, valor):
        """
        Insere um novo elemento com o valor fornecido após o elemento de referência.
        Se a referência não existir, não insere.
        """

        novo_elemento = Elemento(valor)

        self.busca(referencia)

        if self._cursor is None:
            print("O elemento de referencia não foi encontrado.")
            return
        
        if self._cursor == self._ultimo:
            self.inserir_como_ultimo(valor)
            return

        self._cursor.prox, novo_elemento.prox = novo_elemento, self._cursor.prox

    def remover_primeiro(self):
        """
        Remove o primeiro elemento da lista.
        """

        if self._primeiro is None:
            print("A lista está vazia.")
            return

        self._primeiro = self._primeiro.prox

    def remover_ultimo(self):
        """
        Remove o último elemento da lista.
        Se a lista estiver vazia, exibe uma mensagem de erro.
        """

        if self._primeiro is None:
            print("A lista está vazia.")
            return

        self.busca_anterior(self._ultimo.valor)

        self._cursor.prox = None

        self._ultimo = self._cursor

    def remover_da_posicao(self, posição):
        """
        Remove o elemento da posição indicada (começando do zero).
        """

        if self._primeiro is None:
            print("A lista está vazia.")
            return

        self.acessa_posicao(posição)

        if self._cursor is None:
            print("A posição não existe.")
            return

        if self._cursor == self._primeiro:
            self.remover_primeiro()
            return

        if self._cursor == self._ultimo:
            self.remover_ultimo()
            return
        
        self.acessa_posicao(posição - 1)

        self._cursor.prox = self._cursor.prox.prox

    def remover(self, valor):
        """
        Remove o elemento que possui o valor especificado.
        Se o elemento não existir, exibe uma mensagem de erro.
        """

        if self._primeiro is None:
            print("A lista está vazia.")
            return

        self.busca(valor)

        if self._cursor is None:
            print("O elemento não foi encontrado.")
            return

        if self._cursor == self._primeiro:
            self.remover_primeiro()
            return

        if self._cursor == self._ultimo:
            self.remover_ultimo()
            return
        
        self.busca_anterior(valor)

        self._cursor.prox = self._cursor.prox.prox    
    
    def imprimir(self):
        """
        Imprime todos os elementos da lista em formato de lista Python.
        """

        print(self.get_lista())

    def get_lista(self):
        """
        Retorna uma lista Python com todos os elementos da lista encadeada.
        """

        elementos = []

        atual = self._primeiro

        while atual:
            elementos.append(atual.valor)
            atual = atual.prox

        return elementos



def main():
    lista = ListaEncadeada()

    # Inserir como primeiro
    lista.inserir_como_primeiro(10)
    lista.imprimir()

    # Inserir como último
    lista.inserir_como_ultimo(20)
    lista.imprimir()

    # Inserir na posição 1 (intermediária)
    lista.inserir_na_posicao(1, 15)
    lista.imprimir()

    # Inserir na posição 0 (primeira)
    lista.inserir_na_posicao(0, 33)
    lista.imprimir()

    # Inserir na posição 4 (última)
    lista.inserir_na_posicao(4, 65)
    lista.imprimir()

    # Inserir antes do elemento 20
    lista.inserir_antes_de(20, 18)
    lista.imprimir()

    # Inserir depois do elemento 10
    lista.inserir_depois_de(10, 12)
    lista.imprimir()

    # Remover primeiro
    lista.remover_primeiro()
    lista.imprimir()

    # Remover último
    lista.remover_ultimo()
    lista.imprimir()

    # Remover da posição 1
    lista.remover_da_posicao(1)
    lista.imprimir()

    # Remover elemento 12
    lista.remover(18)
    lista.imprimir()
