def find_quads_ranks(combo_dict):
    for key in combo_dict:
        if combo_dict[key] == 4:
            quads_rank = key
        elif combo_dict[key] == 1:
            rank = key

    return quads_rank, rank


def find_full_house_ranks(combo_dict):
    for key in combo_dict:
        if combo_dict[key] == 3:
            house_rank = key
        elif combo_dict[key] == 2:
            full_rank = key

    return house_rank, full_rank


def find_two_pair_ranks(combo_dict):
    two_pair_list = []

    for key in combo_dict:
        if combo_dict[key] == 2:
            two_pair_list.append(key)

    return two_pair_list[1], two_pair_list[0]


def find_one_pair_ranks(combo_dict):
    for key in combo_dict:
        if combo_dict[key] == 2:
            return key
