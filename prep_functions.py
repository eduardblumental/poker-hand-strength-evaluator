from itertools import combinations
from textwrap import wrap


combo_strength_dict = {'straight_flush': '9',
                    'quads': '8',
                    'full_house': '7',
                    'flush': '6',
                    'straight': '5',
                    'set': '4',
                    'two_pair': '3',
                    'one_pair': '2',
                    'high_card': '1'}


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


def create_combo_dict(hand):
    combo_dict = {
        '01': 0,
        '02': 0,
        '03': 0,
        '04': 0,
        '05': 0,
        '06': 0,
        '07': 0,
        '08': 0,
        '09': 0,
        '10': 0,
        '11': 0,
        '12': 0,
        '13': 0
    }

    for card in hand:
        card_rank = map_card_to_rank(card)
        combo_dict[card_rank] += 1

    return combo_dict


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