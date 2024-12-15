#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x: Number of rounds to be played.
        nums: List containing the maximum number for each round.

    Returns:
        Name of the player with the most wins ("Maria" or "Ben").
        If no winner can be determined, return None.
    """
    if not nums or x < 1:
        return None

    # Precompute the prime numbers up to the maximum n in nums
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_count = [0] * (max_num + 1)

    # Create a cumulative prime count array
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        # Check the number of primes up to n
        if prime_count[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the count is odd
        else:
            ben_wins += 1  # Ben wins if the count is even

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(n):
    """
    Generates a boolean list indicating prime numbers up to n.

    Args:
        n: The upper limit of the range to check for primes.

    Returns:
        A list where True represents a prime number.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = False

    return primes
