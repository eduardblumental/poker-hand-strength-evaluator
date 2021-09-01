from prep_functions import *


def is_straight_flush(hand):
    if is_straight(hand) and is_flush(hand):
        return True


def is_quads(combo_dict):
    for key in combo_dict:
        if combo_dict[key] == 4:
            return True

    return False


def is_full_house(hand):
    pass


def is_flush(hand):
    pass


def is_straight(hand):
    pass


def is_two_pair(hand):
    pass


def is_pair(hand):
    pass