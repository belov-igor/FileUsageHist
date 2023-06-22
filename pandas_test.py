import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(seed=42)
data_points = 1000

df = pd.DataFrame(data=list(zip(np.random.choice(["Math", "English"], size=data_points),
                                np.random.beta(15, 10, size=data_points),
                                np.random.beta(30, 4, size=data_points))),
                  columns=['Major', 'Test1', 'Test2'])

df.head()
print(df)
df.hist(column='Test1')