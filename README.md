# pytest exercises

Exercises for the pytest presentation.
Inspired on [Improve Your Python: Understanding Unit Testing](https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/).


## Setup

* Clone the repo and `cd` into it

* Setup a [conda](http://conda.pydata.org/miniconda.html) or [virtualenv](https://virtualenv.pypa.io/en/stable/userguide/) virtual environment.


#### conda virtual environment

* Install the conda virtual environment from `environment.yml`

```{bash}
$ conda env create --file environment.yml
```

* Activate the virtual environment

```{bash}
$ source activate pytest-presentation
```


#### virtualenv virtual environment

* Create a new virtual environment called `pytest-presentation`

```{bash}
$ virtualenv pytest-presentation
```

* Activate the virtual environment

```{bash}
$ source pytest-presentation/bin/activate
```

* Install the requirements from `requirements.txt`

```{bash}
$ pip install --requirement requirements.txt
```


### Using primes

* Install `primes` in editable mode (alternatively use `python setup.py develop`):

```{bash}
$ pip install --editable .
```

* Check that you can use `primes`:

```{bash}
$ python
Python 3.6.0rc1 | packaged by conda-forge | (default, Dec  7 2016, 22:57:23)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.54)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from primes import utils
>>> utils.is_prime(5)
True
```


## Exercises

The exercises are in `tests/test_utils.py`.

* Exercise 1 & 2: pytest basics
* Exercise 3: fixtures
* Exercise 4: checking for errors

Run all tests with

```{bash}
$ pytest tests/
```

Run a single test with

```{bash}
$ pytest tests/test_utils.py::test_find_next_prime
```
