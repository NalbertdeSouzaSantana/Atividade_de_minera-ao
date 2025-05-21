def criar_no(atributo=None, classe=None):
    return {
        'atributo': atributo,
        'classe': classe,
        'filhos': {}
    }

def adicionar(no, valor, filho):
    no['filhos'][valor] = filho

def mostrar_arvore(no, prefixo=""):
    if no['classe']:
        print(f"{prefixo}=> Classe: {no['classe']}")
    else:
        print(f"{prefixo}>> Teste: {no['atributo']}")
        for valor, filho in no['filhos'].items():
            print(f"{prefixo}  [{valor}]")
            mostrar_arvore(filho, prefixo + "    ")

def construir_arvore():
    while True:
        atributo = input("Qual é o primeiro atributo (ex: Clima, Humor, Situação)? ").strip()
        if atributo != "":
            break
        print("⚠️ O atributo não pode ficar em branco.")
    raiz = criar_no(atributo=atributo)
    construir_filhos(raiz)
    return raiz

def construir_filhos(no):
    while True:
        try:
            quantos = int(input(f"Quantos valores possíveis para '{no['atributo']}'? (1 a 10): "))
            if 1 <= quantos <= 10:
                break
            else:
                print("⚠️ Digite um número entre 1 e 10.")
        except ValueError:
            print("⚠️ Por favor, digite um número válido.")

    for _ in range(quantos):
        while True:
            valor = input(f" - Valor para '{no['atributo']}': ").strip()
            if valor != "":
                break
            print("   ⚠️ Valor não pode ficar em branco. Tente novamente.")

        while True:
            tipo = input("   Isso leva a uma nova pergunta (P) ou uma decisão final (D)? ").strip().upper()
            if tipo in ("P", "D"):
                break
            print("   ⚠️ Resposta inválida. Use 'P' ou 'D'.")

        if tipo == "D":
            while True:
                classe = input("   Qual é a decisão (classe)? ").strip()
                if classe != "":
                    break
                print("   ⚠️ A classe não pode ficar em branco.")
            filho = criar_no(classe=classe)
        else:  # tipo == "P"
            while True:
                novo_atributo = input("   Qual é o novo atributo? ").strip()
                if novo_atributo != "":
                    break
                print("   ⚠️ O novo atributo não pode ficar em branco.")
            filho = criar_no(atributo=novo_atributo)
            construir_filhos(filho)

        adicionar(no, valor, filho)

# Execução
if __name__ == "__main__":
    print("Bem-vindo! Vamos construir sua Árvore de Decisão personalizada.")
    arvore = construir_arvore()
    print("\nÁrvore final construída:")
    mostrar_arvore(arvore)
