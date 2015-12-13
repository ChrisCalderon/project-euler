# Fibonacci numbers go 0, 1, 1, 2, 3, 5, 8, etc
#                      ^  -  -  ^  -  -  ^
# Every 3rd number is even!

MAX = 4e6
a, b, c = 0, 1, 1
result = 0
while (c + b) < MAX:
    result += c + b
    b, c = c + c + b, c + c + c + b + b # notice that only c and b matter...
print result
