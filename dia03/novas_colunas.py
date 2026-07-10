# %%
import pandas as pd
import numpy as np

df = pd.read_csv('../data/customers.csv', sep=';')
df

# %%
df['Points_doubble'] = df['Points'] * 2
df

# %%
df['Points_ratio'] = df['Points_doubble'] / df['Points']
df

# %%
df['Constante'] = 1
df

# %%
df['Points_log'] = np.log(df['Points'])
df

# %%
df['Name'].str.upper()

# %%

def get_first(nome):
    nome = nome.upper()
    return nome.split('_')[0]

# %%
df['Name_First'] = df['Name'].apply(get_first)
df

# %%
soma = lambda x,y: x + y

# %%
def intervalo_pontos(pontos):

    if pontos < 2500:
        return 'baixo'
    
    elif pontos < 3500:
        return 'medio'
    
    else:
        return 'alto'
    
df['faixa_Pontos'] = df['Points'].apply(intervalo_pontos)
df
