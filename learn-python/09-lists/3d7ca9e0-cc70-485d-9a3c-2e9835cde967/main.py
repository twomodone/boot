def reverse_array(items):
    reversed_array = []
    for i in range(len(items) - 1, -1, -1):
        reversed_array.append(items[i])
    return reversed_array
