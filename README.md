# Pytest Presentation


## Setup

* Clone the repo and `cd` into it.

* Install the [conda](http://conda.pydata.org/miniconda.html) virtual environment

```{bash}
$ conda env create -f environment.yml
```

* Activate the virtual environment

```{bash}
$ source activate pytest-presentation
```

* Install `primes` in editable mode (alternatively use `python setup.py develop`):

```{bash}
$ pip install --editable .
```

* Use `primes`

```{bash}
$ python
Python 3.6.0rc1 | packaged by conda-forge | (default, Dec  7 2016, 22:57:23)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.54)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from primes import utils
>>> utils.is_prime(5)
True
```

