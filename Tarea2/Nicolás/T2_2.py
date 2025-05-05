import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle

# Cargar archivo
df = pd.read_csv("Encuesta VD.csv", encoding="latin1")

# Contar valores
data = df['¿Dónde sueles ver anime?'].value_counts()

# Crear gráfico
fig = plt.figure(
    FigureClass=Waffle,
    rows=5,
    values=data,
    title={'label': 'Distribución por plataforma', 'loc': 'center'},
    labels=[f"{k} ({v})" for k,v in data.items()],
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
)
plt.show()