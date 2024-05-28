#!/usr/bin/python3
"""Prime Game Module
"""


def isWinner(x, nums):
    """Get the winner
    """
    def sieve_of_eratosthenes(max_num):
        """Return range of prime numbers up to 'max_num'
        """
        primes = [True] * (max_num + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= max_num:
            if primes[p]:
                for i in range(p * p, max_num + 1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(max_num + 1) if primes[p]]

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    def play_game(n):
        """Simulate playing the game for n rounds
        """
        prime_set = set(primes)
        primes_remaining = [p for p in primes if p <= n]

        turn = 0  # 0 for Maria, 1 for Ben
        while primes_remaining:
            current_prime = primes_remaining[0]
            primes_remaining = [
                    p for p in primes_remaining if p % current_prime != 0]
            turn = 1 - turn

        # 0 if Ben wins (Maria has no move),
        # 1 if Maria wins (Ben has no move)
        return turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            winner = play_game(n)
            if winner == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None