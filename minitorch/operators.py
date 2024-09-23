"""Collection of the core mathematical operators used throughout the code base."""

from functools import reduce
import math

# ## Task 0.1
from typing import Callable, Iterable, List

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x: float, y: float) -> float:
    return x*y

def id(a: float) -> float:
    return a

def add(a: float, b: float) -> float:
    return a+b

def neg(a: float) -> float:
    return -a

def lt(a: float, b: float) -> bool:
    return a < b

def eq(a: float, b: float) -> bool:
    return a == b

def max(a: float, b: float) -> float:
    return a if a > b else b

def is_close(a: float, b: float) -> bool:
    return (a - b) < 1e-2 if a > b else (b - a) < 1e-2 
                                    
def sigmoid(a: float) -> float:
    return 1.0/(1.0 + math.exp(-a)) if a >=0 else math.exp(a)/(1.0 + math.exp(a))

def relu(a: float) -> float:
    return max(0, a)

def log(a: float) -> float:
    return math.log(a)

def exp(a: float) -> float:
    return math.exp(a) 

def inv(a: float) -> float:
    return 1/a 

def inv_back(a: float, b: float) -> float:
    return -b/a**2 

def log_back(a: float, b: float) -> float:
    return b/a

def relu_back(a: float, b: float) -> float:
    return 0 if a < 0 else b

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists
def negList(a: List[float]) -> List[float]:
    return [-x for x in a]

def addLists(a: List[float], b: List[float]) -> List[float]:
    return [x + y for x,y in zip(a, b)]

def sum(a: List[float]) -> float:
    return reduce(lambda x, y: x + y, a) if a else 0

def prod(a: List[float]):
    return reduce(lambda x, y: x * y, a) if a else 0

# TODO: Implement for Task 0.3.
