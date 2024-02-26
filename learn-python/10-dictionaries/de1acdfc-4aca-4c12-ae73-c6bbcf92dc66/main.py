def get_most_common_enemy(enemies_dict):
    if len(enemies_dict) == 0:
        return None
    else:
        max_so_far = float("-inf")
        enemy_name = None
        for enemy in enemies_dict:
            count = enemies_dict[enemy]
            if count > max_so_far:
                max_so_far = count
                enemy_name = enemy
        return enemy_name
