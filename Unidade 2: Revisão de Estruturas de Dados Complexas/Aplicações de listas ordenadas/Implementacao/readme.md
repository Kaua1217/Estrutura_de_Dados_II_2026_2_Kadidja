# Árvores Binárias de Busca (ABB) - Aplicação Interativa e Materiais de Aula

Este repositório contém os materiais didáticos e uma aplicação web interativa desenvolvidos para o estudo de **Árvores Binárias de Busca (ABB)**. O conteúdo faz parte da disciplina de **Estrutura de Dados II** do curso de Ciência da Computação (UDF).

O objetivo deste conjunto de arquivos é ensinar, de forma teórica e prática, as regras de ordenação, inserção e busca em árvores binárias simples, demonstrando como as decisões lógicas diminuem o custo da busca (tendendo a `O(log n)` em árvores equilibradas).

---

## 📁 Arquivos do Repositório

### 1. `Aula_Arvores_Simples_Busca_Basica_UDF_18setembro.pdf`
Slides utilizados na aula ministrada pela Prof.a Kadidja Valéria. 
* **Conteúdo:** Vocabulário essencial (raiz, folhas, nós, níveis), regras da Árvore Binária de Busca, impacto do formato da árvore no custo de busca (equilibrada vs. degenerada), implementação guiada em Python e a proposta do workshop prático.

### 2. `Mini_GDD_ABB_Interativa.pptx`
Apresentação contendo o *Mini Game Design Document* (GDD) elaborado durante o workshop da aula.
* **Conteúdo:** Documentação da mecânica da aplicação interativa, definindo o problema do usuário (localizar valores e entender o caminho), a árvore inicial sugerida (`[50, 30, 70, 20, 40, 60, 80]`), os loops de feedback visual/textual e as condições de sucesso/falha (atingir o valor ou chegar a `None`).

### 3. `abb_interativa.html`
A aplicação web interativa que tira o GDD do papel e materializa os conceitos ensinados nos slides.
* **Conteúdo:** Uma interface completa feita em HTML, CSS e JavaScript puro (sem dependências externas) que permite visualizar o funcionamento do algoritmo passo a passo.
* **Funcionalidades:**
  * **Animação de Inserção:** Mostra a comparação nó a nó até encontrar uma posição vazia.
  * **Animação de Busca:** Permite buscar um valor e exibe o caminho exato percorrido, parando no nó encontrado ou apontando para um "None" fantasma em caso de falha.
  * **Fila Personalizada:** O usuário pode inserir seus próprios números para ver como diferentes ordens de inserção moldam árvores diferentes.
  * **Código Espelhado:** Exibe o código Python equivalente na tela para facilitar a conexão entre teoria, visualização e código real.

---

## 🚀 Como usar a aplicação interativa

A aplicação não requer instalação de bibliotecas, servidores ou ambientes de desenvolvimento. 

1. Baixe o arquivo `abb_interativa.html` para o seu computador.
2. Dê um duplo clique no arquivo, ou clique com o botão direito e selecione **"Abrir com"** para abrir no seu navegador web de preferência (Google Chrome, Firefox, Edge, Safari, etc.).
3. Utilize o painel esquerdo para inserir os valores iniciais e, em seguida, teste a funcionalidade de "Buscar" acompanhando os relatórios gerados no console visual da tela.

---

## 🛠️ Tecnologias Utilizadas
* **Teoria & Estrutura:** Python (código demonstrativo) e Lógica de Estrutura de Dados.
* **Aplicação Web:** HTML5, CSS3 (com tipografia do Google Fonts) e JavaScript Vanilla (manipulação de DOM e desenho de SVG dinâmico).

---
*Material baseado no roteiro e workshop da aula de 14/18 de setembro.*
