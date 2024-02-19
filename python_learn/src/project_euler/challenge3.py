"""
Eulerproject.net - challenge 3
we will try to solve this using Pollard's rho algorithm
https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
"""
def gcd(a, b):
    """GCD algorithm using the Eucledian algorithm"""
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def g_of_x(x, n):
    """Pollard Rho requires a function (x^2 + 1)"""
    return ((x**2) + 1) % n

def pollard_rho_algorithm(n):
    """Actual Pollard Rho algorithm. returns a list containing the prime factors of the number"""
    results = []
    x = 2
    y = 2
    d = 1

    while d != n:
        x = g_of_x(x, n)
        y = g_of_x(g_of_x(y, n), n)
        d = gcd(abs(x - y), n)
        if d != 1:
            results = results + [d]
            n = n / d
    return results

def challenge_solver(n):
    """solver. will select the maximum value of the pollard rho"""
    factors = pollard_rho_algorithm(n)
    print(factors)
    return max(factors)

print(challenge_solver(600851475143))
