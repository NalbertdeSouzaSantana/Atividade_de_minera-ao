import math
import pandas as pd

def entropia(data_frame, classes, atributo_classe):
    soma = 0
    qtd_total = len(data_frame[atributo_classe])
    for classe in classes:
        qtd_classe = len(data_frame[data_frame[atributo_classe] == classe])
        p_i = qtd_classe / qtd_total
        if p_i == 0:
            log = 0
        else:
            log = math.log2(p_i)
        item = p_i * log
        soma += item
    return -1 * soma

def ganho(data_frame, atributo, atributo_classe):
    values = data_frame[atributo].unique()
    classes = data_frame[atributo_classe].unique()
    qtd_total = len(data_frame[atributo])
    soma = 0
    for value in values:
        sub_set = data_frame[data_frame[atributo] == value]
        qtd_value = len(sub_set)
        p_v = qtd_value / qtd_total
        entropia_subset = entropia(data_frame=sub_set, classes=classes, atributo_classe=atributo_classe)
        soma += p_v * entropia_subset

    return entropia(data_frame, classes, atributo_classe) - soma

def construir_arvore(df, atributos, atributo_classe):
    classes_unicas = df[atributo_classe].unique()
    

    if len(classes_unicas) == 1:
        return classes_unicas[0]

   
    if len(atributos) == 0:
        return df[atributo_classe].mode()[0]  


    ganhos = {atrib: ganho(df, atrib, atributo_classe) for atrib in atributos}
    melhor_atributo = max(ganhos, key=ganhos.get)

    arvore = {melhor_atributo: {}}

    for valor in df[melhor_atributo].unique():
        subconjunto = df[df[melhor_atributo] == valor]
        if subconjunto.empty:
            arvore[melhor_atributo][valor] = df[atributo_classe].mode()[0]
        else:
            novos_atributos = [a for a in atributos if a != melhor_atributo]
            arvore[melhor_atributo][valor] = construir_arvore(subconjunto, novos_atributos, atributo_classe)

    return arvore

dados = {
    'Gênero': ['F', 'M', 'F', 'M', 'F', 'M', 'M', 'F', 'M', 'F'],
    'Idade': [22, 35, 28, 40, 23, 30, 36, 27, 50, 24],
    'Escolaridade': [
        'Médio', 'Superior completo', 'Superior incompleto', 'Superior completo',
        'Médio', 'Médio', 'Pós-graduação', 'Superior completo',
        'Pós-graduação', 'Superior incompleto'
    ],
    'Estado Civil': [
        'Solteiro', 'Casado', 'Solteiro', 'Divorciado', 'Solteiro',
        'Casado', 'Casado', 'Solteiro', 'Divorciado', 'Solteiro'
    ],
    'Renda (R$)': [2500, 4000, 3200, 4100, 2700, 3000, 4200, 2900, 4500, 2600],
    'Comprou': ['Não', 'Sim', 'Sim', 'Sim', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Não']
}

df = pd.DataFrame(dados)

df['Renda'] = pd.cut(df['Renda (R$)'], bins=3, labels=["Baixa", "Média", "Alta"])
df['Faixa Etária'] = pd.cut(df['Idade'], bins=3, labels=["Jovem", "Adulto", "Idoso"])
df.drop(columns=['Idade', 'Renda (R$)'], inplace=True)

atributos = [col for col in df.columns if col != 'Comprou']

arvore = construir_arvore(df, atributos, 'Comprou')

import pprint
pprint.pprint(arvore)
