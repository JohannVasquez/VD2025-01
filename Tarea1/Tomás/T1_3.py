import pandas as pd
import matplotlib.pyplot as plt
import squarify
import ast
import matplotlib.cm as cm
import matplotlib.colors as colors

df = pd.read_csv('TV_show_data.csv', low_memory=False)

df = df.dropna(subset=['Genres', 'Rating'])
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df = df.dropna(subset=['Rating'])

df['Genres'] = df['Genres'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])

df_exploded = df.explode('Genres')

#Excluyo 'Adult', 'DIY' y 'Travel' de la lista de géneros, debido a su poca relevancia frente a otros géneros.
excluded_genres = ['Adult', 'DIY', 'Travel']
df_exploded = df_exploded[~df_exploded['Genres'].isin(excluded_genres)]

genre_group = df_exploded.groupby('Genres').agg(
    count=('Name', 'count'),
    avg_rating=('Rating', 'mean')
).reset_index()

genre_group = genre_group.sort_values(by=['count', 'avg_rating'], ascending=[False, False]).head(20)

cmap = plt.colormaps['YlGn']
norm = colors.Normalize(vmin=genre_group['avg_rating'].min(), vmax=genre_group['avg_rating'].max())
color_list = [cmap(norm(r)) for r in genre_group['avg_rating']]

fig, ax = plt.subplots(figsize=(20, 12))
squarify.plot(
    sizes=genre_group['count'],
    label=[
        f"{g}\n{c} series\n★ {r:.1f}"
        for g, c, r in zip(genre_group['Genres'], genre_group['count'], genre_group['avg_rating'])
    ],
    color=color_list,
    alpha=0.85,
    text_kwargs={'fontsize': 10},
    ax=ax
)
ax.axis('off')
plt.title("Treemap - Top 20 Géneros (sin Adult, DIY, Travel) ordenado por Relevancia", fontsize=16)

sm = cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, pad=0.02)
cbar.set_label('★ Rating promedio por género', fontsize=12)

# Se invierte el eje y para que los géneros con más series aparezcan en la parte superior.
ax.invert_yaxis()

plt.show()