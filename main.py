# Each hand is converted into an 11-digit integer where the first digit represents the
# combination strength and 10 others represent its rank.

# Combination strengths are as follows:
# Straight Flush: 9
# Quads: 8
# Full House: 7
# Flush: 6
# Straight: 5
# Set: 4
# Two Pair: 3
# One Pair: 2
# High Card: 1


import sys
from itertools import combinations
from textwrap import wrap


def map_card_to_rank(card):
    card_dict = {
        '2': '01',
        '3': '02',
        '4': '03',
        '5': '04',
        '6': '05',
        '7': '06',
        '8': '07',
        '9': '08',
        'T': '09',
        'J': '10',
        'Q': '11',
        'K': '12',
        'A': '13'
    }

    return card_dict[card[0]]


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


def is_straight_flush(hand):
    if is_straight(hand) and is_flush(hand):
        return True


def is_quads(hand):
    pass


def is_full_house(hand):
    pass


def is_flush(hand):
    pass


def is_straight(hand):
    pass


def is_two_pair(hand):
    pass


def is_pair(hand):
    pass


def calculate_rank_score(hand):
    ranks = []

    for card in hand:
        ranks.append(map_card_to_rank(card))

    score = int(''.join(sorted(ranks, reverse=True)))
    return score


def main_hand_evaluator(hand):
    pass


if __name__ == "__main__":
    print(calculate_rank_score(['Ah', '2c', 'Js', 'Qd', '5s']))
