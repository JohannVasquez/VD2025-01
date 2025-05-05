import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Cargar archivo
df = pd.read_csv("Encuesta VD.csv", encoding="latin1")

# Crear conjuntos
set1 = set(df[df['¿Dónde sueles ver anime?'] == 'Netflix']['Token'])
set2 = set(df[df['¿Prefieres anime doblado o subtitulado?'] == 'Doblado']['Token'])

# Dibujar Venn
plt.figure(figsize=(6,6))
venn2([set1, set2], set_labels=('Usan Netflix', 'Prefieren Doblado'))
plt.title("Relación entre plataforma y tipo de doblaje")
plt.show()