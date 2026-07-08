# %%
import pandas as pd

# %%

data = {
    'nome': ['kepler', 'nah', 'valquiria', 'maria'],
    'sobrenome': ['batista', 'ataide', 'batista', 'batista'],
    'idade': [31, 32, 2, 31]

}

# %%

data['idade'][0]

# %%

df = pd.DataFrame(data)
df

# %%

df['idade']

# %%

df['idade'][0]

# %%

type(df['idade'])

# %%

df['sobrenome']

# %%

df.iloc[0]

# %%

df.index

# %%

df.columns

# %%

df.info(memory_usage='deep')

# %%

df.dtypes

# %%

df['peso'] = [80, 53, 65, 14]
df.describe()

# %%

df.head()

# %%

df.tail()
