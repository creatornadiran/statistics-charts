import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from .Qualitative import QualitativeCharts
class QuantitativeDistributions:
    def frequency_distribution(data, k=None):
        """
        print frequency distribution of data
        DataFrame must in shape (*,)
        """
        if len(data.shape) == 1:
            data_range = data.max()-data.min()
            if k==None:
                k = np.ceil(np.sqrt(data.shape[0]))
            class_width = np.ceil((data_range/k)*100)/100
            floor = data.min()
            ranges =[]
            frequencies =[]
            for i in range(1,k+1):
                ceil = floor+class_width
                ranges.append(f"({floor:.2f}-{ceil:.2f})")
                frequencies.append(data[(data>=floor) & (data<ceil)].shape[0])
                floor = ceil
            dataFrame = pd.DataFrame()
            dataFrame["ranges"] = ranges
            dataFrame["frequencies"] = frequencies
            QualitativeCharts.bar_chart(dataFrame)
        else:
            print("Data must be 1 dim")
class QuantitativeCharts:
    def histogram(data):
        """
        draws histogram
        DataFrame must in shape (*,)
        """
        if len(data.shape) == 1:
            plt.hist(data)
            plt.title("Histogram")
            plt.xticks(rotation=30)
            plt.show()
        else:
            print("Data must be 1 dim")
    def scatter_plot(data):
        """
        draws scatter_plot
        DataFrame must in shape (*,2) and 2 variables must be quantitative
        """
        if data.shape[1] == 2:
            plt.scatter(data.iloc[:,0], data.iloc[:,1])
            plt.title("Scatter Plot")
            plt.xticks(rotation=30)
            plt.show()
        else:
            print("Data must be 2 dim")

