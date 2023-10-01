def prima(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def bil_prima(n):
    n = n + 1
    while not prima(n):
        n += 1
    return n

def generate_primes_grid(width, height, start):
    list_result = []
    current = start
    for i in range(height):
        row = []
        for j in range(width):
            current = bil_prima(current)
            row.append(current)
        list_result.append(row)
    return list_result
            print('\n')







if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """