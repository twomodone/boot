def filter_messages(messages):
    filtered_messages = []
    count_of_words_removed = []

    for message in messages:
        words = message.split()
        non_bad_words = []
        counter = 0
        for word in words:
            if word == "dang":
                counter += 1
            else:
                non_bad_words.append(word)
        new_message = " ".join(non_bad_words)
        filtered_messages.append(new_message)
        count_of_words_removed.append(counter)

    return filtered_messages, count_of_words_removed
