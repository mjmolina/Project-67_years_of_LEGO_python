# Import modules
import pandas as pd
import matplotlib.pyplot as plt

# To read the sets data as `sets`
sets = pd.read_csv('datasets/sets.csv')

# To create a summary of average number of parts by year: `parts_by_year`
parts_by_year = sets[["year", "num_parts"]].groupby('year').mean()
print(parts_by_year)

# To plot the trends in average number of parts by year
parts_by_year.plot(x=None, y=None, kind='bar', ylim=(0,250))
plt.show()

