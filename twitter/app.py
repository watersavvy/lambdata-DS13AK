import pandas as pd
import time

df = pd.DataFrame([[1, 5, 9], [2, 5, 7], [1, 1, 0]])

while 1==1:
    time.sleep(2)
    df = df + 1
    print(df.head())