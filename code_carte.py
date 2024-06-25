url = 'https://raw.githubusercontent.com/LesMouettesSavantes/MouettesProjetTemperatures/main/Stations_id.csv'
coord = pd.read_csv(url)

coord.head()

import plotly.express as px
fig = px.scatter_mapbox(coord, 
                        lat="lat", 
                        lon="lon", 
                        hover_name="STANAME", 
                        color=all_means,
                        height=800,
                        width=800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
