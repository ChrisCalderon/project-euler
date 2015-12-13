# Every number is divisible by 1
# Every number divisible by 16 is divisible by 8, 4, and 2
# Every number divisible by 9 is divisible by 3
# Every number divisible by 16*9 is divisible by 1, 2, 3, 4, 6, 8, 9, 12, 16, and 18
# Every number divisbile by 16*9*5 is divisible by 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, and 20
# it looks like the product of the highest power of each prime less than 20 is the answer
# 2^4*3^2*5^1*7*11*13*17*19
import pe3
import math

def smallest_multiple(n):
    result = 2**int(math.log(n, 2))
    result *= 3**int(math.log(n, 3))
    prime = pe3.next_prime()
    while prime < n:
        result *= prime**int(math.log(n, prime))
        prime = pe3.next_prime()
    return result

def main():
    print smallest_multiple(20)

if __name__ == '__main__':
    main()
