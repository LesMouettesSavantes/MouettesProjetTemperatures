import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importer jeu de donnees:
df = pd.read_csv("/home/legrand/Documents/Mouettes_Savantes/donnees/All_temperatures.csv")

print(df.head()) # affiche les premieres lignes du tableau

n = np.size(df.iloc[:,1])
np.sum(df.iloc[:,1])/n
