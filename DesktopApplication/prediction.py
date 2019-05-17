import numpy as np
from sklearn.preprocessing  import StandardScaler

def pred(livingArea, landValue, price):
    X = np.array([[livingArea,landValue,price]])
    std = StandardScaler()
    X = std.fit_transform(X)
    b = [0.38045592, 0.3160429 , 0.16668651]
    y_pred = X.dot(b)
    return y_pred