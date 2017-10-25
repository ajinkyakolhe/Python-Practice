'''
# Program for finding factorial for a number
'''
def fact_me(x):
    '''
    :param x: input value
    :type x: int
    :return: the factorial value
    :rtype: int
    '''
    x = int(input("Enter the number of which you have to find a factorial"))
    n = 1
    for i in range(1,x+1):
        n = n*i
    print(n)


# Optimal solution:
def fact(x):
    '''
    :param x: input value
    :type x: int
    :return: the factorial value
    :rtype: int
    '''
    return x*fact(x-1) if x > 1 else 1

