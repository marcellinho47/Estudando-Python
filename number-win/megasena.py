import itertools
import pandas as pd
from collections import Counter

POSSIBLE_NUMBER = list(range(1, 60))

POSSIBLE_GAME_COMBINATIONS = list(itertools.combinations(POSSIBLE_NUMBER, 6))

print(f'Number of possible combinations: {len(POSSIBLE_GAME_COMBINATIONS)}')

df_past_win_combinations = pd.read_excel('.\\documents\\resultados_megasena.xlsx')

list_past_win_combinations = []

for index, row in df_past_win_combinations.iterrows():
    game = [row['bola 1'], row['bola 2'], row['bola 3'], row['bola 4'], row['bola 5'], row['bola 6']]
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
top_n_predicted_combinations = [comb for score, comb in predicted_combinations[:10]]

df_top_combinations = pd.DataFrame(top_n_predicted_combinations)
df_top_combinations.to_csv('.\\documents\\top_n_predicted_combinations.csv', index=False, header=True)
