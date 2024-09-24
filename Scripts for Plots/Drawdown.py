import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def drawdown_plt(x):
  
  x = np.log(x / x.shift(1)).dropna() * 100
  
  x[x > 0] = 0
  
  for column in x.columns:
        plt.figure()  # Create a new figure for each plot
        plt.plot(x[column])
        plt.title(f"{column} Drawdown")
        plt.xlabel('Trading Days')
        plt.ylabel('Negative Return (%)')
        plt.show()
        
drawdown_plt(result)
