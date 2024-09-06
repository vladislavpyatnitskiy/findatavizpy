# Function to generate line plot
def line_plt(dataframe):
    for column in dataframe.columns:
        plt.figure()  # Create a new figure for each plot
        plt.plot(dataframe[column])
        plt.title(column)
        plt.xlabel('Trading Days')
        plt.ylabel('Prices')
        plt.show()

line_plt(result)
