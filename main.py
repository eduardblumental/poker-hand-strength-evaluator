import sys
from hand_evaluators import *

# Each hand is converted into an 11-digit integer where the first digit represents the
# combination strength and 10 others represent its rank.


def main():
    with open('test-cases.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            line_list = line.replace('\n', '').split(' ')

            game_type = line_list[0]

            if game_type == 'five-card-draw':
                table = ''
                hands = line_list[1:]
                sorted_hands = sort_hands_by_strength(hands)
            else:
                table = line_list[1]
                hands = line_list[2:]
                evaluated_hands = {}

                for hand in hands:
                    evaluated_hands[hand] = evaluate_holdem_hand(game_type, table, hand)

                sorted_hands = dict(sorted(evaluated_hands.items(), key=lambda item: item[1]))

            print(f'{" ".join(sorted_hands.keys())}')


if __name__ == "__main__":
    main()
