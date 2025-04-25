**Relatório de Implementação da Lista Encadeada em Python**

### Classe Elemento

A classe `Elemento` representa cada "nó" da lista encadeada. Cada elemento guarda dois dados:

- `valor`: o dado em si.
- `prox`: uma referência (ponteiro) para o próximo elemento da lista.

```python
class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
```

---

### Classe ListaEncadeada

Essa é a classe principal. Ela é responsável por gerenciar a lista como um todo.

#### Atributos privados:

- `_primeiro`: aponta para o primeiro elemento.
- `_ultimo`: aponta para o último elemento.
- `_cursor`: é usado como apoio para buscas e inserções.

#### Métodos principais:

##### Acesso e Busca

- `busca(referencia)`: Percorre a lista procurando um valor igual à referência e posiciona o cursor ali.

- `busca_anterior(referencia)`: Percorre a lista buscando o elemento que tem o valor da referencia e posiciona o cursor no elemento anterior a ele.

- `acessa_primeiro()`: Coloca o cursor no primeiro elemento.

- `acessa_ultimo()`: Coloca o cursor no último elemento.

- `acessa_posicao(posição)`: Percorre a lista e posiciona o cursor na posição informada.

##### Inserção

- `inserir_como_primeiro(valor)`: Cria um novo elemento e o coloca no início da lista, ou seja, define que o novo_elemento.prox será o atual primeiro e redefine o self.\_primeiro para ser o novo_elemento. Se a lista estiver vazia, ele será o primeiro e último ao mesmo tempo.

- `inserir_como_ultimo(valor)`: Insere o novo elemento no final da lista e modifica o self.\_ultimo para apontar para o novo elemento. Se a lista estiver vazia, o elemento inserido também será o primeiro.

- `inserir_na_posicao(posição, valor)`: Insere em uma posição específica, ou seja, busca a posição anterior a desejada e adiciona o novo elemento após ela. Se for posição 0, chama o inserir_como_primeiro().

- `inserir_antes_de(referencia, valor)`: Procura o elemento anterior a referencia e insere após ele novo elemento. Se for o primeiro, chama o inserir_como_primeiro().

- `inserir_depois_de(referencia, valor)`: Parecido com o anterior, mas busca o elemento de referencia e insere depois dele.

##### Remoção

- `remover_primeiro()`: Remove o primeiro da lista (move o ponteiro para o próximo).

- `remover_ultimo()`: Busca o penúltimo elemento e faz com que ele passe a ser o novo último.

- `remover_da_posicao(posição)`: Remove um elemento de uma posição específica.

- `remover(valor)`: Remove um elemento com valor igual ao passado.

##### Impressão

- `imprimir()`: Mostra todos os elementos da lista em formato de lista Python.

---

### Ilustrações Simples (Textuais)

**Lista Encadeada Após inserções:**

```
[33] -> [10] -> [12] -> [15] -> [18] -> [20] -> [65]
```

**Remover o primeiro (33):**

```
[10] -> [12] -> [15] -> [18] -> [20] -> [65]
```

**Remover o último (65):**

```
[10] -> [12] -> [15] -> [18] -> [20]
```

**Remover da posição 1 (12):**

```
[10] -> [15] -> [18] -> [20]
```

**Remover elemento 18:**

```
[10] -> [15] -> [20]
```

---

### Considerações Finais

A implementação foi feita com foco em didática e organização. O uso de um cursor interno permitiu reaproveitar código em várias funções, o que deixou a lógica mais limpa. As mensagens de erro também ajudam no uso correto da lista.

Essa abordagem é ótima para aprender o funcionamento interno das listas encadeadas, e pode ser base para outras estruturas mais complexas, como listas duplamente encadeadas ou filas/filas de prioridade.