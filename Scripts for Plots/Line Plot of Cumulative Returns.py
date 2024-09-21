import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def cmlplot(x):
  
  x = (np.exp(np.cumsum(np.log(x / x.shift(1)).dropna())) - 1) * 100
  
  for column in x.columns:
        plt.figure()  # Create a new figure for each plot
        plt.plot(x[column])
        plt.title(column)
        plt.xlabel('Trading Days')
        plt.ylabel('Return (%)')
        plt.show()
        
cmlplot(result)
