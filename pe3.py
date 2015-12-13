PRIMES = [3]

def next_prime():
    num = PRIMES[-1] + 2 # odd + 2 is the next odd, don't check evens for primality
    is_prime = False
    while True:
        lim = num**0.5 # don't check for prime factors larger than this
        for p in PRIMES:
            if p > lim:
                is_prime = True
                break
            elif num%p==0:
                is_prime = False
                break
            else:
                continue
        if is_prime:
            PRIMES.append(num)
            return num
        else:
            num += 2

def largest_prime_factor(n):
    largest = 2
    while not n&1:
        n >> 1 # divide out the twos
    if n%3 == 0:
        largest = 3
        while n%3==0:
            n /= 3
    while n > 1:
        p = next_prime()
        if n%p==0:
            largest = p
            while n%p==0:
                n /= p
    return largest

def main():
    # testing prime finding
    # print 2, 3,
    # for i in range(100):
    #     print next_prime(),
    print largest_prime_factor(600851475143)

if __name__ == '__main__':
    main()
