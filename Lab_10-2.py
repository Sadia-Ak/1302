import pandas as pd

data1 = {'Player_name': ['player 1', 'player 2', 'player 3', 'player 4', 'player 5', 'player 6', 'player 7', 'player 8'],
         'game 1': [100, 99, 101, 86, 120, 111, 135, 26],
         'game 2': [78, 45, 14, 78, 45, 56, 89, 85],
         'game 3': [98, 78, 47, 100, 99, 96, 87, 87]}
table1 = pd.DataFrame(data1)


data2 = {'Player_name': ['player 8', 'player 9', 'player 10', 'player 11', 'player 4', 'player 13', 'player 14', 'player 15', 'player 16'],
         'game 1': [26, 100, 25, 47, 86, 78, 89, 74, 87],
         'game 2': [85, 65, 58, 111, 100, 96, 74, 85, 74],
         'game 3': [87, 65, 66, 47, 100, 74, 77, 98, 89]}
table2 = pd.DataFrame(data2)

concatenated = pd.concat([table1, table2], axis=1)

print(concatenated)
