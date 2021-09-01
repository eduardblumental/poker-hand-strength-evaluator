import sys
from itertools import combinations
from textwrap import wrap


def string_hand_to_list(hand):
    return wrap(hand, 2)


def return_all_possible_combinations(game_type, table, hand):
    if game_type == 'texas-holdem':
        for combo in combinations(table + hand, 5):
            yield combo
    elif game_type == 'omaha-holdem':
        for table_combo in combinations(table, 3):
            for hand_combo in combinations(hand, 2):
                combo = table_combo + hand_combo
                yield combo
    elif game_type == 'five-card-draw':
        yield hand


if __name__ == "__main__":
    print(return_all_possible_combinations('omaha-holdem',
                                           ['Ah', '2d', '3h', 'Js', 'Ac'],
                                           ['2c', '3s', 'Qd', 'Jc']))
