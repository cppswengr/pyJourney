primes = []                     # this will contain the primes in the end
upto = 100                      # the limit, inclusive



def get_prime_numbers(upto=10):
    """
    Return prime numbers upto the specified (and inclusive) limit
    :param upto:
    :return:
    """

    primes = []                 # this will contain the primes
    for n in range(2, upto + 1):

        for divisor in range(2, n):
            if n % divisor == 0:
                break
        else:
            primes.append(n)

    return primes

if __name__ == "__main__":
    print(get_prime_numbers(upto=100))