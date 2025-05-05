import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import numpy as np

# Cargar archivo
df = pd.read_csv("../Encuesta_T2_VD.csv", encoding="latin1")


pivot = pd.crosstab(df['¿Cuántas horas a la semana dedicas a ver anime?'],
                    df['¿Cuántas series de anime completas has visto este año?'])

def truncate_colormap(cmap, minval=0.2, maxval=1.0, n=100):
    new_cmap = LinearSegmentedColormap.from_list(
        f"trunc({cmap.name},{minval:.2f},{maxval:.2f})",
        cmap(np.linspace(minval, maxval, n))
    )
    return new_cmap

# Crear colormap truncado
green_cmap = truncate_colormap(plt.cm.Greens, 0.3, 1.0)

# Plot
plt.figure(figsize=(8,6))
sns.heatmap(pivot, annot=True, cmap=green_cmap)

# Invertir el eje Y
plt.gca().invert_yaxis()

plt.title("Relación entre horas vistas y cantidad de series")
plt.xlabel("Series vistas")
plt.ylabel("Horas semanales")
plt.show()
