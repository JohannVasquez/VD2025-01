import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos desde el archivo JSON
def load_data(file_path):
    return pd.read_json(file_path)

# Función para imprimir las columnas del DataFrame
def print_columns(df):
    print("Columnas del DataFrame:")
    for column in df.columns:
        print(column)

# Cargar el archivo JSON
df = load_data('tvs.json')
df_filtered = df[df['vote_average'] != 0]
df_filtered = df_filtered[df_filtered['number_of_episodes'] != 0]

# Imprimir las columnas del DataFrame
print_columns(df_filtered)

# Crear una nueva columna para los rangos de temporadas
bins = [0, 2, 3, 5, 10, 20, 30, 60, 100, 200, 400]  # Define los límites de los rangos
labels = ['1', '2-3', '4-5', '6-10', "11-20", '21-30', '31-60', '61-100', '101-200', '201+']  # Etiquetas para los rangos
df_filtered['season_range'] = pd.cut(df_filtered['number_of_seasons'], bins=bins, labels=labels, right=False)

# Crear la tabla dinámica para el heatmap
heat_df = df_filtered.explode('genres').pivot_table(
    index=df_filtered['genres'].apply(lambda x: x[0]['name'] if x else None),
    columns='season_range',
    values='name',
    aggfunc='count',
    fill_value=0,
    observed=True
)

# Crear el heatmap sin la máscara
plt.figure(figsize=(10, 5))
sns.heatmap(heat_df, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Cantidad'}, vmin=1, vmax=10000)
plt.title('Cantidad de series por género y rango de temporadas (Heatmap)')
plt.xlabel('Rango de temporadas')
plt.ylabel('Género')
plt.tight_layout()
plt.show()