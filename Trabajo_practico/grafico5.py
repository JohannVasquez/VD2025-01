import pandas as pd
import matplotlib.pyplot as plt
import squarify
import pycountry

df = pd.read_csv("tvs.csv")

df = df[df['origin_country[0]'].notna()]

country_counts = df['origin_country[0]'].value_counts().reset_index()
country_counts.columns = ['iso_alpha2', 'count']

def alpha2_to_country_name(code):
    try:
        return pycountry.countries.get(alpha_2=code).name
    except:
        return code

country_counts['country'] = country_counts['iso_alpha2'].apply(alpha2_to_country_name)

top_countries = country_counts.head(20)

cmap = plt.colormaps['YlOrRd']
norm = plt.Normalize(vmin=top_countries['count'].min(), vmax=top_countries['count'].max())
colors = [cmap(norm(val)) for val in top_countries['count']]

fig, ax = plt.subplots(figsize=(20, 12))
squarify.plot(
    sizes=top_countries['count'],
    label=[
        f"{country}\n{count} series"
        for country, count in zip(top_countries['country'], top_countries['count'])
    ],
    color=colors,
    alpha=0.85,
    text_kwargs={'fontsize': 10},
    ax=ax
)
ax.axis('off')
plt.title("Treemap - Top 20 Países que más series han producido", fontsize=16)

import matplotlib.cm as cm
sm = cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, pad=0.02)
cbar.set_label('Cantidad de series producidas', fontsize=12)

ax.invert_yaxis()

plt.show()