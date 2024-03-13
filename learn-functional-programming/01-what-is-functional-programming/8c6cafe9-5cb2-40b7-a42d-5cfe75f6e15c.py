def get_median_font_size(font_sizes):
    sorted_list = sorted(font_sizes)
    list_length = len(sorted_list)
    if list_length == 0:
        return None
    elif list_length % 2 != 0:
        return sorted_list[list_length // 2]
    else:
        sum = sorted_list[list_length // 2] + sorted_list[(list_length // 2) - 1]
        return sum / 2
