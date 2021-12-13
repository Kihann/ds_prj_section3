import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm

raw_df = pd.read_csv('rawdata.csv')
raw_df['date'] = pd.to_datetime(raw_df['date'])
raw_df = raw_df.drop_duplicates(['date'])
raw_df = raw_df.set_index('date')

def mynum(column):
  column = column.replace(',', '')
  return int(column)

for i in range(0, 6+1):
  raw_df.iloc[:, i] = raw_df.iloc[:, i].apply(mynum)

raw_df['updown'] = raw_df['up'] + raw_df['down']
raw_df = raw_df.drop(['up', 'down'], axis = 1)
df = raw_df.drop(['updown', 'open_price', 'high_price', 'low_price', 'trading_volume'], axis = 1)

model = ARIMA(df.close_price.values, order = (2,1,1))
model_fit = model.fit(trend = 'c', full_output = True, disp = True)

forecast_data = model_fit.forecast(steps=5)
y_pred = np.round(forecast_data[0].tolist(), -2)
y_pred = [int(i) for i in y_pred]

print(forecast_data[0])