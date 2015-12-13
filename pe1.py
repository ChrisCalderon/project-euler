# The sum of the multiples of 3 and 5 below 1000 is
# 3*sum of numbers from 1 to 1000/3 (333) plus
# 5*sum of numbers from 1 to 1000/5 (200) minus
# 15*sum of numbers from 1 to 1000/15

def triangle(n):
    '''Returns the n-th triangle number.'''
    # Triangle numbers are:
    # * 1
    #
    # *
    # ** 3
    #
    # *
    # **
    # *** 6
    #
    # etc.
    return n*(n+1)/2

def main():
    MAX = 1000
    print 3*triangle((MAX - 1)/3) + 5*triangle((MAX - 1)/5) - 15*triangle((MAX - 1)/15)

if __name__ == '__main__':
    main()
