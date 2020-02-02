"""
Eulerproject.net - challenge2
we will try to solve this using a recursive function
"""

def challenge_solver():
    """start the recursion with the first two terms"""
    print(fibonacci_term(1, 0))

def fibonacci_term(current_term, previous_term):
    """function is called recursively to calculate the sum"""

    # next term is the sum of the current and previous term
    next_term = current_term + previous_term
    # if the sum is less than the value we do one more iteration
    if next_term < 4000000:
        previous_term = current_term
        current_term = next_term
        #check if the current term is even . if this case we will not add this variable to the sum
        if (current_term % 2) != 0:
            next_term = 0
        # iterate one more and add result to the current value
        return fibonacci_term(current_term, previous_term) + next_term
    else:
        # base case
        return 0

challenge_solver()
