import circlify
import matplotlib.pyplot as plt
import pandas as pd

# Carga el CSV real y proceso igual que antes
df = pd.read_csv("TV_show_data (2).csv")
import ast
def parse_genres(val):
    if isinstance(val, str):
        try:
            return ast.literal_eval(val)
        except:
            return []
    return val

df['Genres'] = df['Genres'].apply(parse_genres)
df_exploded = df.explode('Genres')

# Contar géneros
genre_counts = df_exploded['Genres'].value_counts()

# Para cada género, buscar el tipo más común
genre_type_mode = (
    df_exploded.groupby('Genres')['Type']
    .agg(lambda x: x.mode().iat[0] if not x.mode().empty else 'Unknown')
)

# Obtener lista de tipos únicos para colores
unique_types = genre_type_mode.unique()
color_map = {t: plt.cm.Set2(i / len(unique_types)) for i, t in enumerate(unique_types)}

# Crear datos para circlify
data = []
for genre, count in genre_counts.items():
    g_type = genre_type_mode[genre]
    color = color_map[g_type]
    data.append({'id': genre, 'datum': count, 'color': color, 'type': g_type})

# Crear estructura para circlify
circles = circlify.circlify(
    [d['datum'] for d in data],
    show_enclosure=False,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# Plot
fig, ax = plt.subplots(figsize=(12, 12))
ax.axis('off')
lim = max(
    max(abs(circle.x) + circle.r, abs(circle.y) + circle.r)
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

# Dibujar círculos y etiquetas
for circle, d in zip(circles, data):
    x, y, r = circle.x, circle.y, circle.r
    ax.add_patch(plt.Circle((x, y), r, color=d['color'], alpha=0.7, linewidth=2, ec='black'))
    plt.text(x, y, d['id'], ha='center', va='center', fontsize=12, weight='bold')

# Leyenda por tipo
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color_map[t], edgecolor='black', label=t) for t in unique_types]
plt.legend(handles=legend_elements, loc='lower left', bbox_to_anchor=(1, 0))

# Guardar imagen
plt.savefig("grafico7_circlepacking.png", bbox_inches='tight')
plt.close()
