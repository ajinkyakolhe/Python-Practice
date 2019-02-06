# fibonacci.py

# This code is used to demonstrate substitution trace in a more complicated
# example. It is good practice for understanding recursion, but it is not
# an ideal solution for computing Fibonacci numbers.

def fibo( n ):
    """ Compute a number in the Fibonacci series.
        :param n: the ordinal value; we are computing the "nth" in the series.
        :return: the nth value in the fibonacci series
        :pre: n >= 0
    """
    assert n >= 0, "fibo: Argument must be a natural number."
    if n < 2:
        result = n
    else:
        result = fibo( n - 2 ) + fibo( n - 1 )
    return result

def fibo2( n ):
    return fibo2_rec( 0, 1, n )

def fibo2_rec( prev, curr, n ):
    assert n >= 0, "fibo2: Argument must be a natural number."
    if n == 0:
        result = 0
    elif n == 1:
        result = curr
    else:
        result = fibo2_rec( curr, prev+curr, n-1 )
    return result

def fibo3( n ):
    assert n >= 0, "fibo3: Argument must be a natural number."
    prev = 0
    curr = 1
    while n > 1:
        prev_temp = curr
        curr = prev + curr
        prev = prev_temp
        n = n - 1
    if n == 0:
        result = 0
    else:
        result = curr
    return result

def test():
    for i in range( 100 ):
        print( "fibo(" + str( i ) + ") = " + str( fibo3( i ) ) )

if __name__ == "__main__":
    test()
