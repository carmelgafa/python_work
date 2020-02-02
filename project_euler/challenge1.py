"""Eulerproject.net - challenge1"""

# we will solve this using arithmetic progression theory
# we know that the nth therm of the progression,
# an = a1 + (n-1)d
# the sum of the terms of the progression,
# sn = (n/2) [2a1 + (n-1)d]
# if we want to get the sum of the terms starting from the first term
# a1 = d
# the equation is further simplified to
# sn = (nd/2)(1+n)

def sum_of_n_terms(difference, threshold):
    """returns the sum of the n terms of a series having difference d"""

    # start with getting the number of terms for the first number
    number_of_terms = int(threshold / difference)

    return (number_of_terms * difference) * (1 + number_of_terms) / 2


def challenge_solver(number1, number2, threshold):
    """Solution of challenge 1 problem"""
    return (sum_of_n_terms(number1, threshold)
            + sum_of_n_terms(number2, threshold)
            - sum_of_n_terms(number1 * number2, threshold))

print(challenge_solver(3, 5, 999))
