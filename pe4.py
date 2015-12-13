def is_palindrome(s):
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

def main():
    result = 0
    for a in range(999, 99, -1):
        for b in range(a, 99, -1):
            n = a*b
            if is_palindrome(str(n)) and n > result:
                result = n
                break
    print result

if __name__ == '__main__':
    main()
