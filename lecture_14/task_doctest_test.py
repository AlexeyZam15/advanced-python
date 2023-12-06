def say(string, multiplier=2, separator=" "):
    """
    >>> say('Hello')
    Hello Hello
    >>> say('Hi', 5)
    Hi Hi Hi Hi Hi
    >>> say('cat', 3, '(=^.^=)')
    cat(=^.^=)cat(=^.^=)cat
    """
    print(f"{separator}".join([string for _ in range(multiplier)]))


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
