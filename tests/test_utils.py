import pytest
from primes.utils import is_prime
from primes.utils import find_next_prime
from primes.utils import load_next_prime


"""Example unit test."""


def test_find_next_prime():
    """Create a unit test with a simple assert statement."""
    assert find_next_prime(4) == 5


"""Grouping unit tests."""


class TestIsPrime(object):
    """Tests can be grouped in a class.

    Classes support xunit-style setups:
    http://doc.pytest.org/en/latest/xunit_setup.html

    Run all tests in the class with:
    >>>pytest tests/tests.py::TestIsPrime
    """

    def test_prime(self):
        """Create a unit test with a simple assert statement."""
        assert is_prime(3) is True

    def test_one(self):
        """Exercise 1: Adjust is_prime() to let this test pass."""
        assert is_prime(1) is False

    def test_zero(self):
        """Exercise 1: Adjust is_prime() to let this test pass."""
        assert is_prime(0) is False

    def test_negative(self):
        """Exercise 2: Test that negative numbers result in False and adjust
        is_prime().
        """
        pass


"""Fixtures."""


@pytest.fixture
def give_three():
    """Fixtures provide more and better features than the setup & teardown
     methods: http://doc.pytest.org/en/latest/fixture.html

    Define fixtures with pytest.fixtures. Scope fixtures by giving it
    arguments (e.g. pytest.fixture('session')).
    """
    return 3


def test_float(give_three):
    """Use fixture give_three."""
    assert is_prime(give_three) is True


def test_load_next_prime_single(tmpdir):
    """Built-in fixtures.

    tmpdir is a fixture giving us a temporary directory.
    """
    p = tmpdir.mkdir('sub').join('file.txt')
    p.write(5)
    assert load_next_prime(str(p)) == 7


def test_load_next_prime_multiple(tmpdir):
    """Exercise 4: checking for exceptions.

    Use pytest.raises to catch the RunTimeError raised when a file contains
    multiple numbers.
    """
    p = tmpdir.mkdir('sub').join('file.txt')
    p.write('5\n7')
    assert p.read() == '5\n7'  # When can read the file again.
