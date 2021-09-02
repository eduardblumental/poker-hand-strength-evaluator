from itertools import combinations
from prep_functions import *
from combination_checkers import *
from rank_returners import *


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


def return_all_possible_combinations(game_type, table, hand):
    hand_list = []
    list_hand = string_hand_to_list_hand(hand)
    list_table = string_hand_to_list_hand(table)

    if game_type == 'texas-holdem':
        for combo in combinations(list_table + list_hand, 5):
            hand_list.append(''.join(combo))
    elif game_type == 'omaha-holdem':
        for table_combo in combinations(list_table, 3):
            for hand_combo in combinations(list_hand, 2):
                combo = table_combo + hand_combo
                hand_list.append(''.join(combo))

    return hand_list


def sort_hands_by_strength(list_hands):
    hand_strength_dict = {}

    for hand in list_hands:
        hand_strength_dict[hand] = main_hand_evaluator(string_hand_to_list_hand(hand))

    return sort_dict_by_value(hand_strength_dict)


def evaluate_holdem_hand(game_type, table, hand):
    possible_hands = return_all_possible_combinations(game_type, table, hand)
    hands_dict = sort_hands_by_strength(possible_hands)
    return max(list(hands_dict.values()))
