import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import probplot

def qq_plot(data, log=False):
    if log:
        data = np.diff(np.log(data), axis=0)[1:]

    num_assets = data.shape[1]
    
    for n in range(num_assets):
        asset_data = data[:, n]
        
        plt.figure()
        plt.title("Q-Q Plot")
        probplot(asset_data, plot=plt)
        plt.grid(True, linestyle='--', alpha=0.7)
        
        plt.show()

# Assuming 'returns_df' is a DataFrame containing your return data
# Example usage
qq_plot(result, log=True)  # Set log=True if log returns
