import csv
import json
import os

def buscar_em_arquivo(nome_arquivo, termo_busca):
    if not os.path.isfile(nome_arquivo):
        print("❌ Arquivo não encontrado.")
        return

    extensao = os.path.splitext(nome_arquivo)[1].lower()

    if extensao == '.csv':
        ler_e_buscar_csv(nome_arquivo, termo_busca)
    elif extensao == '.txt':
        ler_e_buscar_txt(nome_arquivo, termo_busca)
    elif extensao == '.json':
        ler_e_buscar_json(nome_arquivo, termo_busca)
    else:
        print("⚠️ Tipo de arquivo não suportado.")

def ler_e_buscar_csv(nome_arquivo, termo_busca):
    termo_eh_id = termo_busca.isdigit()

    with open(nome_arquivo, newline='', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        cabecalho = next(leitor)

        if termo_eh_id:
            resultados = [linha for linha in leitor if termo_busca == linha[0]]
        else:
            resultados = [
                linha for linha in leitor
                if any(termo_busca.lower() in campo.lower() for campo in linha)
            ]

    if resultados:
        total = len(resultados)
        print(f"\n✅ {total} resultado(s) encontrado(s) para '{termo_busca}':\n")

        limite = 10
        for i in range(min(limite, total)):
            print(dict(zip(cabecalho, resultados[i])))

        if total > limite:
            ver_tudo = input(f"\n⚠️ Exibir todos os {total} resultados? (s/n): ").lower()
            if ver_tudo == 's':
                for i in range(limite, total):
                    print(dict(zip(cabecalho, resultados[i])))
    else:
        print("🔎 Nenhum resultado encontrado.")

def ler_e_buscar_txt(nome_arquivo, termo_busca):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        resultados = [linha.strip() for linha in linhas if termo_busca.lower() in linha.lower()]

    if resultados:
        print(f"\n✅ {len(resultados)} resultado(s) encontrado(s):\n")
        for linha in resultados[:10]:
            print(linha)
        if len(resultados) > 10:
            ver_tudo = input(f"\n⚠️ Exibir todos os {len(resultados)} resultados? (s/n): ").lower()
            if ver_tudo == 's':
                for linha in resultados[10:]:
                    print(linha)
    else:
        print("🔎 Nenhum resultado encontrado.")

def ler_e_buscar_json(nome_arquivo, termo_busca):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    resultados = []
    for item in dados:
        if isinstance(item, dict):
            if any(termo_busca.lower() in str(valor).lower() for valor in item.values()):
                resultados.append(item)

    if resultados:
        print(f"\n✅ {len(resultados)} resultado(s) encontrado(s):\n")
        for item in resultados[:10]:
            print(item)
        if len(resultados) > 10:
            ver_tudo = input(f"\n⚠️ Exibir todos os {len(resultados)} resultados? (s/n): ").lower()
            if ver_tudo == 's':
                for item in resultados[10:]:
                    print(item)
    else:
        print("🔎 Nenhum resultado encontrado.")

# Execução
nome_arquivo = input("📂 Digite o nome do arquivo (ex: credits.csv): ")
termo = input("🔍 Digite o nome ou ID que deseja buscar: ")
buscar_em_arquivo(nome_arquivo, termo)
