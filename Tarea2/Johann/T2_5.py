import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar archivo
df = pd.read_csv("../Encuesta_T2_VD.csv", encoding="latin1")

# Crear gráfico
plt.figure(figsize=(10,6))
sns.violinplot(data=df, x='¿Prefieres anime doblado o subtitulado?',
               y='¿Cuántas series de anime completas has visto este año?')
plt.title("Distribución de cantidad de series vistas según preferencia")
plt.show()
