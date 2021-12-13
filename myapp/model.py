import pandas as pd
from sklearn.linear_model import LinearRegression
from category_encoders import BinaryEncoder
from sklearn.pipeline import make_pipeline

df_X = pd.read_csv('X_train.csv')
df_y = pd.read_csv('y_train.csv')
X = df_X.drop(['fuelType', 'transmission', 'carID', 'brand', 'model'], axis = 1)
y = df_y.drop(['carID'], axis = 1)

# enc = BinaryEncoder(cols=['transmission', 'fuelType']).fit(X)
# X = enc.transform(X)

model = LinearRegression()
model.fit(X, y)

X_test = [[1999, 10000, 1000.0, 1500.0, 1]]
y_pred = model.predict(X_test)