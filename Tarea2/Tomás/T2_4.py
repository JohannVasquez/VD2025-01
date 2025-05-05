import pandas as pd
import matplotlib.pyplot as plt
import squarify
import matplotlib.cm as cm
import matplotlib.colors as colors

df = pd.read_csv("../Encuesta_T2_VD.csv", encoding="latin1")

data = df['¿Cuántas series de anime completas has visto este año?'].value_counts()
labels = [f"{k}\n({v})" for k, v in data.items()]

norm = colors.Normalize(vmin=min(data.values), vmax=max(data.values))
color_map = cm.Greens
colors_list = [color_map(norm(value)) for value in data.values]

plt.figure(figsize=(10, 6))
squarify.plot(sizes=data.values, label=labels, color=colors_list, alpha=0.9)
plt.title("Cantidad de series completas vistas")
plt.axis('off')
plt.gca().invert_yaxis()
plt.show()
