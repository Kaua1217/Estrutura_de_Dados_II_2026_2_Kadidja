# 🐍 Snake AVL — Estruturas de Dados II

<p align="center">
  <strong>Jogo Educativo baseado em Lista Duplamente Ligada e Árvore AVL</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Estruturas%20de%20Dados-II-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Árvore-AVL-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Projeto-Snake-orange?style=for-the-badge">
</p>

---

# 🎮 Jogo Base

O projeto utiliza como referência o Snake, desenvolvido por Adel Katergi como parte do projeto Data Structure Arcade.

No projeto original, o Snake utiliza uma Lista Duplamente Ligada (Doubly Linked List) para representar o corpo da cobra. Cada parte do corpo pode ser representada como um nó, permitindo o uso das referências previous e next.

O projeto original foi desenvolvido com o objetivo de demonstrar, de forma prática, a aplicação de estruturas de dados em jogos.

Desenvolvedor: Adel Katergi
Projeto: Data Structure Arcade
Estrutura de dados: Doubly Linked List
Jogo: Snake
## 📌 Sobre o Projeto

O **Snake AVL** é um projeto desenvolvido para a disciplina de **Estruturas de Dados II**, do curso de **Ciência da Computação**.

O projeto parte de um jogo **Snake** baseado originalmente em uma **Lista Duplamente Ligada** e propõe um upgrade da mecânica utilizando uma **Árvore AVL** para gerenciamento e organização do ranking dos jogadores.

A proposta busca transformar conceitos teóricos de Estruturas de Dados em elementos visíveis e interativos dentro do jogo, permitindo que o jogador compreenda conceitos como:

* 🌳 Árvore AVL;
* 🔑 Nós e chaves;
* 📏 Altura da árvore;
* ⚖️ Fator de balanceamento;
* 🔄 Rotações simples;
* 🔄 Rotações duplas;
* 📊 Organização e busca de pontuações;
* 🏆 Ranking dos jogadores.

A atividade tem como proposta analisar um modelo existente, identificar suas limitações didáticas e técnicas e desenvolver uma melhoria funcional utilizando estruturas avançadas de dados.

---

# 🎮 Jogo Base

O projeto utiliza como referência o **Snake / Lista Duplamente Ligada** disponível no projeto Data Structure Arcade:

🔗 https://akatergi.github.io/DataStructureArcade/snake/snake.html

No modelo original, o corpo da cobra é representado por uma **Lista Duplamente Ligada**. Entretanto, os conceitos relacionados à estrutura permanecem praticamente invisíveis para o jogador.

O jogador controla a cobra, coleta maçãs e acumula pontos, mas não visualiza diretamente conceitos como:

* `head`;
* `tail`;
* `previous`;
* `next`;
* nós da lista;
* referências entre os elementos.

Além disso, o jogo original não utiliza uma estrutura avançada para organizar as pontuações dos jogadores.

---

# 🎯 Objetivo do Upgrade

O objetivo do projeto é **reutilizar a mecânica do Snake e adicionar uma Árvore AVL ao sistema de ranking**.

Dessa maneira, a pontuação obtida durante uma partida passa a ser utilizada para alimentar uma estrutura de dados que organiza os jogadores.

O fluxo proposto é:

```text
Jogar Snake
     ↓
Coletar maçãs
     ↓
Acumular pontos
     ↓
Finalizar partida
     ↓
Registrar pontuação
     ↓
Inserir pontuação na Árvore AVL
     ↓
Verificar balanceamento
     ↓
Executar rotação, se necessário
     ↓
Atualizar ranking
```

Esse fluxo corresponde ao **Core Loop** definido no documento da atividade.

---

# 🌳 Estrutura de Dados Utilizada

## Árvore AVL

A estrutura escolhida para o upgrade foi a **Árvore AVL**.

Uma AVL é uma árvore de busca binária que precisa permanecer balanceada após as operações de inserção e remoção.

No projeto, serão trabalhados principalmente:

* **Fator de Balanceamento**
* **Altura**
* **Rotações LL**
* **Rotações RR**
* **Rotações LR**
* **Rotações RL**

A atividade estabelece que o fator de balanceamento válido para uma árvore AVL balanceada deve estar entre:

```text
-1, 0 e +1
```

## Quando uma inserção provoca desequilíbrio, o sistema identifica o caso correspondente e realiza a rotação necessária.

# 🏆 Ranking com Árvore AVL

A principal aplicação da AVL no projeto será o **ranking de jogadores**.

Cada pontuação registrada será armazenada em um nó da árvore.

### Estrutura conceitual

```text
              500
             /   \
           300    700
          /  \    /  \
        150  400 600  900
```

Cada nó poderá representar uma pontuação registrada e o(s) jogador(es) associado(s).

### Exemplo

```text
Pontuação: 500
Jogador: Kauã
```

Outro jogador obtendo:

```text
Pontuação: 300
Jogador: João
```

resultará na inserção da nova chave na estrutura.

Com novas pontuações, a árvore poderá sofrer desequilíbrios e realizar rotações automaticamente.

---

# ⚖️ Fator de Balanceamento

O fator de balanceamento será utilizado para demonstrar o funcionamento interno da AVL.

A ideia é observar a diferença entre a altura da subárvore esquerda e da subárvore direita.

```text
FB = altura(esquerda) - altura(direita)
```

Para a árvore permanecer balanceada:

```text
FB ∈ {-1, 0, +1}
```

Quando o valor ultrapassa esse intervalo, a árvore precisa ser reorganizada por meio de uma rotação.

No jogo, esse processo será utilizado como parte da representação visual da estrutura de dados.

---

# 🔄 Rotações da AVL

O sistema deverá identificar os principais casos de desequilíbrio.

## Caso LL

Ocorre quando a inserção acontece na parte esquerda da subárvore esquerda.

```text
        30
       /
     20
    /
  10
```

Aplicação:

```text
Rotação à direita
```

Resultado:

```text
      20
     /  \
   10    30
```

---

## Caso RR

Ocorre quando a inserção acontece na parte direita da subárvore direita.

```text
10
  \
   20
     \
      30
```

Aplicação:

```text
Rotação à esquerda
```

Resultado:

```text
      20
     /  \
   10    30
```

---

## Caso LR

Ocorre quando a inserção acontece na direita da subárvore esquerda.

```text
      30
     /
   10
     \
      20
```

Aplicação:

```text
Rotação à esquerda
+
Rotação à direita
```

---

## Caso RL

Ocorre quando a inserção acontece na esquerda da subárvore direita.

```text
10
  \
   30
  /
20
```

Aplicação:

```text
Rotação à direita
+
Rotação à esquerda
```

A atividade prevê que os casos **LL, RR, LR e RL** sejam identificados pela AVL e tratados com a rotação correspondente.

---

# 🐍 Relação entre Snake e Estruturas de Dados

O projeto trabalha com duas estruturas principais.

## Lista Duplamente Ligada

É utilizada para representar o **corpo da cobra**.

Conceitualmente:

```text
HEAD
 ↓
[ Nó ] ⇄ [ Nó ] ⇄ [ Nó ] ⇄ [ Nó ]
                                      ↑
                                     TAIL
```

Cada nó possui referências para:

```text
previous ← Nó → next
```

O crescimento da cobra representa o aumento da quantidade de nós da lista.

---

## Árvore AVL

É utilizada para representar o **ranking das pontuações**.

```text
             [500]
            /     \
        [300]     [700]
        /  \       /  \
     [200][400] [600][900]
```

Dessa maneira:

```text
Snake
  │
  ├── Corpo → Lista Duplamente Ligada
  │
  └── Pontuação → Árvore AVL
                     │
                     └── Ranking
```

---

# 🎮 Gameplay

Durante a partida, o jogador deverá:

1. Controlar a cobra pelo mapa;
2. Coletar as maçãs;
3. Aumentar sua pontuação;
4. Aumentar o tamanho da cobra;
5. Finalizar a partida;
6. Registrar sua pontuação;
7. Inserir a pontuação na AVL;
8. Verificar o fator de balanceamento;
9. Executar uma rotação quando necessário;
10. Atualizar o ranking.

Esse ciclo representa a integração entre **gameplay e Estruturas de Dados II**.

---

# 🏁 Condição de Vitória

O objetivo do jogador é conseguir a **maior pontuação possível**, buscando melhorar sua posição no ranking.

```text
Maior pontuação
      ↓
Melhor posição no ranking
```

A pontuação final é inserida na Árvore AVL e passa a fazer parte da classificação dos jogadores.

---

# 💀 Condição de Derrota

O jogador perde quando:

* a cabeça da cobra colide com uma parede; ou
* a cabeça da cobra colide com o próprio corpo.

À medida que a cobra cresce, a Lista Duplamente Ligada possui mais nós, tornando seu gerenciamento e navegação progressivamente mais complexos.

É importante destacar que o balanceamento da AVL **não representa uma condição de derrota**. O sistema realiza automaticamente as rotações necessárias para manter o ranking balanceado.

---

# 🔍 Problema Identificado no Jogo Original

O jogo original possui uma importante limitação pedagógica: a estrutura de dados utilizada internamente não é apresentada de forma explícita ao jogador.

O jogador consegue jogar, mas não necessariamente consegue perceber que:

```text
Cobra
 ↓
Lista Duplamente Ligada
 ↓
Nós
 ↓
Previous / Next
```

Também não existe, no modelo original, uma estrutura destinada à organização das pontuações dos usuários em um ranking baseado em árvore.

O upgrade busca solucionar justamente essa limitação, tornando os conceitos de Estruturas de Dados mais visíveis durante a experiência.

---

# 🧠 Objetivo Educacional

Além de funcionar como jogo, o projeto possui finalidade educacional.

A proposta é permitir que o estudante observe na prática conceitos que normalmente são apresentados de maneira teórica.

### Conceitos trabalhados

| Conceito                | Aplicação no projeto        |
| ----------------------- | --------------------------- |
| Nó                      | Representa uma pontuação    |
| Chave                   | Valor da pontuação          |
| Altura                  | Quantidade de níveis da AVL |
| Fator de Balanceamento  | Identifica desequilíbrios   |
| Rotação LL              | Correção de desequilíbrio   |
| Rotação RR              | Correção de desequilíbrio   |
| Rotação LR              | Rotação dupla               |
| Rotação RL              | Rotação dupla               |
| Lista Duplamente Ligada | Estrutura do corpo da cobra |
| Árvore AVL              | Estrutura do ranking        |

O mapeamento entre os conceitos teóricos e as mecânicas do jogo é uma das partes centrais da atividade.

---

# 🖥️ Proposta de Interface

A interface do projeto pode apresentar simultaneamente o jogo e a estrutura de dados.

### Área do jogo

```text
┌──────────────────────────────────┐
│              SNAKE               │
│                                  │
│       🟩 🟩 🟩                   │
│                    🍎            │
│                                  │
│                                  │
└──────────────────────────────────┘

Pontuação: 350
```

### Área da AVL

```text
        500
       /   \
     350    700
    /  \
  200  400
```

### Informações adicionais

```text
Fator de Balanceamento: 0
Altura: 3
Última operação: Inserção
Última rotação: Rotação à direita
```

A ideia é fazer com que o jogador consiga acompanhar visualmente o que está acontecendo com a estrutura enquanto joga.

---

# 🚀 Funcionamento Geral

O funcionamento pode ser representado pelo seguinte fluxo:

```text
                 ┌───────────────┐
                 │ Iniciar Jogo  │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Controlar     │
                 │ Cobra         │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Coletar Maçã  │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Aumentar      │
                 │ Pontuação     │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Fim da Partida│
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Inserir Score │
                 │ na AVL        │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Verificar FB  │
                 └───────┬───────┘
                         ↓
                  ┌──────┴──────┐
                  │ Desequilíbrio│
                  └──────┬──────┘
                         ↓
                 ┌───────────────┐
                 │ Executar      │
                 │ Rotação       │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Atualizar     │
                 │ Ranking       │
                 └───────────────┘
```

---

# 👥 Integrantes

**Ciência da Computação — Estruturas de Dados II**

* **Edilson Filho**
* **Yan Souza**
* **Kauã Sousa**

Projeto desenvolvido em **2026.2**.

---

# 📚 Referência do Modelo Base

O projeto utiliza como referência o jogo Snake do **Data Structure Arcade**:

https://akatergi.github.io/DataStructureArcade/snake/snake.html

O modelo foi utilizado como ponto de partida para a análise e proposta de upgrade apresentada neste projeto.

---

# 🎤 Apresentação

A proposta foi estruturada para também ser apresentada em um **Pitch de aproximadamente 3 minutos**, conforme solicitado na atividade.

Durante a apresentação, os principais pontos são:

1. Apresentação do Snake original;
2. Problema identificado;
3. Estrutura de dados utilizada;
4. Proposta de upgrade;
5. Funcionamento da AVL;
6. Integração entre pontuação e ranking;
7. Demonstração das rotações;
8. Objetivo educacional do projeto.

A atividade estabelece o Pitch como etapa final de preparação e defesa do modelo desenvolvido.

---

# 📌 Status do Projeto

🚧 **Em desenvolvimento**

### Implementado / Definido

* [x] Escolha do jogo base
* [x] Análise das limitações
* [x] Escolha da Árvore AVL
* [x] Definição do ranking
* [x] Mapeamento dos conceitos de ED II
* [x] Definição do Core Loop
* [x] Definição das condições de vitória e derrota
* [ ] Implementação completa do jogo
* [ ] Implementação da AVL
* [ ] Integração do ranking
* [ ] Visualização da árvore
* [ ] Testes
* [ ] Apresentação final

---

# 📖 Conclusão

O **Snake AVL** propõe uma forma de transformar um jogo conhecido em uma ferramenta de aprendizagem de Estruturas de Dados.

A partir do Snake baseado em Lista Duplamente Ligada, o projeto adiciona uma **Árvore AVL responsável pela organização das pontuações**, permitindo relacionar diretamente conceitos como altura, fator de balanceamento e rotações com ações realizadas durante o jogo.

Dessa forma, a estrutura de dados deixa de ser apenas um componente interno do programa e passa a fazer parte da experiência visual e interativa do jogador.

> **Jogar, pontuar, inserir, balancear e visualizar.** 🐍🌳
