def remove_duplicates(spells):
    set_of_spells = set()
    
    for spell in spells:
        set_of_spells.add(spell)
    unique_spells = []
    
    for spell in set_of_spells:
        unique_spells.append(spell)
    return unique_spells
