from pe7 import sieve_of_eratosthenes

def sum_primes(n):
    result = 2
    odds = sieve_of_eratosthenes(n)
    for i, isPrime in enumerate(odds):
        if isPrime:
            result += 2*i + 3
    return result

def main():
    print sum_primes(int(2e6))

if __name__ == '__main__':
    main()
