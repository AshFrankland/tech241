# Intro to Python

As with any good Python introduction, we learned how to make a virtual environment in PyCharm,
and inside our venv we put a hello_world program containing just `print('Hello World!')`

Once we had that all set up we began by looking into variables.
We started by looking at basic assignment which looks like this:

```python
a = 1  # int
b = 2  # int
c = 3.5  # float
hi = 'hello world!'  # string
```
After we understood variables, we looked at operations you can perform on them,
such as:
* Arithmetic Operations
  * Addition `+`
  * Subtraction `-`
  * Division `/`
  * Multiplication `*`
  * Modulo `%`
* Comparison Operations
  * Equal to `==`
  * Not Equal to `!=`
  * Greater than `>`
  * Less than `<`
  * Greater than or Equal to `>=`
  * Less than or Equal to `<=`

Next we discussed the different [Data Types][1].  
These included:
* Numbers
  * Integer `int`
  * Float `float`
  * Complex `complex`
  * ~~Long Integer `long`~~ _no longer supported but worth knowing about_
* Strings `str`
* Boolean `bool`
* None `NoneType`

Armed with our new Python skills, we were tasked in writing a small program
which would take inputs from a user,
and return their answers in a nicely formatted string.

Here is my program:

```python
name = input('What is your name? ')
age = input('How old are you? ')
dob = input('When were you born? ')
address = input('Where do you live? ')

print(f'\nHi {name},\n'
      f'you are {age} years old,\n'
      f'you were born on {dob},\n'
      f'and live in {address},\n'
      f'on your next birthday you\'ll turn {int(age) + 1}')
```
[1]: https://www.w3schools.com/python/python_datatypes.asp