import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import probplot
import pandas as pd

def qq_plot(x, log=False): # QQ Plot for stock returns
  
    if log:
        data = np.log(x / x.shift(1)).dropna() # Returns

    for column in data.columns:
        plt.figure()  # Create a new figure for each plot
        probplot(x[column], plot=plt)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.title(f"{column} Q-Q Plot")
        plt.show()
        
qq_plot(result, log=True)  # Set log=True if log returns
