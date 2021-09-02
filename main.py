import sys
from hand_evaluators import *

# Each hand is converted into an 11-digit integer where the first digit represents the
# combination strength and 10 others represent its rank.


def line_to_sorted_hands(line):
    line_list = line.replace('\n', '').split(' ')
    game_type = line_list[0]

    if game_type == 'five-card-draw':
        hands = line_list[1:]
        sorted_hands = sort_hands_by_strength(hands)
    else:
        table = line_list[1]
        hands = line_list[2:]
        evaluated_hands = {}

        for hand in hands:
            evaluated_hands[hand] = evaluate_holdem_hand(game_type, table, hand)

        sorted_hands = sort_dict_by_value(evaluated_hands)

    return sorted_hands


def main():
    lines = sys.stdin

    for line in lines:
        try:
            sorted_hands = line_to_sorted_hands(line)
            output_line = ''

            previous_strength = 0
            for key in sorted_hands:
                if sorted_hands[key] == previous_strength:
                    output_line += '=' + key
                else:
                    output_line += ' ' + key
                previous_strength = sorted_hands[key]

            output_line = output_line.strip()
            print(output_line)
        except:
            print('Error')


if __name__ == "__main__":
    main()
