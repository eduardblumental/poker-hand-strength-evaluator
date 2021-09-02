from itertools import combinations


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