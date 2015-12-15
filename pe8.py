import sys

def yield_next_product(ints, n):
    # ints is a string
    while len(ints) > n:
        next_sequence = ints[:n]
        zero = next_sequence.find('0')
        if zero > -1:
            ints = ints[zero + 1:]
        else:
            yield reduce(lambda a, b: a*int(b), next_sequence, 1)
            ints = ints[1:]

def main():
    n = int(sys.argv[1])
    ints = ''.join(open('pe8.txt').read().split('\n'))
    print max(yield_next_product(ints, n))

if __name__ == '__main__':
    main()
