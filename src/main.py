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


# === Funcoes interativas (INICIO) ============================================
# DESCRICAO: Funcoes cuja responsabilidade e captar e redirocionar o fluxo do 
# programa segundo entradas do usuario.

def escolher_opcao():
    """Escolher uma opção de qualquer menu apresentado para o usuário."""
    return input("\nEscolha uma opção: ")  # Retornar o valor da entrada do usuário (nesse caso, como string).

def apresentar_menu_principal():
    """Apresentar menu inicial de interação com o usuário para criar nova partida, inserir dados, editar dados de uma partida, remover partida ou enviar dados para servidor."""
    print("\nInício do programa 'olimpiadas-tenis-de-mesa'."
              + "\n 0. Sair"
              + "\n 1. Criar nova partida e inserir dados"
              + "\n 2. Editar dados de outra partida"
              + "\n 3. Remover partida"
              + "\n 4. Enviar dados para servidor")

# === Funcoes interativas (FIM) ===============================================

# TODO: implementar funcionalidade "Criar partida" (dados locais)

# TODO: implementar funcionalidade "Inserir dados" (dados locais)

# TODO: implementar funcionalidade "Editar partida" (dados locais)

# TODO: implementar funcionalidade "Remover partida" (dados locais)

# TODO: implementar funcionalidade "Enviar dados para servidor"


def main():
    """Método main para iniciar o programa."""
    continuar = True

    while continuar:
        limpar_tela()  # Limpar a tela antes de exibir o menu_principal

        apresentar_menu_principal()
        opcao = escolher_opcao()

        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "2":
            print("Prosseguindo para editar dados de partida")
            input("Pressione Enter para continuar...")
        elif opcao == "1":
            print("Prosseguindo para criar nova partida e inserir dados")
            input("Pressione Enter para continuar")
        elif opcao == "3":
            print("Prosseguindo para remover partida")
            input("Pressione Enter para continuar...")
        elif opcao == "4":
            print("Prosseguindo para enviar dados para o servidor")
            input("Pressione Enter para continuar")
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
