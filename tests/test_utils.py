from primes.utils import is_prime
from primes.utils import find_next_prime


def test_is_prime():
    assert is_prime(3) is True


def test_find_next_prime():
    assert find_next_prime(4) == 5
