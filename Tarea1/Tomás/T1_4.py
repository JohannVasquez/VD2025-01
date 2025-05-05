import pandas as pd
import matplotlib.pyplot as plt
import ast

df = pd.read_csv('TV_show_data.csv', low_memory=False)

df['Average Runtime'] = pd.to_numeric(df['Average Runtime'], errors='coerce')

df = df.dropna(subset=['Genres', 'Average Runtime'])
df['Genres'] = df['Genres'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
df_exploded = df.explode('Genres')

genre_runtime = df_exploded.groupby('Genres')['Average Runtime'].mean().sort_values()

fig, ax = plt.subplots(figsize=(10, 8))

for i, (genre, avg_runtime) in enumerate(genre_runtime.items()):
    ax.plot([0, avg_runtime], [i, i], color='gray', lw=2)
    ax.plot(avg_runtime, i, 'o', color='blue')

ax.set_yticks(range(len(genre_runtime)))
ax.set_yticklabels(genre_runtime.index)
ax.set_xlabel('Tiempo Promedio (minutos)')
ax.set_title('Dumbbell Plot - Duración promedio por episodio según género')
plt.tight_layout()
plt.show()
