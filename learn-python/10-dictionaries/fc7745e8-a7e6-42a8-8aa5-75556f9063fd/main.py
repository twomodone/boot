def count_enemies(enemy_names):
    enemies = {}
    for name in enemy_names:
        if name in enemies:
            enemies[name] += 1
        else:
            enemies[name] = 1
    return enemies
