import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Encuesta_T2_VD.csv", encoding="latin1")

plt.figure(figsize=(10,3))
sns.stripplot(data=df, x='¿Cuántas horas a la semana dedicas a ver anime?',
              y='¿Prefieres anime doblado o subtitulado?', jitter=True, size=8)
plt.title("Tipo de preferencia según horas de visualización")
plt.show()