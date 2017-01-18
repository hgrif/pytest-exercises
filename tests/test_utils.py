import pytest
from primes.utils import is_prime
from primes.utils import find_next_prime
from primes.utils import load_next_prime


"""Example unit test.

Creating a unit test is as simple as creating a function beginning with
'test_' that contains an assert.
"""


def test_find_next_prime():
    """Create a unit test with a simple assert statement."""
    assert find_next_prime(4) == 5


"""Grouping unit tests.

Sometimes it makes sense to group unit tests: for instance, you want to keep
all unit tests for a function together. Tests can be grouped in a file, but
also in a class.

Unit tests in class can share fixture-like methods that are called everytime
a method is called. More info on these so-called xunit-style setups:
http://doc.pytest.org/en/latest/xunit_setup.html


Run all tests in the class with:
>>>pytest tests/tests.py::TestIsPrime
"""


class TestIsPrime(object):
    """Tests can be grouped in a class."""

    def test_prime(self):
        """Create a unit test as a method with a simple assert statement."""
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
        assert is_prime(-1) is False


"""Fixtures.

Fixtures provide more and better features than the setup & teardown methods:
http://doc.pytest.org/en/latest/fixture.html

Define fixtures with the decorator @pytest.fixture. Scope fixtures by giving it
arguments (e.g. pytest.fixture('session')).

Use a fixture by specifying it as an argument for your test function.
"""


@pytest.fixture
def give_three():
    """Fixture that returns the integer 3."""
    return 3


def test_float(give_three):
    """Use fixture give_three by specifying it as an argument."""
    assert is_prime(give_three) is True


"""Built-in fixtures.

pytest also ships with some common fixtures so you don't have create these
yourself.

An example is tmp_dir that creates a temporary directory. Just put it as an
argument for your function and you'll get it for free!
http://doc.pytest.org/en/latest/tmpdir.html
"""


def test_load_next_prime_single(tmpdir):
    """tmpdir is a fixture build in pytests that gives us a temporary
    directory.

    Exercise 3:
    * Use tmpdir to create a directory 'sub' with a file called 'file.txt'
    * Write '5' to the file
    * Make sure the unit test passes

    More info: http://doc.pytest.org/en/latest/tmpdir.html
    """
    p = tmpdir.mkdir('sub').join('file.txt')
    p.write('5')
    assert load_next_prime(str(p)) == 7


"""Exceptions.

pytest can also test that your functions errors out the way you want to.
"""


def test_load_next_prime_multiple(tmpdir):
    """Exercise 4: checking for exceptions.

    Use pytest.raises to check that a RunTimeError is raised when a file
    contains multiple numbers.
    """
    p = tmpdir.mkdir('sub').join('file.txt')
    p.write('5\n7')
    assert p.read() == '5\n7'  # Our file should contain two numbers.
    with pytest.raises(RuntimeError):
        load_next_prime(str(p))
