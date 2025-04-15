import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el archivo JSON
def load_data(file_path):
    return pd.read_json(file_path)

# Cargar el archivo JSON
df = load_data('tvs.json')

# Filtrar los datos para excluir vote_average = 0
df_filtered = df[df['vote_average'] != 0]
df_filtered = df_filtered[df_filtered['number_of_episodes'] != 0]
df_filtered = df_filtered[df_filtered['number_of_seasons'] != 0]


# Mostrar las primeras filas del DataFrame filtrado para verificar
print(df_filtered.head())

# Crear el gráfico usando los datos filtrados
plt.figure(figsize=(8, 5))
plt.hexbin(df_filtered['number_of_seasons'], df_filtered['vote_average'], gridsize=10, cmap='Purples', edgecolors='none', vmin=1, vmax=10000)
plt.colorbar(label='Cantidad de series')
plt.xlabel('Número de temporadas')
plt.ylabel('Rating promedio')
plt.title('Relación entre rating y número de temporadas (Hexbin Plot)')
plt.tight_layout()
plt.show()