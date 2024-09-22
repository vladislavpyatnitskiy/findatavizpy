import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def hist_plt(x, log_returns=True):
  
  if log_returns:
    x = np.log(x / x.shift(1)).dropna()
  
  for column in x.columns:
        plt.figure()  # Create a new figure for each plot
        plt.hist(x[column])
        plt.title(column)
        plt.xlabel('Returns')
        plt.ylabel('Frequency')
        plt.show()

hist_plt(result) # Display
