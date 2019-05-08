import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('SaratogaHouses.csv')
print(dataset.head())

X = dataset['livingArea']
y = dataset['price']
plt.title("Price W.R.T Living Area")
plt.xlabel('Living Area')
plt.ylabel('Price')
plt.boxplot(y)
plt.show()
