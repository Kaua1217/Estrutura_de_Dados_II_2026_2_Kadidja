# 3. Conheça os usuários

| Código | Usuário |
|---|---|
| A | Ana |
| B | Bruno |
| C | Carla |
| D | Diego |
| E | Elisa |
| F | Felipe |
| G | Gabriela |
| H | Heitor |
| I | Isabela |
| J | João |
| K | Karen |
| L | Lucas |
| M | Mariana |
| N | Nicolas |
| O | Olivia |
| P | Pedro |
| Q | Rafaela |
| R | Ricardo |
| S | Sofia |
| T | Thiago |
| U | Valentina |
| V | Vinícius |
| W | Yasmin |

## As amizades são:

```python
amizades = {
    "Ana": ["Bruno", "Carla", "Diego", "Felipe", "Heitor"],
    "Bruno": ["Ana", "Carla", "Elisa", "Gabriela", "João"],
    "Carla": ["Ana", "Bruno", "Diego", "Felipe", "Isabela", "Karen"],
    "Diego": ["Ana", "Carla", "Elisa", "Gabriela", "Lucas"],
    "Elisa": ["Bruno", "Diego", "Felipe", "Heitor", "Mariana"],
    "Felipe": ["Ana", "Carla", "Elisa", "Gabriela", "Isabela", "Nicolas"],
    "Gabriela": ["Bruno", "Diego", "Felipe", "Heitor", "João", "Olivia"],
    "Heitor": ["Ana", "Elisa", "Gabriela", "Isabela", "Karen", "Pedro"],
    "Isabela": ["Carla", "Felipe", "Heitor", "João", "Lucas", "Rafaela"],
    "João": ["Bruno", "Gabriela", "Isabela", "Karen", "Mariana", "Ricardo"],
    "Karen": ["Carla", "Heitor", "João", "Lucas", "Nicolas", "Sofia"],
    "Lucas": ["Diego", "Isabela", "Karen", "Mariana", "Olivia", "Thiago"],
    "Mariana": ["Elisa", "João", "Lucas", "Nicolas", "Pedro", "Valentina"],
    "Nicolas": ["Felipe", "Karen", "Mariana", "Olivia", "Rafaela", "Vinícius"],
    "Olivia": ["Gabriela", "Lucas", "Nicolas", "Pedro", "Ricardo", "Yasmin"],
    "Pedro": ["Heitor", "Mariana", "Olivia", "Rafaela", "Sofia"],
    "Rafaela": ["Isabela", "Nicolas", "Pedro", "Ricardo", "Thiago"],
    "Ricardo": ["João", "Olivia", "Rafaela", "Sofia", "Valentina"],
    "Sofia": ["Karen", "Pedro", "Ricardo", "Thiago", "Vinícius"],
    "Thiago": ["Lucas", "Rafaela", "Sofia", "Valentina", "Yasmin"],
    "Valentina": ["Mariana", "Ricardo", "Thiago", "Vinícius"],
    "Vinícius": ["Nicolas", "Sofia", "Valentina", "Yasmin"],
    "Yasmin": ["Olivia", "Thiago", "Vinícius"]
}
```

# 4. Passo a passo: desenhe o grafo

[<img width="1032" height="727" alt="image" src="https://github.com/user-attachments/assets/87825abd-d181-464b-9721-7833e6529695" />
](https://github.com/EdilsonUDF/Estrutura_de_Dados_2/blob/main/Unidade3/Grafo/grafo_rede.png)

1. Crie um vértice para cada usuário.
2. Identifique os vértices com os nomes ou códigos dos usuários.
3. Desenhe uma aresta entre cada par de amigos.
4. Como as amizades são mútuas, utilize um grafo não direcionado.

# 5. Passo a passo: calcule o grau

O grau de um vértice corresponde ao número de conexões diretas que um usuário possui.

| Usuário | Grau |
|---|---:|
| Ana | 5 |
| Bruno | 5 |
| Carla | 6 |
| Diego | 5 |
| Elisa | 5 |
| Felipe | 6 |
| Gabriela | 6 |
| Heitor | 6 |
| Isabela | 6 |
| João | 6 |
| Karen | 6 |
| Lucas | 6 |
| Mariana | 6 |
| Nicolas | 6 |
| Olivia | 6 |
| Pedro | 5 |
| Rafaela | 5 |
| Ricardo | 5 |
| Sofia | 5 |
| Thiago | 5 |
| Valentina | 4 |
| Vinícius | 4 |
| Yasmin | 3 |

### Quem tem mais conexões diretas?

Os usuários com o maior grau são:

- Carla: 6 conexões.
- Felipe: 6 conexões.
- Gabriela: 6 conexões.
- Heitor: 6 conexões.
- Isabela: 6 conexões.
- João: 6 conexões.
- Karen: 6 conexões.
- Lucas: 6 conexões.
- Mariana: 6 conexões.
- Nicolas: 6 conexões.
- Olivia: 6 conexões.

# 6. Passo a passo: calcule o número de amizades

- **Total de usuários:** 23
- **Total de amizades:** 61

Como cada amizade é representada por uma aresta não direcionada, cada conexão deve ser contada apenas uma vez.

# 7. Passo a passo: calcule a densidade

- **Densidade decimal:** 0,2411
- **Densidade percentual:** 24,11%

# 8. Passo a passo: represente o grafo em Python

Utilize o Google Colab para representar a rede social por meio de código Python.

[**Acessar o Google Colab**](https://colab.research.google.com/drive/1BsT0Tgw-_DUnZjAD7PxCHN0QxwhHlJRi?usp=sharing)

# 9. Passo a passo: encontre um caminho

Um caminho é uma sequência de vértices conectados por arestas.

**Primeiro caminho:**

Ana → Bruno → Carla → Felipe

- Número de arestas: 3.

**Você encontrou outro caminho com a mesma quantidade de arestas? Qual?**

Ana → Diego → Carla → Felipe

- Número de arestas: 3.

Os dois caminhos possuem a mesma quantidade de arestas e conectam Ana a Felipe.
