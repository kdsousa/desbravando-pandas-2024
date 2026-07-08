# %%
import pandas as pd

# %%

idades = [30, 42, 90, 34]
idades

# %%
# Transformação para series Pandas
series_idades = pd.Series(idades)
series_idades

# %%
# Métodos da séres pandas
# Média
series_idades.mean()

# %%
# Variancia
series_idades.var()
# Desvio Padrão
series_idades.std()

# %%
# Mediana
series_idades.median()

# %%
# Sumarização
series_idades.describe()

# %%
# Dimensão da Séries
series_idades.shape

# %%
# Navegando na lista 
idades[0]

# %%
# Navegando na série
series_idades[0]

# %%
# Alterando index da série
series_idades.index = ['a', 'b', 'c', 'd']

# %%
# Navegando nos índices novos
series_idades['c']

# %%

series_idades.iloc[0]

# %%

series_idades.loc['b']

# %%

series_idades.name = 'idades'
series_idades

# %%
