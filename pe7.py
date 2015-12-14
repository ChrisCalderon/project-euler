import math

def sieve_of_eratosthenes(n):
    d = n/2 - 1
    nums = [True]*d
    
    for i in xrange(d):
        if nums[i]:
            step = 2*i + 3
            start = 2*i*i + 6*i + 3
            for j in xrange(start, d, step):
                nums[j] = False
    return nums

def upper_bound_for_prime(n):
    return n*math.log(n) + n*math.log(math.log(n))

def main():
    n = 10001
    #print upper_bound_for_prime(n)
    ps = sieve_of_eratosthenes(int(upper_bound_for_prime(n)))
    primes = [2*i + 3 for i, isPrime in enumerate(ps) if isPrime]

    print primes[n - 2]
    

if __name__ == '__main__':
    main()
        
