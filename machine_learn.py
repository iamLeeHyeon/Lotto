
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# CSV Read
df = pd.read_csv('Lotto.csv')

# Date to int
df['draw_date'] = pd.to_datetime(df['draw_date']).astype('int64') / 10**9

# select win cols
win_num_cols = [f'win_num_{i+1}' for i in range(6)]
y = df[win_num_cols]

X = df.drop(columns=win_num_cols + ['sum'])

# data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model learning
model = LinearRegression()
model.fit(X_train, y_train)

# model rate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
