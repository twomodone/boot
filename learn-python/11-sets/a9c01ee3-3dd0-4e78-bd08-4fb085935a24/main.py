def count_vowels(text):
    vowels = "aeiouAEIOU"
    set_of_vowels = set()
    count = 0
    for char in text:
        if char in vowels:
            set_of_vowels.add(char)
            count += 1
    return count, set_of_vowels
