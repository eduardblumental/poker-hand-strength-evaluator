import sys
from itertools import combinations
from textwrap import wrap
from prep_functions import *
from combination_checkers import *
from rank_returners import *

# Each hand is converted into an 11-digit integer where the first digit represents the
# combination strength and 10 others represent its rank.


def calculate_rank_score(hand):
    ranks = []

    for card in hand:
        ranks.append(map_card_to_rank(card))

    score = ''.join(sorted(ranks, reverse=True))
    return score


def main_hand_evaluator(hand):
    combo_dict = create_combo_dict(hand)

    if is_quads(combo_dict):
        quads_rank, rank = find_quads_ranks(hand)
        hand_strength = combo_strength_dict['quads'] + calculate_rank_score(quads_rank * 4) + calculate_rank_score(rank)
    else:
        hand_strength = combo_strength_dict['high_card'] + calculate_rank_score(hand)

    return hand_strength


if __name__ == "__main__":
    print(main_hand_evaluator(['Ah', '2c', 'Js', 'Qd', '5s']))
