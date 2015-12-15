def brute_force(n):
    for a in xrange(2, n+1):
        for b in xrange(a+1, n+1):
            for c in xrange(b+1, n+1):
                if a+b+c==1000 and (a*a + b*b == c*c):
                    return a*b*c
def main():
    print brute_force(1000)

if __name__ == '__main__':
    main()
