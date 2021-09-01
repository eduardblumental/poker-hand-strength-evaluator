def is_straight_flush(hand, combo_dict):
    if is_straight(combo_dict) and is_flush(hand):
        return True


def is_quads(combo_dict):
    for rank in combo_dict:
        if combo_dict[rank] == 4:
            return True

    return False


def is_full_house(combo_dict):
    for rank1 in combo_dict:
        if combo_dict[rank1] == 3:
            for rank2 in combo_dict:
                if combo_dict[rank2] == 2:
                    return True

    return False


def is_flush(hand):
    suits = ''

    for card in hand:
        suits += card[1]

    if len(set(suits)) == 1:
        return True
    else:
        return False


def is_straight(combo_dict):
    for rank in combo_dict:
        pass


def is_set(combo_dict):
    for rank in combo_dict:
        if combo_dict[rank] == 3:
            return True

    return False


def is_two_pair(combo_dict):
    for rank1 in combo_dict:
        if combo_dict[rank1] == 2:
            for rank2 in combo_dict:
                if rank2 == rank1:
                    continue
                if combo_dict[rank2] == 2:
                    return True

    return False


def is_pair(combo_dict):
    for rank in combo_dict:
        if combo_dict[rank] == 2:
            return True

    return False