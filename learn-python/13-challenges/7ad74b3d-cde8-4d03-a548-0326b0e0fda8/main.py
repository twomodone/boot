def join_strings(strings):
    new_string = ""
    for i in range(0, len(strings)):
        if i == len(strings) - 1:
            new_string += strings[i]
        else:
            new_string += f"{strings[i]},"
    return new_string
