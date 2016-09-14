# Import libraries necessary for this project
import numpy as np
import pandas as pd
import renders as rs
from IPython.display import display # Allows the use of display() for DataFrames


# Read dataset
data = pd.read_csv("customers.csv")
print "Dataset has {} rows, {} columns".format(*data.shape)
print data.head()  # print the first 5 rows

pd.scatter_matrix(data, alpha = 0.3, figsize = (14,8), diagonal = 'kde');
