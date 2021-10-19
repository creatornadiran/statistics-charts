from scharts import QuantitativeDistributions,QuantitativeCharts
import pandas as pd
import numpy as np
if __name__ == "__main__":
    objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    user_num = [10, 8, 6, 4, 2, 1]
    qual_DataFrame = pd.DataFrame()
    qual_DataFrame["objects"] = objects
    qual_DataFrame["user_num"] = user_num
    grades = np.random.randint(0,10,(150))
    scatter_data = pd.DataFrame({"col1":np.random.randint(0,150,(150)), "col2":np.random.randint(0,10,(150))})
    QuantitativeCharts.scatter_plot(scatter_data)