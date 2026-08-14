class Pilha:
    """Implementação de uma pilha usando lista."""

    def __init__(self):
        self._itens = []

    def empilhar(self, item):
        """Adiciona um elemento ao topo da pilha."""
        self._itens.append(item)

    def desempilhar(self):
        """Remove e retorna o elemento do topo."""
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")
        return self._itens.pop()

    def topo(self):
        """Retorna o elemento do topo sem removê-lo."""
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")
        return self._itens[-1]

    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self._itens) == 0

    def tamanho(self):
        """Retorna a quantidade de elementos da pilha."""
        return len(self._itens)

    def __str__(self):
        return " -> ".join(map(str, reversed(self._itens)))


def menu():
    pilha = Pilha()

    while True:
        print("\n=== PILHA - ESTRUTURA DE DADOS ===")
        print("1. Empilhar")
        print("2. Desempilhar")
        print("3. Consultar topo")
        print("4. Ver pilha")
        print("5. Ver tamanho")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            item = input("Digite o valor: ")
            pilha.empilhar(item)
            print(f"'{item}' foi empilhado.")

        elif opcao == "2":
            try:
                item = pilha.desempilhar()
                print(f"'{item}' foi removido da pilha.")
            except IndexError as erro:
                print(erro)

        elif opcao == "3":
            try:
                print(f"Topo: {pilha.topo()}")
            except IndexError as erro:
                print(erro)

        elif opcao == "4":
            if pilha.esta_vazia():
                print("A pilha está vazia.")
            else:
                print(f"Topo -> {pilha}")

        elif opcao == "5":
            print(f"Tamanho da pilha: {pilha.tamanho()}")

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
