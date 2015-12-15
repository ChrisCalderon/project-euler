# Fibonacci numbers go 0, 1, 1, 2, 3, 5, 8, etc
#                      ^  -  -  ^  -  -  ^
# Every 3rd number is even!

def sum_even_fibs(n):
    a, b, c = 0, 1, 1
    result = 0
    while a < n:
        result += a
        a, b, c = c + b, c + c + b, c + c + c + b + b
    return result

def main():
    print sum_even_fibs(4e6)

if __name__ == '__main__':
    main()
