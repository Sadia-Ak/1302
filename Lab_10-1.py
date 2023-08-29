import pandas as pd

data = {'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690],
        'Ranking': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
        'Team': ['red', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'yellow', 'red', 'blue'],
        'year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
        'MVP': ['Kevin', 'Kevin', 'mike', 'john', 'parth', 'mark', 'Aron', 'neil', 'edward', 'max', 'neil', 'john']}

df = pd.DataFrame(data)
grouped = df.groupby('year')
grouped_df = grouped.agg({'Points': 'sum',
                           'Ranking': 'mean',
                           'Team': lambda x: x.iloc[0],
                           'MVP': lambda x: x.iloc[0]})
print(grouped_df)