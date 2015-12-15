def yield_next_product(ints, n):
    '''This will find the left-right and up-down products.'''
    # ints is a list
    while len(ints) > n:
        next_sequence = ints[:n]
        
        try:
            zero = next_sequence.index(0)
        except:
            zero = -1

        if zero > -1:
            ints = ints[zero + 1:]
        else:
            yield reduce(lambda a, b: a*b, next_sequence, 1)
            ints = ints[1:]

def find_diagonal_products(ints, n):
    pass

def find_largest_adjacent_product(ints, n):
    # ints is an array of arrays
    left_right = max(yield_next_product(sum(ints, []), n))
    up_down = max(yield_next_product(sum(zip(*ints), []), n))
    # the zip(*ints) transposes the array of arrays

    
    
