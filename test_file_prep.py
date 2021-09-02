import random
random.seed(10)


def create_card_list():
    rank_list = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    suit_list = ['s', 'c', 'h', 'd']
    card_list = []

    for rank in rank_list:
        for suit in suit_list:
            card_list.append(rank+suit)

    return card_list


def draw_cards(card_list, number_of_cards):
    new_card_list = card_list
    draw = ''

    for _ in range(number_of_cards):
        card = random.choice(new_card_list)
        new_card_list.remove(card)
        draw += card

    return new_card_list, draw


def example_generator(game_type):
    if game_type == 'texas-holdem':
        table_card_count = 5
        hands_card_count = 2
    elif game_type == 'omaha-holdem':
        table_card_count = 5
        hands_card_count = 4
    elif game_type == 'five-card-draw':
        table_card_count = 0
        hands_card_count = 5

    card_list = create_card_list()
    new_card_list, table = draw_cards(card_list, table_card_count)

    hands = []
    for _ in range(5):
        new_card_list, hand = draw_cards(new_card_list, hands_card_count)
        hands.append(hand)

    if game_type == 'five-card-draw':
        example = game_type + ' ' + ' '.join(hands)
    else:
        example = game_type + ' ' + table + ' ' + ' '.join(hands)

    return example


def main():
    game_type_list = ['texas-holdem', 'omaha-holdem', 'five-card-draw']

    with open('test-cases.txt', 'w') as f:
        for game_type in game_type_list:
            for _ in range(1000):
                example = example_generator(game_type)
                f.write(example + '\n')


if __name__ == "__main__":
    main()