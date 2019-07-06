
def div():
    '''
    # Program for finding numbers divisible or indivisible in a given range
    :return: Values divisible by 7 and not by 5
    :rtype: int
    '''
    a = []
    for i in range(2000,3200):
        if i%5 and not i%7:
            a.append(i)
    print(a)
    print(" Testing this out from Pycharm. ")
