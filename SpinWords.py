import doctest


def spin_words(sentence):
    """
    Spin words in a sentence.

    >>> spin_words("Hey fellow warriors")
    'Hey wollef sroirraw'

    """
    return ' '.join(word if len(word) <= 4 else word[::-1] for word in sentence.split())


if __name__ == '__main__':
    doctest.testmod()
