#!/usr/bin/env python3
'''main.py
Descricao: arquivo principal do sistema `pi2a-olimpiadas-tenis-de-mesa`.
'''
import os


def limpar_tela():
    """Limpar a tela do terminal."""
    # Limpar a tela do terminal segundo o tipo de sistema operacional onde é
    # executado:
    os.system('cls' if os.name == 'nt' else 'clear')  # 'nt' para Windows e 'clear' para qualquer outro (Linux, macOS, etc)


def escolher_opcao():
    """Escolher uma opção de qualquer menu apresentado para o usuário."""
    return input("\nEscolha uma opção: ")  # Retornar o valor da entrada do usuário (nesse caso, como string).

# TODO: implementar funcionalidade "Criar partida" (dados locais)

# TODO: implementar funcionalidade "Inserir dados" (dados locais)

# TODO: implementar funcionalidade "Editar partida" (dados locais)

# TODO: implementar funcionalidade "Remover partida" (dados locais)

# TODO: implementar funcionalidade "Enviar dados para servidor"


def main():
    """Método main para iniciar o programa."""
    continuar = True

    while continuar:
        limpar_tela()  # Limpar a tela antes de exibir o menu
        print("\nInício do programa 'olimpiadas-tenis-de-mesa'."
              + "\n 0. Sair"
              + "\n 1. Criar nova partida e inserir dados"
              + "\n 2. Editar dados de outra partida"
              + "\n 3. Remover partida"
              + "\n 4. Enviar dados para servidor")

        opcao = escolher_opcao()

        if opcao == "2":
            print("Prosseguindo para editar dados de partida")
            input("Pressione Enter para continuar...")
        elif opcao == "1":
            print("Prosseguindo para criar nova partida e inserir dados")
            input("Pressione Enter para continuar")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
