"""
Estrutura de Dados II — Grafos, BFS e DFS
Desafio individual: conectividade de uma rede simulada de conexões entre cidades.

Pergunta de pesquisa:
    "Se uma ou mais conexões da rede simulada ficarem indisponíveis, ainda existe
    caminho entre a origem e o destino? Quantas conexões a mais esse caminho exige,
    e como BFS e DFS se comportam diante do bloqueio?"

AVISO: simulação computacional didática. Os vértices, arestas e bloqueios são
fictícios e NÃO representam rotas aéreas reais nem servem para orientar voos.

Uso no terminal:
    python solucao_grafos.py                -> menu (experimentos, testes, busca)
    python solucao_grafos.py --experimentos -> executa os experimentos A, B, C e D
    python solucao_grafos.py --testes       -> executa os testes automáticos

Uso no Google Colab:
    cole o arquivo inteiro em uma célula e execute (Shift+Enter): o menu aparece
    e as respostas são digitadas na caixa de entrada abaixo da célula.
"""

import sys
import unicodedata
from collections import deque
from itertools import permutations

# ---------------------------------------------------------------------------
# 1. Modelagem: grafo NÃO dirigido, NÃO ponderado
#    Vértices = aeroportos identificados pelas siglas IATA
#    Arestas  = ligações permitidas no modelo (valem nos dois sentidos)
# ---------------------------------------------------------------------------
AEROPORTOS = {
    "BSB": "Brasília (DF)",
    "GYN": "Goiânia (GO)",
    "BHZ": "Belo Horizonte (MG)",
    "CGB": "Cuiabá (MT)",
    "CGR": "Campo Grande (MS)",
    "GRU": "São Paulo/Guarulhos (SP)",
    "GIG": "Rio de Janeiro/Galeão (RJ)",
    "LDB": "Londrina (PR)",
    "CWB": "Curitiba (PR)",
    "FLN": "Florianópolis (SC)",
}

CONEXOES = [
    ("BSB", "GYN"),   # eixo Centro-Oeste
    ("BSB", "BHZ"),   # eixo Sudeste
    ("BSB", "CGB"),   # eixo Oeste
    ("GYN", "GRU"),
    ("GYN", "CGR"),
    ("BHZ", "GIG"),
    ("BHZ", "GRU"),
    ("GRU", "GIG"),
    ("GRU", "CWB"),
    ("GRU", "LDB"),
    ("CGB", "CGR"),
    ("CGR", "LDB"),   # rota alternativa pelo interior
    ("LDB", "CWB"),
    ("CWB", "FLN"),   # única ligação de FLN (aresta-ponte)
]


def construir_grafo(conexoes):
    """Cria a lista de adjacência (dict -> lista). Cada aresta entra nos dois extremos."""
    grafo = {}
    for a, b in conexoes:
        grafo.setdefault(a, [])
        grafo.setdefault(b, [])
        if b not in grafo[a]:
            grafo[a].append(b)
        if a not in grafo[b]:
            grafo[b].append(a)
    return grafo


GRAFO = construir_grafo(CONEXOES)


# ---------------------------------------------------------------------------
# 2. Algoritmos de busca
# ---------------------------------------------------------------------------
def bfs(rede, origem, destino):
    """Busca em largura com FILA (FIFO).
    Retorna (caminho, ordem_de_visita). caminho = None se não houver caminho.
    Em grafo não ponderado, o caminho tem o MENOR número de arestas."""
    fila = deque([(origem, [origem])])
    visitados = {origem}
    ordem = []
    while fila:
        atual, caminho = fila.popleft()      # retira o PRIMEIRO inserido
        ordem.append(atual)
        if atual == destino:
            return caminho, ordem
        for vizinho in rede.get(atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)       # marca ao enfileirar: evita duplicatas
                fila.append((vizinho, caminho + [vizinho]))
    return None, ordem


def dfs(rede, origem, destino):
    """Busca em profundidade com PILHA (LIFO).
    Retorna (caminho, ordem_de_visita). Encontra UM caminho, se existir,
    mas não garante o menor número de arestas."""
    pilha = [(origem, [origem])]
    visitados = set()
    ordem = []
    while pilha:
        atual, caminho = pilha.pop()         # retira o ÚLTIMO inserido
        if atual in visitados:
            continue
        visitados.add(atual)
        ordem.append(atual)
        if atual == destino:
            return caminho, ordem
        # reversed: o primeiro vizinho da lista é o primeiro a ser explorado
        for vizinho in reversed(rede.get(atual, [])):
            if vizinho not in visitados:
                pilha.append((vizinho, caminho + [vizinho]))
    return None, ordem


# ---------------------------------------------------------------------------
# 3. Contingência: bloqueio de arestas SEM alterar a rede original
# ---------------------------------------------------------------------------
def bloquear_conexoes(rede, bloqueios):
    """Devolve uma CÓPIA da rede sem as arestas indicadas (nos dois sentidos).
    Lança ValueError se alguma aresta não existir."""
    copia = {no: vizinhos.copy() for no, vizinhos in rede.items()}
    for a, b in bloqueios:
        if b not in copia.get(a, []):
            raise ValueError(f"A conexão {a} – {b} não existe na rede.")
        copia[a].remove(b)
        copia[b].remove(a)
    return copia


# ---------------------------------------------------------------------------
# 4. Utilitários
# ---------------------------------------------------------------------------
def numero_arestas(caminho):
    return len(caminho) - 1 if caminho else None


def _normalizar(texto):
    """Remove acentos, espaços extras e caixa: 'Goiânia' -> 'goiania'."""
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return " ".join(sem_acento.lower().split())


def resolver_nome(rede, texto):
    """Converte o texto digitado na sigla do vértice, ou None se inexistente.
    Aceita a sigla ('gru') ou o nome da cidade sem acento ('sao paulo')."""
    alvo = _normalizar(texto)
    for sigla in rede:
        cidade = AEROPORTOS.get(sigla, sigla).split(" (")[0]     # 'São Paulo/Guarulhos'
        opcoes = {_normalizar(sigla), _normalizar(cidade)}
        opcoes.update(_normalizar(parte) for parte in cidade.split("/"))
        if alvo in opcoes:
            return sigla
    return None


def formatar(caminho):
    if caminho is None:
        return "nenhum caminho encontrado (destino inalcançável no modelo)"
    return f"{' → '.join(caminho)}  ({numero_arestas(caminho)} arestas)"


def comparar(rede, origem, destino, titulo):
    caminho_bfs, ordem_bfs = bfs(rede, origem, destino)
    caminho_dfs, ordem_dfs = dfs(rede, origem, destino)
    print(f"\n--- {titulo} ---")
    print(f"Origem: {origem} | Destino: {destino}")
    print(f"BFS: {formatar(caminho_bfs)}")
    print(f"     ordem de visita: {', '.join(ordem_bfs)}")
    print(f"DFS: {formatar(caminho_dfs)}")
    print(f"     ordem de visita: {', '.join(ordem_dfs)}")
    return caminho_bfs, caminho_dfs


def imprimir_rede(rede):
    n_arestas = sum(len(v) for v in rede.values()) // 2
    print(f"\nRede simulada: {len(rede)} vértices, {n_arestas} arestas")
    for sigla, vizinhos in rede.items():
        nome = AEROPORTOS.get(sigla, "")
        print(f"  {sigla} {nome:<27} -> {', '.join(vizinhos) if vizinhos else '(isolado)'}")


# ---------------------------------------------------------------------------
# 5. Experimentos A, B, C e D (seção 7 do material)
# ---------------------------------------------------------------------------
def executar_experimentos():
    origem, destino = "BSB", "CWB"
    imprimir_rede(GRAFO)

    # A — rede completa
    comparar(GRAFO, origem, destino, "Experimento A: rede completa")

    # B — bloqueio GYN–GRU
    rede_b = bloquear_conexoes(GRAFO, [("GYN", "GRU")])
    comparar(rede_b, origem, destino, "Experimento B: bloqueio GYN–GRU")

    # C — segunda conexão bloqueada (ainda há caminho?)
    rede_c1 = bloquear_conexoes(GRAFO, [("GYN", "GRU"), ("GRU", "CWB")])
    comparar(rede_c1, origem, destino,
             "Experimento C1: bloqueios GYN–GRU + GRU–CWB")

    # C — corte que desconecta o destino
    rede_c2 = bloquear_conexoes(GRAFO, [("GRU", "CWB"), ("LDB", "CWB")])
    comparar(rede_c2, origem, "FLN",
             "Experimento C2: bloqueios GRU–CWB + LDB–CWB")

    # D — mesma rede, ordem de vizinhos diferente
    rede_d = {no: v.copy() for no, v in GRAFO.items()}
    rede_d["BSB"] = ["CGB", "BHZ", "GYN"]
    comparar(rede_d, origem, destino,
             "Experimento D: ordem de vizinhos de BSB invertida")

    print("\nRede original preservada após os bloqueios:",
          GRAFO == construir_grafo(CONEXOES))


# ---------------------------------------------------------------------------
# 6. Testes automáticos
# ---------------------------------------------------------------------------
def _todos_caminhos_simples(rede, origem, destino):
    """Força bruta (só para validar BFS): menor nº de arestas entre todos os caminhos."""
    melhor = None
    intermediarios = [v for v in rede if v not in (origem, destino)]
    for k in range(len(intermediarios) + 1):
        for meio in permutations(intermediarios, k):
            caminho = [origem, *meio, destino]
            if all(b in rede[a] for a, b in zip(caminho, caminho[1:])):
                if melhor is None or len(caminho) < len(melhor):
                    melhor = caminho
        if melhor:
            return numero_arestas(melhor)
    return None


def _caminho_valido(rede, caminho, origem, destino):
    return (caminho[0] == origem and caminho[-1] == destino
            and len(set(caminho)) == len(caminho)
            and all(b in rede[a] for a, b in zip(caminho, caminho[1:])))


def executar_testes():
    resultados = []

    def teste(nome, condicao):
        resultados.append(condicao)
        print(f"[{'OK ' if condicao else 'FALHOU'}] {nome}")

    print("\n=== Testes automáticos ===")
    # Modelagem
    teste("Rede tem pelo menos 7 vértices", len(GRAFO) >= 7)
    teste("Grafo é simétrico (não dirigido)",
          all(a in GRAFO[b] for a in GRAFO for b in GRAFO[a]))

    # BFS ótimo e DFS válido em todos os pares
    pares = [(o, d) for o in GRAFO for d in GRAFO if o != d]
    bfs_otimo = all(numero_arestas(bfs(GRAFO, o, d)[0]) == _todos_caminhos_simples(GRAFO, o, d)
                    for o, d in pares)
    teste(f"BFS retorna o menor nº de arestas nos {len(pares)} pares", bfs_otimo)
    dfs_valido = all(_caminho_valido(GRAFO, dfs(GRAFO, o, d)[0], o, d) for o, d in pares)
    teste(f"DFS retorna caminho válido nos {len(pares)} pares", dfs_valido)

    # Origem == destino
    teste("Origem igual ao destino → caminho de 0 arestas",
          bfs(GRAFO, "BSB", "BSB")[0] == ["BSB"]
          and dfs(GRAFO, "BSB", "BSB")[0] == ["BSB"])

    # Bloqueio não altera a original
    copia_antes = {k: v.copy() for k, v in GRAFO.items()}
    rede_b = bloquear_conexoes(GRAFO, [("GYN", "GRU")])
    teste("Bloqueio não altera a rede original", GRAFO == copia_antes)
    teste("Bloqueio remove a aresta nos dois sentidos",
          "GRU" not in rede_b["GYN"] and "GYN" not in rede_b["GRU"])
    teste("Após bloqueio ainda há caminho BSB→CWB",
          bfs(rede_b, "BSB", "CWB")[0] is not None)

    # Caso sem caminho
    rede_c2 = bloquear_conexoes(GRAFO, [("GRU", "CWB"), ("LDB", "CWB")])
    teste("Corte de CWB → BFS e DFS retornam None para FLN",
          bfs(rede_c2, "BSB", "FLN")[0] is None
          and dfs(rede_c2, "BSB", "FLN")[0] is None)

    # Bloqueio inválido
    try:
        bloquear_conexoes(GRAFO, [("BSB", "FLN")])
        teste("Bloqueio de aresta inexistente gera erro", False)
    except ValueError:
        teste("Bloqueio de aresta inexistente gera erro", True)

    # Validação de nomes
    teste("Sigla em minúsculas é reconhecida ('gru')", resolver_nome(GRAFO, "gru") == "GRU")
    teste("Nome da cidade sem acento é reconhecido ('sao paulo')",
          resolver_nome(GRAFO, "sao paulo") == "GRU")
    teste("Sigla inexistente é rejeitada ('MAO')", resolver_nome(GRAFO, "MAO") is None)

    # DFS depende da ordem dos vizinhos
    rede_d = {no: v.copy() for no, v in GRAFO.items()}
    rede_d["BSB"] = ["CGB", "BHZ", "GYN"]
    teste("Mudar a ordem dos vizinhos muda o DFS, mas não o tamanho do BFS",
          dfs(rede_d, "BSB", "CWB")[0] != dfs(GRAFO, "BSB", "CWB")[0]
          and numero_arestas(bfs(rede_d, "BSB", "CWB")[0])
          == numero_arestas(bfs(GRAFO, "BSB", "CWB")[0]))

    print(f"\n{sum(resultados)}/{len(resultados)} testes aprovados.")
    return all(resultados)


# ---------------------------------------------------------------------------
# 7. Modo interativo
# ---------------------------------------------------------------------------
def pedir_vertice(rede, rotulo):
    while True:
        texto = input(f"{rotulo}: ").strip()
        nome = resolver_nome(rede, texto)
        if nome:
            return nome
        print(f"  '{texto}' não existe na rede. Siglas válidas: {', '.join(rede)}")


def pedir_bloqueios(rede):
    print("\nInforme conexões a bloquear no formato 'SIGLA - SIGLA' (ex.: GYN - GRU).")
    print("Deixe em branco para encerrar.")
    bloqueios = []
    while True:
        texto = input("Bloquear: ").strip()
        if not texto:
            return bloqueios
        partes = [p.strip() for p in texto.replace("–", "-").split("-")]
        if len(partes) != 2:
            print("  Formato inválido. Exemplo: GYN - GRU")
            continue
        a, b = resolver_nome(rede, partes[0]), resolver_nome(rede, partes[1])
        if not a or not b:
            print("  Cidade inexistente na rede.")
        elif b not in rede[a]:
            print(f"  A conexão {a} – {b} não existe na rede.")
        elif (a, b) in bloqueios or (b, a) in bloqueios:
            print("  Conexão já bloqueada.")
        else:
            bloqueios.append((a, b))
            print(f"  Bloqueada: {a} – {b}")


def modo_interativo():
    print("Simulação didática de conectividade — NÃO usar para rotas reais.")
    imprimir_rede(GRAFO)
    print()
    origem = pedir_vertice(GRAFO, "Origem")
    destino = pedir_vertice(GRAFO, "Destino")
    antes = comparar(GRAFO, origem, destino, "Antes do bloqueio")
    bloqueios = pedir_bloqueios(GRAFO)
    if bloqueios:
        rede = bloquear_conexoes(GRAFO, bloqueios)
        descricao = ", ".join(f"{a}–{b}" for a, b in bloqueios)
        depois = comparar(rede, origem, destino, f"Depois do bloqueio ({descricao})")
        if antes[0] and depois[0]:
            diff = numero_arestas(depois[0]) - numero_arestas(antes[0])
            print(f"\nImpacto no menor caminho (BFS): {diff:+d} aresta(s).")
        elif antes[0] and not depois[0]:
            print("\nImpacto: o bloqueio DESCONECTOU origem e destino.")


def menu():
    """Menu principal — funciona no terminal e no Google Colab."""
    while True:
        print("\n========== GRAFOS: BFS e DFS ==========")
        print("1 - Executar experimentos A, B, C e D")
        print("2 - Executar testes automáticos")
        print("3 - Buscar caminho (origem, destino e bloqueios)")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            executar_experimentos()
        elif opcao == "2":
            executar_testes()
        elif opcao == "3":
            modo_interativo()
        elif opcao == "0":
            print("Encerrado.")
            return
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    # No Colab/Jupyter, sys.argv traz argumentos do kernel (ex.: '-f'),
    # por isso só as opções abaixo são tratadas; o resto abre o menu.
    if "--testes" in sys.argv:
        sys.exit(0 if executar_testes() else 1)
    elif "--experimentos" in sys.argv:
        executar_experimentos()
    else:
        try:
            menu()
        except (KeyboardInterrupt, EOFError):
            print("\nEncerrado.")
