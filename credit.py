import pandas as pd
import ast

# Carregar o arquivo CSV
df = pd.read_csv('credits.csv')

# Nome da pessoa que você quer buscar
nome_buscado = 'Malcolm Hutton'

# Percorre as linhas do CSV
for index, row in df.iterrows():
    try:
        cast_list = ast.literal_eval(row['cast'])  # Converte string em lista de dicionários
        for ator in cast_list:
            if ator['name'].lower() == nome_buscado.lower():
                print(f"\n🎬 Filme ID: {row['id']}")
                print(f"🎭 Nome: {ator['name']}")
                print(f"🗣️ Personagem: {ator['character']}")
                print(f"🆔 ID: {ator['id']}")
                print(f"🔢 Ordem: {ator['order']}")
                print(f"🖼️ Foto: {ator['profile_path']}")
    except:
        continue
