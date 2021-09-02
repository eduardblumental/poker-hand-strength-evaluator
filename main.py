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
                hands = line_list[1:]

                sorted_hands = sort_hands_by_strength(hands)

                for key in sorted_hands:
                    print(key, sorted_hands[key])
            else:
                table = line_list[1]
                hands = line_list[2:]


if __name__ == "__main__":
    main()
