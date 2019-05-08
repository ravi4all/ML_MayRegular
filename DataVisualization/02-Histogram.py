import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('SaratogaHouses.csv')
print(dataset.head())

X = dataset['rooms']
plt.hist(X)
plt.show()
