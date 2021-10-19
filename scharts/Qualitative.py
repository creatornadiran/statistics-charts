import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import PercentFormatter

class QualitativeCharts:
    def bar_chart(data):
        """
        draws bar chart
        DataFrame must in shape (*,2)
        """
        if data.shape[1] == 2:
            plt.bar(data.iloc[:, 0], data.iloc[:, 1])
            plt.title("Bar Chart")
            plt.xticks(rotation=30)
            plt.show()
        else:
            print("Data must have 2 column")

    def pie_chart(data):
        """
        draws pie chart
        DataFrame must in shape (*,2)
        """
        if data.shape[1] == 2:
            plt.pie(data.iloc[:, 1], labels=data.iloc[:, 0], autopct='%1.1f%%')
            plt.title("Pie Chart")
            plt.show()
        else:
            print("Data must have 2 column")

    def pareto_chart(data):
        """
        draws pareto chart
        DataFrame must in shape (*,2)
        """
        if data.shape[1] == 2:
            df = data.sort_values(by=data.columns[1], ascending=False)
            df["cum_percentage"] = df.iloc[:, 1].cumsum() / df.iloc[:, 1].sum() * 100
            fig, ax1 = plt.subplots()
            ax1.bar(df.iloc[:, 0], df.iloc[:, 1], label="numbers")
            ax2 = ax1.twinx()
            ax2.plot(df.iloc[:, 0], df.iloc[:, 2], color='orange', label="cum-percentages", marker="D", ms=7)
            ax2.yaxis.set_major_formatter(PercentFormatter())
            ax1.tick_params(axis="y", colors="C0")
            ax2.tick_params(axis="y", colors="C1")
            plt.title("Pareto Chart")
            plt.xticks(rotation=30)
            plt.show()
        else:
            print("Data must have 2 column ([type,count])")
