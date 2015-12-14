from pe1 import triangle

def sum_squares(n):
    return triangle(n)*(2*n + 1)/3

def square_sum(n):
    return triangle(n)**2

def main():
    n = 100
    print square_sum(n) - sum_squares(n)

if __name__ == '__main__':
    main()
