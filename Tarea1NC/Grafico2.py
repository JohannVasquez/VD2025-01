import pandas as pd
import plotly.express as px
import pycountry

df = pd.read_csv("tvs.csv")

df = df[df['origin_country[0]'].notna()]
country_counts = df['origin_country[0]'].value_counts().reset_index()
country_counts.columns = ['iso_alpha2', 'count']

def alpha2_to_alpha3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None

country_counts['iso_alpha3'] = country_counts['iso_alpha2'].apply(alpha2_to_alpha3)
country_counts = country_counts.dropna(subset=['iso_alpha3'])

fig = px.choropleth(country_counts,
                    locations='iso_alpha3',
                    color='count',
                    color_continuous_scale=px.colors.sequential.Turbo,
                    title='Series producidas por país',
                    labels={'count': 'Cantidad de series'})

fig.show()
