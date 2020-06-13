# Mid-Term Project
# Austin Dobbins
# DSC540-T301

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz

# Import data into a dataframe
data = r'C:\Users\austi\OneDrive\Desktop\basic_per_game_player_stats_2013_2018.csv'
df = pd.read_csv(data)

# Print the headers of the dataframe
print(df.columns)

# Change the headers
df.columns = ['Rank', 'Player', 'Age', 'Position', 'Date', 'Team', 'Home/Away', 'Opponent', 'Win/Loss', 'Started',
            'Minutes Played', 'Field Goals', 'FG Attempts', 'FG Percentage',   '2 Point Shots',
            '2 Point Shot Attempts',
            '2 Point Shot Percentage', '3 Point Shot', '3 Point Shot Attempts', '3 Point Shot Percentage',
            'Free Throws', 'Free Throws Attempted', 'Free Throw Percentage', 'Off Rebounds', 'Def Rebounds',
            'Total Rebounds', 'Assist', 'Steals', 'Blocks', 'Turnovers', 'Personal Fouls', 'Points', 'Game Score']
# Display new headers
print(df.columns)

# Find Outliers in Variables Using BoxPlot
sns.boxplot(x=df['Points'])
plt.show()

sns.boxplot(x=df['3 Point Shot Percentage'])
plt.show()

sns.boxplot(x=df['Turnovers'])
plt.show()

# Identify Duplicates in Age Column
dups = df['Age'].duplicated(keep=False)
print(dups)

# Fuzzy Matching on Player Column
fuzz.ratio(df['Player'])




