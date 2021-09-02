import sys
from prep_functions import *
from combination_checkers import *
from rank_returners import *

# Each hand is converted into an 11-digit integer where the first digit represents the
# combination strength and 10 others represent its rank.


def main_hand_evaluator(hand):
    combo_dict = create_combo_dict(hand)

    if is_straight_flush(hand, combo_dict):
        if is_baby_ace(combo_dict):
            hand_strength = combo_strength_dict['straight_flush'] + '0504030201'
        else:
            hand_strength = combo_strength_dict['straight_flush'] + calculate_rank_score(hand)
    elif is_quads(combo_dict):
        quads_rank, rank = find_quads_ranks(combo_dict)
        hand_strength = combo_strength_dict['quads'] + quads_rank * 4 + rank
    elif is_full_house(combo_dict):
        house_rank, full_rank = find_full_house_ranks(combo_dict)
        hand_strength = combo_strength_dict['full_house'] + house_rank * 3 + full_rank * 2
    elif is_flush(hand):
        hand_strength = combo_strength_dict['flush'] + calculate_rank_score(hand)
    elif is_straight(combo_dict):
        if is_baby_ace(combo_dict):
            hand_strength = combo_strength_dict['straight'] + '0504030201'
        else:
            hand_strength = combo_strength_dict['straight'] + calculate_rank_score(hand)
    elif is_set(combo_dict):
        set_rank, remainder_ranks = find_set_ranks(combo_dict)
        hand_strength = combo_strength_dict['set'] + set_rank * 3 + calculate_rank_score(remainder_ranks)
    elif is_two_pair(combo_dict):
        high_pair, low_pair, remainder_rank = find_two_pair_ranks(combo_dict)
        hand_strength = combo_strength_dict['two_pair'] + high_pair * 2 + low_pair * 2 + remainder_rank
    elif is_one_pair(combo_dict):
        pair, remainder_ranks = find_one_pair_ranks(combo_dict)
        hand_strength = combo_strength_dict['one_pair'] + pair * 2 + calculate_rank_score(remainder_ranks)
    else:
        hand_strength = combo_strength_dict['high_card'] + calculate_rank_score(hand)

    return int(hand_strength)


if __name__ == "__main__":
    file = sys.stdin
    for line in file:
        print(line)
    print(main_hand_evaluator(['4c', '5c', '2c', '3c', 'Ac']))
