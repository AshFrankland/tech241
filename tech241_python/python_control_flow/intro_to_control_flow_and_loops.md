# Intro to Control Flow and Loops

### Control Flow:

Control Flow is how we tell our code what specific sections
we want it to run based on some given criteria.
This is achieved through the use of `if` statements like so:
```python
age = int(input('What is your age? '))

if age >= 18:
    print('You can watch any movie')
elif age >= 15:
    print('You can\'t watch 18 rated movies, but can watch any other movie')
elif age >= 12:
    print('You can\'t watch 18, or 15 rated movies, but can watch any other movie')
else:
    print('You can only watch U rated movies')
```
In this example the code will take some variable called `age`
and print a different response depending on what it's value is.

### Loops:

Loops are a feature in most of if not all programming languages,
in Python there are 2 different kinds:
* `for` Loops:
  * In Python `for` loops are used to iterate through something,
  like a `list`, `tuple`, or `dict`, and run some code on each
  item in them.
* `while` Loops:
  * In Python `while` loops are used to loop continuously
  until a given criteria is met (*be careful not to get
  stuck indefinitely*), it's like having a repeating if statement.