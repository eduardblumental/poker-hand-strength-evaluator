def find_quads_ranks(combo_dict):
    for rank in combo_dict:
        if combo_dict[rank] == 4:
            quads_rank = rank
        elif combo_dict[rank] == 1:
            remainder_rank = rank

    return quads_rank, remainder_rank


def find_full_house_ranks(combo_dict):
    for rank in combo_dict:
        if combo_dict[rank] == 3:
            house_rank = rank
        elif combo_dict[rank] == 2:
            full_rank = rank

    return house_rank, full_rank


def find_set_ranks(combo_dict):
    remainder_ranks = []

    for key in combo_dict:
        if combo_dict[key] == 3:
            set_rank = key
        elif combo_dict[key] == 1:
            remainder_ranks.append(key)

    return set_rank, remainder_ranks


def find_two_pair_ranks(combo_dict):
    two_pair_list = []

    for key in combo_dict:
        if combo_dict[key] == 2:
            two_pair_list.append(key)
        elif combo_dict[key] == 1:
            remainder_rank = key

    return two_pair_list[1], two_pair_list[0], remainder_rank


def find_one_pair_ranks(combo_dict):
    remainder_ranks = []

    for key in combo_dict:
        if combo_dict[key] == 2:
            pair_rank = key
        elif combo_dict[key] == 1:
            remainder_ranks.append(key)

    return pair_rank, remainder_ranks
