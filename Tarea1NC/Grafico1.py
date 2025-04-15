import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("tvs.csv")

df = df[df['vote_average'].notna() & df['genres[0].name'].notna()]

plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='genres[0].name', y='vote_average')
plt.title('Distribución de rating promedio por género principal')
plt.xlabel('Género principal')
plt.ylabel('Rating promedio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
