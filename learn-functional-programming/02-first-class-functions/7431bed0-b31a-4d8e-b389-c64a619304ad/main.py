import functools


def accumulate(doc, sentence):
    return f"{doc}. {sentence}"


def accumulate_first_sentences(sentences, n):
    sentences_len = len(sentences)
    if (sentences_len == 0 or n <= 0):
        return ""
    return functools.reduce(accumulate, sentences[:n]) + "."
