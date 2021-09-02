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
        '2': '02',
        '3': '03',
        '4': '04',
        '5': '05',
        '6': '06',
        '7': '07',
        '8': '08',
        '9': '09',
        'T': '10',
        'J': '11',
        'Q': '12',
        'K': '13',
        'A': '14'
    }

    return card_dict[card[0]]


def string_hand_to_list_hand(string_hand):
    return wrap(string_hand, 2)


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
        '13': 0,
        '14': 0
    }

    for card in hand:
        card_rank = map_card_to_rank(card)
        combo_dict[card_rank] += 1

    return combo_dict


def calculate_rank_score(hand):
    ranks = []

    for card in hand:
        if card.isnumeric():
            ranks.append(card)
        else:
            ranks.append(map_card_to_rank(card))

    score = ''.join(sorted(ranks, reverse=True))
    return score


def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: (item[1], item[0])))
