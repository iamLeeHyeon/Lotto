import pandas as pd
import matplotlib.pyplot as plt

# CSV Read
df = pd.read_csv('Lotto.csv')

# win num cols
win_num_cols = [f'win_num_{i+1}' for i in range(6)]
win_nums_df = df[win_num_cols]

# describe
desc = win_nums_df.describe()

# mean plt
plt.figure(figsize=(10,6))
plt.bar(win_num_cols, desc.loc['mean'])
plt.title('Mean of each winning number')
plt.ylabel('Mean')
plt.show()

# std plt
plt.figure(figsize=(10,6))
plt.bar(win_num_cols, desc.loc['std'])
plt.title('Standard deviation of each winning number')
plt.ylabel('Standard deviation')
plt.show()

# meadian plt
plt.figure(figsize=(10,6))
plt.bar(win_num_cols, desc.loc['50%'])  
plt.title('Median of each winning number')
plt.ylabel('Median')
plt.show()