def transpose(matrix):
    return map(list, zip(*matrix))

def yield_horizontal_products(ints, n):
    for i in range(len(ints)):
        for j in range(len(ints) - n + 1):
            product = 1
            for k in range(n):
                if ints[i][j+k]:
                    product *= ints[i][j+k]
                else:
                    break
            else:
                yield product
        print ints[i][j]

def yield_diagonal_products(ints, n):
    for i in range(len(ints) - n + 1):
        for j in range(len(ints) - n + 1):
            product = 1
            for k in range(n):
                if ints[i+k][j+k]:
                    product *= ints[i+k][j+k]
                else:
                    break
            else:
                yield product
        print ints[i][j]
                
def find_largest_adjacent_product(ints, n):
    # ints is an array of arrays
    print 'left'
    left = max(yield_horizontal_products(ints, n))
    print 'right'
    right = max(yield_horizontal_products(map(lambda row: list(reversed(row)),
                                              ints),
                                          n))
    print 'up'
    up = max(yield_horizontal_products(transpose(ints), n))
    print 'down'
    down = max(yield_horizontal_products(map(lambda row: list(reversed(row)),
                                             transpose(ints)),
                                         n))
    print 'diagonal'
    diagonal = max(yield_diagonal_products(ints, n))
    return max((left, right, up, down, diagonal))
    # the zip(*ints) transposes the array of arrays
    
def main():
    intsFile = open('pe11.txt')
    ints = map(lambda line: map(int, line.split(' ')),
               filter(None,
                      intsFile.read().split('\n')))
    print ints
    n = 4
    print find_largest_adjacent_product(ints, n)
    
if __name__ == '__main__':
    main()
