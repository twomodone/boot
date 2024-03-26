def get_median_font_size(font_sizes):
    length = len(font_sizes)
    if length == 0:
        return None
    sorted_font_sizes = sorted(font_sizes)
    if length % 2 == 0:
        return (sorted_font_sizes[length // 2] + sorted_font_sizes[length // 2 - 1]) / 2
    return sorted_font_sizes[length // 2]
