import pandas as pd
import matplotlib.pyplot as plt

# To read the sets data as `sets`
sets = pd.read_csv('datasets/sets.csv')

# To know how many themes of LEGO are shipped there are per year : themes_by_year

themes_by_year=sets[["year", "theme_id"]].groupby('year', as_index=False).agg({"theme_id": pd.Series.nunique})
themes_by_year.shape
print(themes_by_year)

themes_by_year.plot("year")
plt.show()
