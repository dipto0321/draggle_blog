import string


def slug_generator(slug_str):
    return slug_str.translate(str.maketrans(" ", "-", string.punctuation)).lower()
