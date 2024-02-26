def calculate_experience_points(level):
    xp = 0
    for i in range(1, level + 1):
        xp += (i - 1) * 5
    return xp
