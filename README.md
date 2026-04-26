# asgmt-4-visualization-with-modern-data-science

Assignment 4: Visualization with Modern Data Science 2026

## 01. Define a function `check_data_type()` which returns the data type of input in a string format.

```python
def check_data_type(x) -> str:
    """
    >>> check_data_type(1)
    'int'
    >>> check_data_type(1.0)
    'float'
    >>> check_data_type(False)
    'bool'
    >>> check_data_type(True)
    'bool'
    >>> check_data_type('5566')
    'str'
    >>> check_data_type(None)
    'NoneType'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `check_data_structure()` which returns the data structure of input in a string format.

```python
def check_data_structure(x) -> str:
    """
    >>> check_data_structure([2, 3, 5, 7, 11])
    'list'
    >>> check_data_structure((2, 3, 5, 7, 11))
    'tuple'
    >>> check_data_structure({'0': 2, '1': 3, '2': 5, '3': 7, '4': 11})
    'dict'
    >>> check_data_structure({2, 3, 5, 7, 11})
    'set'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `retrieve_first_and_last_elements()` which returns the first and the last elements of a given `list`.

```python
def retrieve_first_and_last_elements(x: list) -> tuple:
    """
    >>> retrieve_first_and_last_elements([2, 3, 5])
    (2, 5)
    >>> retrieve_first_and_last_elements([2, 3, 5, 7])
    (2, 7)
    >>> retrieve_first_and_last_elements(["Frieren", "Heiter", "Eisen", "Himmel"])
    ('Frieren', 'Himmel')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `retrieve_middle_elements()` which returns the middle elements of a given `list`.

```python
def retrieve_middle_elements(x: list):
    """
    >>> retrieve_middle_elements([2, 3, 5])
    3
    >>> retrieve_middle_elements([2, 3, 5, 7])
    (3, 5)
    >>> retrieve_middle_elements([2, 3, 5, 7, 11])
    5
    >>> retrieve_middle_elements([2, 3, 5, 7, 11, 13])
    (5, 7)
    >>> retrieve_middle_elements(["Heiter", "Frieren", "Himmel", "Eisen"])
    ('Frieren', 'Himmel')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `median()` which returns the median value of a given `list`.

Source: <https://en.wikipedia.org/wiki/Median>

```python
def median(x: list):
    """
    >>> median([2, 3, 5, 7, 11])
    5
    >>> median([2, 3, 5, 7, 11, 13])
    6.0
    >>> median([11, 13, 17, 2, 3, 5, 7])
    7
    >>> median([7, 11, 13, 17, 19, 2, 3, 5])
    9.0
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `collect_divisors()` which returns all positive divisors of a given `int`.

Source: <https://en.wikipedia.org/wiki/Divisor>


```python
def collect_divisors(x: int) -> set:
    """
    >>> collect_divisors(1)
    {1}
    >>> collect_divisors(2)
    {1, 2}
    >>> collect_divisors(3)
    {1, 3}
    >>> collect_divisors(4)
    {1, 2, 4}
    >>> collect_divisors(5)
    {1, 5}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `is_prime()` which returns whether a given `int` is a prime number or not.

Source: <https://en.wikipedia.org/wiki/Prime_number>

```python
def is_prime(x: int) -> bool:
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `list_first_n_prime_numbers()` which returns the first `n` prime numbers in a `list`.

```python
def list_first_n_prime_numbers(n: int) -> list:
    """
    >>> list_first_n_prime_numbers(5)
    [2, 3, 5, 7, 11]
    >>> list_first_n_prime_numbers(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> list_first_n_prime_numbers(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `swap_vowel_case()` which converts the input from upper-cased to lower-cased, and from lower-cased to upper-cased, respectively if the input is a vowel.

```python
def swap_vowel_case(x: str) -> str:
    """
    >>> swap_vowel_case('a')
    'A'
    >>> swap_vowel_case('b')
    'b'
    >>> swap_vowel_case('c')
    'c'
    >>> swap_vowel_case('d')
    'd'
    >>> swap_vowel_case('e')
    'E'
    >>> swap_vowel_case('A')
    'a'
    >>> swap_vowel_case('B')
    'B'
    >>> swap_vowel_case('C')
    'C'
    >>> swap_vowel_case('D')
    'D'
    >>> swap_vowel_case('E')
    'e'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `swap_vowels_case_in_word()` which converts the vowels in a word from upper-cased to lower-cased, and from lower-cased to upper-cased, respectively.

```python
def swap_vowels_case_in_word(x: str) -> str:
    """
    >>> swap_vowels_case_in_word('Frieren')
    'FrIErEn'
    >>> swap_vowels_case_in_word('Himmel')
    'HImmEl'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```