import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importer jeu de donnees:
url = 'https://raw.githubusercontent.com/LesMouettesSavantes/MouettesProjetTemperatures/main/All_temperatures.csv'
df = pd.read_csv(url)

print(df.head()) # affiche les premieres lignes du tableau

n = np.size(df.iloc[:,1])
np.sum(df.iloc[:,1])/n
