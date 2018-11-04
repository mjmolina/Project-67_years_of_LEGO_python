# Import modules
import pandas as pd
import matplotlib.pyplot as plt


# To read colors from the database
colors = pd.read_csv('datasets/colors.csv')

# To print the first few rows
colors.head()

# How many differents colors are available in lEGO?

num_colors = colors.shape[0]
print(num_colors)

# colors_summary:Colors distributions focud on the transparency. 

colors_summary = colors.groupby('is_trans').count()
print(colors_summary)



