import pandas as pd
from matplotlib import pyplot as plt
import os

# The directory in which the data is stored.
data_dir = f"{os.getcwd()}/../data/Experiment1000/data/"

# Loop through the data directory.
for fname in os.listdir(data_dir):
    # Check if it is a data file.
    if "All_Data_" in fname and "~lock" not in fname:
        # Create a (pandas) dataframe object from the .csv file.
        df = pd.read_csv(f"{data_dir}{fname}")
        # x = The first column in the spreadsheet.
        x = df["CH1"]
        # Count from 0 to the length of x.
        y = [i for i, elm in enumerate(df["CH1"].tolist())]
        line = plt.plot(y, x)
        plt.show()
