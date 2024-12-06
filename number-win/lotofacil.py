import itertools
import pandas as pd
from collections import Counter

'''
Concurso,Data,bola 1,bola 2,bola 3,bola 4,bola 5,bola 6,bola 7,bola 8,bola 9,bola 10,bola 11,bola 12,bola 13,bola 14,bola 15
3254,27/11/2024,11,10,6,7,3,16,22,19,18,24,17,21,4,8,5

'''

POSSIBLE_NUMBER = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

POSSIBLE_GAME_COMBINATIONS = list(itertools.combinations(POSSIBLE_NUMBER, 15))

print(f'Number of possible combinations: {len(POSSIBLE_GAME_COMBINATIONS)}')

df_past_win_combinations = pd.read_excel('.\\documents\\resultados_lotofacil.xlsx')

list_past_win_combinations = []

for index, row in df_past_win_combinations.iterrows():
    game = [row['bola 1'], row['bola 2'], row['bola 3'], row['bola 4'], row['bola 5'], row['bola 6'], row['bola 7'],
            row['bola 8'], row['bola 9'], row['bola 10'], row['bola 11'], row['bola 12'], row['bola 13'],
            row['bola 14'], row['bola 15']]
    game = tuple(sorted(game))
    list_past_win_combinations.append(game)

    if game in POSSIBLE_GAME_COMBINATIONS:
        POSSIBLE_GAME_COMBINATIONS.remove(game)

# Count the frequency of each number in past winning combinations
number_frequency = Counter()
for combination in list_past_win_combinations:
    number_frequency.update(combination)

# Sort numbers by frequency
sorted_numbers_by_frequency = [number for number, freq in number_frequency.most_common()]

# Apply this model to all possible combinations to predict possible next win
predicted_combinations = []
for combination in POSSIBLE_GAME_COMBINATIONS:
    score = sum(sorted_numbers_by_frequency.index(num) for num in combination)
    predicted_combinations.append((score, combination))

# Sort predicted combinations by score
predicted_combinations.sort()

# Get the top N predicted combinations
top_n_predicted_combinations = [comb for score, comb in predicted_combinations[:5]]

df_combinations = pd.DataFrame(predicted_combinations)
df_combinations.to_csv('.\\documents\\predicted_combinations.csv', index=False, header=True)

df_top_combinations = pd.DataFrame(top_n_predicted_combinations)
df_top_combinations.to_csv('.\\documents\\top_n_predicted_combinations.csv', index=False, header=True)

print(f'Top 10 predicted combinations: {top_n_predicted_combinations}')
