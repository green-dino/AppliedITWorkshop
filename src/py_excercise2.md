Exercise 1: Exploring Type Conversion Functions
Convert Between Types:
Convert an integer to a string: str(123)
Convert a string to an integer: int('123')
Convert a string to a float: float('123.45')
Check Types:
Use type(123) to check the type of an integer.
Use type('123') to check the type of a string.
Use type(123.45) to check the type of a float.
Exercise 2: Using len and abs
Length of Collections:
Find the length of a string: len('Hello, World!')
Find the length of a list: len([1, 2, 3, 4, 5])
Find the length of a dictionary: len({'a': 1, 'b': 2, 'c': 3})
Absolute Values:
Find the absolute value of a positive number: abs(10)
Find the absolute value of a negative number: abs(-10)
Exercise 3: Using min and max
Find Minimum and Maximum Values:
Find the minimum value in a list: min([3, 1, 4, 1, 5, 9])
Find the maximum value in a list: max([3, 1, 4, 1, 5, 9])
Use with Multiple Arguments:
Find the minimum of multiple arguments: min(3, 1, 4)
Find the maximum of multiple arguments: max(3, 1, 4)
Exercise 4: Using sum and round
Sum of Values:
Calculate the sum of a list of numbers: sum([1, 2, 3, 4, 5])
Calculate the sum of a tuple of numbers: sum((1, 2, 3, 4, 5))
Rounding Numbers:
Round a float to the nearest integer: round(3.14)
Round a float to two decimal places: round(3.14159, 2)
Exercise 5: Using enumerate and zip
Enumerate Function:
Create a list: fruits = ['apple', 'banana', 'cherry']
Use enumerate to get index-value pairs: list(enumerate(fruits))
Zip Function:
Create two lists: names = ['Alice', 'Bob', 'Charlie'], ages = [25, 30, 35]
Use zip to combine lists into pairs: list(zip(names, ages))
Exercise 6: Using sorted and reversed
Sorting Collections:
Sort a list of numbers: sorted([3, 1, 4, 1, 5, 9])
Sort a list of strings: sorted(['apple', 'banana', 'cherry'])
Reversing Collections:
Reverse a list of numbers: list(reversed([3, 1, 4, 1, 5, 9]))
Reverse a string: ''.join(reversed('hello'))
Exercise 7: Using all and any
Check All Elements:
Check if all elements are true: all([True, True, True])
Check if all elements are non-zero: all([1, 2, 3, 0])
Check Any Element:
Check if any element is true: any([False, True, False])
Check if any element is non-zero: any([0, 0, 3, 0])
Exercise 8: Using map and filter
Map Function:
Create a list of numbers: numbers = [1, 2, 3, 4, 5]
Use map to apply a function to each element: list(map(lambda x: x * 2, numbers))
Filter Function:
Create a list of numbers: numbers = [1, 2, 3, 4, 5]
Use filter to filter elements: list(filter(lambda x: x % 2 == 0, numbers))
Exercise 9: Using isinstance and issubclass
Check Instances:
Check if an object is an instance of a type: isinstance(123, int)
Check if an object is an instance of multiple types: isinstance('hello', (int, str))
Check Subclasses:
Define a class: class Animal: pass
Define a subclass: class Dog(Animal): pass
Check if a class is a subclass: issubclass(Dog, Animal)
Exercise 10: Using dir and vars
Explore Attributes:
Use dir to list attributes of an object: dir([]) for a list.
Use dir to list attributes of a module: import math; dir(math)
View Object’s __dict__:
Define a simple class with attributes:
python
Copy code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
Create an instance and view its attributes: p = Person('Alice', 25); vars(p)