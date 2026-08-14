# Estrutura de Dados - Pilha

Projeto desenvolvido para a atividade de **Estrutura de Dados II**, com a implementação de uma estrutura de dados do tipo **Pilha (Stack)**.

## Sobre o projeto

A pilha é uma estrutura de dados linear que segue o princípio **LIFO (Last In, First Out)**, ou seja, o último elemento inserido é o primeiro a ser removido.

Neste projeto, a pilha foi implementada utilizando uma lista do Python.

## Operações implementadas

- **Empilhar (push):** adiciona um elemento ao topo da pilha.
- **Desempilhar (pop):** remove o elemento que está no topo.
- **Consultar topo (peek):** mostra o elemento do topo sem removê-lo.
- **Verificar se está vazia:** informa se existem elementos na pilha.
- **Consultar tamanho:** informa a quantidade de elementos armazenados.

## Estrutura do projeto

```text
estrutura-dados-pilha/
├── pilha.py
└── README.md
```

## Como executar

É necessário ter o Python 3 instalado.

No terminal, execute:

```bash
python pilha.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 pilha.py
```

## Exemplo de funcionamento

```text
=== PILHA - ESTRUTURA DE DADOS ===
1. Empilhar
2. Desempilhar
3. Consultar topo
4. Ver pilha
5. Ver tamanho
0. Sair
```

Exemplo:

```text
Empilhar: 10
Empilhar: 20
Empilhar: 30

Topo -> 30 -> 20 -> 10

Desempilhar -> 30

Topo -> 20
```

## Conceito utilizado

A implementação segue o conceito **LIFO**:

```text
Entrada:
10
20
30

Topo
 ↓
30
20
10

Saída:
30
20
10
```

## Autor

**Kauã**

Projeto acadêmico desenvolvido para a disciplina de **Estrutura de Dados II**.
