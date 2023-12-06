def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the remainder of the division in the range [2, P).
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


help(is_prime)
