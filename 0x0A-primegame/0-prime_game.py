#!/usr/bin/python3

def isWinner(x, nums):
    """Determines the winner of the prime game for x rounds"""
    if not nums or x < 1:
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes to precompute number of primes up to max_n
    is_prime = [False, False] + [True for _ in range(2, max_n + 1)]
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Precompute the number of primes up to i
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + int(is_prime[i])

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
