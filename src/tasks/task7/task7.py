import random
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

amount=20000

dice1 = [random.randint(1,6) for _ in range(0,amount)]
dice2 = [random.randint(1,6) for _ in range(0,amount)]

rolls=[dice1[i]+dice2[i] for i in range(0,amount)]

count = Counter(rolls)

percentage=percentage = {key: f'{round(count[key] / amount * 100, 2)}%' for key in range(2, 13)}

keys = list(percentage.keys()) 
values = [float(value.strip('%')) for value in percentage.values()]

plt.figure(figsize=(10, 6))
bars = plt.bar(keys, values, color='skyblue')

for bar, value in zip(bars, values):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.3, f'{value}%', ha='center', va='bottom', fontsize=10)
    plt.text(bar.get_x() + bar.get_width() / 2, yval/2, f'{int(round(36*value/100,0))}/36', ha='center', va='bottom', fontsize=10)

plt.title('Sum repetitions', fontsize=14)
plt.xlabel('Sum', fontsize=12)
plt.ylabel('Repetition (%)', fontsize=12)
plt.ylim(0,20)

df = pd.DataFrame(list(percentage.items()), columns=['Sum', 'Repetition percentage'])
df.set_index('Sum', inplace=True)
print(df)

plt.show()          

