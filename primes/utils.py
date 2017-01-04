def is_prime(number):
    """Return True if *number* is prime."""
    for element in range(2, number):  # Don't use 0 and 1
        if number % element == 0:
            return False
    return True


def find_next_prime(number):
    """Find the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            return index


def load_next_prime(file):
    with open(file, 'r') as f:
        contents = f.read().split()
    if len(contents) != 1:
        raise RuntimeError("Too many elements")
    return find_next_prime(int(contents[0]))
