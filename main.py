import json
import os

ARQUIVO_TAREFAS = "tarefas.json"

# ----------------------------
# Funções auxiliares
# ----------------------------

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

# ----------------------------
# Funções principais
# ----------------------------

def criar_tarefa():
    titulo = input("Título da tarefa: ")
    responsavel = input("Responsável: ")
    status = "A Fazer"

    nova_tarefa = {
        "titulo": titulo,
        "responsavel": responsavel,
        "status": status
    }

    tarefas = carregar_tarefas()
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso!\n")

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return

    print("\n📋 Lista de Tarefas:")
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['titulo']} - {t['responsavel']} ({t['status']})")
    print()

def atualizar_status():
    listar_tarefas()
    tarefas = carregar_tarefas()
    if not tarefas:
        return

    indice = int(input("Número da tarefa para atualizar: ")) - 1
    if 0 <= indice < len(tarefas):
        print("\nEscolha o novo status:")
        print("1 - A Fazer")
        print("2 - Em Progresso")
        print("3 - Concluído")

        opcao = input("Opção: ")
        if opcao == "1":
            tarefas[indice]["status"] = "A Fazer"
        elif opcao == "2":
            tarefas[indice]["status"] = "Em Progresso"
        elif opcao == "3":
            tarefas[indice]["status"] = "Concluído"
        else:
            print("Opção inválida.")
            return

        salvar_tarefas(tarefas)
        print("✅ Status atualizado com sucesso!\n")
    else:
        print("Número inválido.\n")

def excluir_tarefa():
    listar_tarefas()
    tarefas = carregar_tarefas()
    if not tarefas:
        return

    indice = int(input("Número da tarefa para excluir: ")) - 1
    if 0 <= indice < len(tarefas):
        removida = tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print(f"🗑️ Tarefa '{removida['titulo']}' removida com sucesso!\n")
    else:
        print("Número inválido.\n")

# ----------------------------
# Menu principal
# ----------------------------

def menu():
    while True:
        print("===== AgileLog =====")
        print("1. Criar nova tarefa")
        print("2. Listar tarefas")
        print("3. Atualizar status")
        print("4. Excluir tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            atualizar_status()
        elif opcao == "4":
            excluir_tarefa()
        elif opcao == "5":
            print("Encerrando o AgileLog. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# ----------------------------
# Execução
# ----------------------------

if __name__ == "__main__":
    menu()
