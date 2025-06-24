import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("tvs.csv")

country_cols = ['origin_country[0]','origin_country[1]','origin_country[2]','origin_country[3]']
genre_cols   = [f'genres[{i}].name' for i in range(8)]
df_anime = df[
    df[country_cols].apply(lambda r: 'JP' in r.values, axis=1) &
    df[genre_cols].apply(lambda r: 'Animation' in r.values, axis=1)
]

df_anime['first_air_date'] = pd.to_datetime(df_anime['first_air_date'], errors='coerce')
df_anime = df_anime.dropna(subset=['first_air_date'])
df_anime['decade'] = (df_anime['first_air_date'].dt.year // 10) * 10

counts    = df_anime['decade'].value_counts().sort_index()
labels    = counts.index.astype(int).tolist()
values    = counts.values.astype(float)
max_val   = values.max()
total     = values.sum()

N         = len(values)
thick     = 0.8          # grosor
gap       = 0.2          # separación 
full_turn = 2*np.pi     
max_arc   = full_turn*0.85 

fig, ax = plt.subplots(figsize=(8,8), subplot_kw=dict(polar=True))
ax.set_theta_zero_location('W')
ax.set_theta_direction(-1)
ax.set_xticks([])

centers = [i*(thick+gap)+thick/2 for i in range(N)]
ax.set_yticks(centers)
ax.set_yticklabels(labels, fontsize=10, ha='right')
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.7)
ax.set_ylim(0, N*(thick+gap))

for i, (lab, val) in enumerate(zip(labels, values)):
    angle = (val / max_val) * max_arc
    
    base = i * (thick + gap)
    ax.bar(
        x=angle/2,      
        height=thick,  
        width=angle,     
        bottom=base,
        color=plt.cm.Blues(val/max_val),
        edgecolor='white',
        linewidth=1
    )

    ax.text(
        x=angle + 0.02,   
        y=base + thick/2,
        s=str(int(val)),
        ha='left', va='center',
        fontsize=9
    )


ax.set_title("Cantidad de Animes por Década", y=1.05, fontsize=16, weight='bold')

plt.tight_layout()
plt.show()
