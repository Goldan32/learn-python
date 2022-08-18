**This guide is not meant to be taken seriously, I created it for my freinds who I'll be teaching face to face with much more in depth explanations.**

# Python for ~~Dummies~~ Dumbasses
Enjoy.

\\insert_toc\\

## Getting Started
This chapter can be done on your own. It contains intstruction on stuff you need to download to get started.

### IDE or Editor
First you'll need a program which we can use for editing code. My recommendation is **VSCode** editor from Microsoft. It's open source and widely used today. Install it from the following link, default location is encouraged. During installation make sure to enable the option **Add VSCode to PATH**.

- https://code.visualstudio.com/

To try out VSCode, simply open a Command Prompt, and type
```bash
code
```

### Python interpreter
There is only one Python interpreter that matters, the official one. Install it, and make sure to select the option to **Add Python to PATH** during installation.

- https://www.python.org/downloads/

To verify that python is correctly installed, open a Command Prompt and type
```bash
python --version
```

If that didn't work, try
```
python3 --version
```

### Creating your first project
Python does not require specific programs to create projects. Every project is just a folder containing .py source files.

1. Open a Command Prompt and navigate to the place where you want to place your project.
```bash
# To enter a folder execute
cd folder_name

# To go up a level execute
cd ..
```

2. Make the project folder and enter it.
```bash
mkdir learn_python
cd learn_python
```

3. Open VSCode
```bash
code .
```
4. Create a new file in VSCode with **Ctrl+N** and name it *hello.py*.

5. Copy or type this line into the file.
```python
print("Hello World!")
```

6. Run the program by typing this into the command line.
```bash
python3 hello.py
```

7. The program should print `Hello World!` to the Command Prompt.

**This is where you should stop alone, and wait for a face to face course**

## First let's just talk about programming
This can't be done alone. Let's engage in a discussion about the following topics
 - Why do you want to learn programming?
 - What do you plan on using programming for?
 - What do you already know about programming?

Every basic concept that is not clear for you should be explained here:
 - What is programming?
 - Why is it useful?
 - How computers process code?
 - COMMENTS

## Interpreted language
Contrary to compiled languages, intepreted languages are executed line-by-line. While a compiled language wont compile if there is a syntax error, an interpreted language will execute every line until the syntax error is reached.

There is no need to explain this concept further but the concept could be explained further: Interpreted languages run already compiled pieces of code, which often bloats runtime because the compiler can't see the whole code, thus can't optimize the binary.

## Variables
Variables in python are created when value is assigned to them. By default, a new value can be assigned the same way, and the retained value can also be freely modified.

### Numbers
Python knows 2 types of numbers. Both of them has no upper or lower bound. All the usual operations can be performed on both types.

#### Integers
Integers are whole numbers. However operations executed on them that can be fractions, will not be integers, but whole floats (see later).

```python
num_integer = 42

x1 = num_integer + 2    # 44
x2 = num_integer - 6    # 36
x3 = num_integer * 3    # 126
x4 = num_integer / 2    # 21.0
x5 = num_integer / 5    # 8.4
x6 = num_integer // 5   # 8
x7 = num_integer % 5    # 2
x8 = num_integer ** 2   # 1764
```

#### Floats
Floats represent fractions. I could go on and on about how they are not precise but it wont ever matter when using python. A float can also be a whole number, but it will act as a float in all scenarios where that matters. Express that a whole number is a float and not an integer in the following way.

```python
num_float = 3.14
whole_float = 42.0
```

All the operations that work on integers work on floats.

It's important to note that while adding `3` to `2.1` results in a float, adding `3.9` to `2.1` will not result in an integer but a whole float.

### Text
Text is stored in a type called *string* or often *str* for short.
```python
string_singleQuote = 'This is a string'
string_doubleQuote = "This is also a string"
string_fstring     = f"This string can contain a variable like {num_integer}"
string_multiline   = """This a 
multiline  string"""
```
These are the ways of creating a string. There is no difference between the first two. The *fstring* is a special string where you can replace a variable with its text representation by enclosing its name in `{}` characters. This will make our lives easier later. The fourth line is the definition of a multiline string. Python parses the code line by line, so we need a special way to tell the intepreter that this is not a syntax error but a multiline string.

We can also mutate strings with operations, just like with numbers.
```python
concat_string = string_singleQuote + " and " + string_doubleQuote
duck_says = "quack " * 3
```

### Boolean
Booleans are a type of variable that only has 2 states, *true* or *false*. This will be important when discussing control flow of a program where this 'two stateness' is essential.
```python
var_f = False
var_t = True
```

But wait. How does python know that we're trying to make a boolian and not a string that contains `"False"`. We are certainly not telling it like for example in C++.
```cpp
// NOT PYTHON CODE
std::String str1 = "False"
std::bool b1 = false;
```
Contrary to this, python uses the **Duck Test** to determine the type of a variable.
> If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

Meaning that if it was defined with `""` and it occupies 6 bytes in memory than it must be a string.

## Printing
Any basic program will need to communicate with the user. This is usually done by writing to the *standard output*. The program can also take input from the user, but communication in the other direction is more important.

The `print()` function has so many usecases that explaining them is not reasonable. Here are some basic uses that can be easily understood.
```python
print(num_integer)
print(num_float)
print(string_singleQuote)
print(string_fstring)
print(string_multiline)

print(num_float, num_integer)
print(num_float, end=" and ")
print(num_integer)
```

The only note here is the argument `end=`. When printing, the line that gets printed is finished with a new line character. To change this behaviour we must explicitly give this argument.

But wait a minute here. How does `print()` or even python know how to print a number. Well only the types and classes (see later) than can be converted to a string can be printed. All the basic types can be converted automatically, but later we will learn how any type can be converted with a little effort.

## Functions
Python normally executes our code line by line. This is actually not true, there are ways we can influence what the next executed piece of code should be. One of these ways is with functions. We can think of functions as "mini-programs" inside our program. When a function is *called*, this mini-program takes control of our main program and its lines will be executed until the function *returns*. After that, the main program retakes control and continues from next line after the function call.

Of course a function can call another function and so on until we run out of the stack, which let's be honest will never happen in a normal usecase on an x86 computer. By the way what is the stack? Well it's not essential to know but can be explained easily if you're courious.

So how to define functions? Here is the boilerplate code of a python source file with a function. The function should be defined before the first line that is actually executed. Write a function that prints something to the console.
```python
def hello():
    print("Hello from a function!")
hello()
print("Hello World")
```

Sidenote, but an important one at that. In all languages there is a block system for grouping code. We did not need it so far, but we somehow have to be able to separate the code of the function from other code of the source file. In python this is done with *indentation*. My advice is to always indent with **4 spaces** a level, but one tab character can also be used.

The functions first line is on the 0th indentation level and is called a function header. After that comes the definition of the function which is on the 1st indentation level. When we write a line on the 0th level again, than the function definition ends there. Indentation will be used more at the control flow chapter.

### Arguments
This is a tough one but try to look at a function as a mini-program again. The function can't see variables that were defined in the original program and vice-versa. But then how will we communicate with functions? A function can have as many *arguments* as you want however we'll soon see that we rarely need more than one or two.

When passing an argument to a function, we essentially make a copy of that variable that the function can use. It's not always a copy, or what is a copy anyway but we'll talk about that later. For now think that a function can't modify a value passed to it.

Let's write a function that prints the square of its argument.
```python
def square(number):
    print(number ** 2)

square(5)
square("five")
```

So the last line does not work, a string cannot be raised to any power. We can add a little hint about the parameters or arguments of a function but it won't perform a type check.

```python
def square(number: int):
    print(number ** 2)

square(5)
square("five")
```

### Return values
Another problem is: If a function can only work on copies of variables, how can we write a function that mutates a value? Return values are the key here. A function can have as many return values as you want, it will be clear in the next chapter why. For now let's just work with a single one. Write a function that takes a string and appends it with `quack`.
```python
def talking_duck(sentence: str) -> str:
    temp = sentence + " Quack."
    return temp

new_sentence = talking_duck("Hello World!")
print(new_sentence)
```
See that the return value can be specified but this is also only for the programmer to undertand its own code more.

### Standard program boilerplate
There is a clear "best" structure for a python program that should be followed. Not all parts of it will be familiar, but from now on use this boilerplate for all of your programs. Remove any section not needed in your code!
```python
# Module imports come here
from sys import argv

# Class definitions come here
class Beer:
    pass

# Functions come here
def talking_duck(sentence: str) -> str:
    temp = sentence + " Quack."

# Main function comes here
def main():
    new_sentence = talking_duck("Hello World!")
    print(new_sentence)

# The only thing not in a function should be this
if __name__ == "__main__":
    main()
```

I'll think about if it's necessary to explain all parts of this, but use this structure please. It makes testing easier also if you make a `test()` function that you can run instead of `main()`.

## Complex data structures
The basic types are great for describing one thing. But python is a very high level language and natively offers options to create different collections of the basic types. There are many more, but here we'll learn the 3 most important ones.

### List
Lists are python's implementation of a standard array or vector. It's used the most in basic programs. A list stores elements in order, it is indexable, an element can occur multiple times and elements can be changed or modified. In short, a list is **ordered**, **changable** and **allows duplicates**.

When to use a list? Lists have a variety of usecases. It's hard to demonstrate how useful they are without iterations, but here is how to handle them anyway.

```python
# Create an empty list
people = []

# or
people = list()

# Let's say a person is a string now
person1 = "John"

# Add these values to the list
people.append(person1)
people.append("Joe")

print(people)

people[1] = "Not Joe"
print(people[1])
```

`append()` puts the value in its argument to the back of the list. `print()` can display a full list but in more of a debugging and not a nice format. A nice format will be shown when learning loops.

It goes without saying, but the first element of a list is accessed with the index **0**. This means that the last index is one below the length of the list, which by the way can be accessed with the `len()` function. `len()` works on all iterable types, more on them later.

### Dictionary
A dictionary is a collection that can be used to store key-value pairs. It can also be refered to as an *associative array* but that can be confusing as dictionaries are **unordered**. However you can still iterate through them, it will be shown how later. The keys are unique, but two different keys can be paired with the same value.

Using a dictionary is somewhat easier than using a list because of its unordered nature. The keys and the values can be of any type.

```python
# Create an empty dictionary
translator = []

# Add some items
translator["apple"] = "alma"
translator["pear"] = "korte"
translator["throw"] = "dob"
translator["drum"] = "dob"
print(translator)

# Change a value
translator["apple"] = "iPhone gyarto ceg"
print(translator)

```
So adding new reacords and changing existing ones is easy. How do you think a key can be changed instead of a value?
### Tuple
A tuple is a collection that is similar to a list as it's **ordered and duplicate items are allowed**, but these items **cannot be changed**. You will rarely define tuples but here is how to do it. As a tuple cannot be changed, you have to add all the items while defining it. Its members can be accessed by indexing.

```python
exam_subjects = ("maths", "hungarian", "history", "physics", "english")
print(exam_subjects[2])
```

I know what you think. This is utterly useless, right? No, you couldn't be more wrong.

Let's say we want to create a function that simulates the inverse of the absolute value mathematical function. A positive number can be the absolute value of the same number and the same number times -1. But a function can only return 1 value as we already know.

This is where a tuples come in. From a function we can return an **unnamed tuple**, then at the place of the function call we can use **patter matching** to deconstruct that tuple into multiple variables.

```python
def inverse_abs(num):
    return (num, num * -1)          # Unnamed tuple

positive, negative = inverse_abs(5) # Pattern matching

print(positive, negative)
```
## Control flow
And we are finally here. After this chapter, our programs will now longer execute one line after the other, but the next line will often be decided based on a value of a variable.

### if statement
The if statement of if block is the simplest control flow structure. The if block gets executed if the expression in its header is true. Here comes in handy the boolean type. Every other type can be converted to boolean when it is in the header of an if block. We can invert a boolean with the `not` keyword.

Let's see some examples

```python
num_t = 12
num_f = 0

string_t = "something"
string_f = ""

if num_t:
    print("A number is true if it is not zero")

if string_t:
    print("A string is true if it is not empty")

# Now make the false ones true by inverting them

if not num_f:
    print("Zero is false")

if not string_f:
    print("Empty string is false")
```

Not only a single variable can be converted to boolean type. The result of an operation can also be either true of false. Here are some examples.

```python
num1 = 23
num2 = 20

str1 = "apple"
str2 = "pear"

if str1 == "apple":
    print("This is true")

if str1 == str2:
    print("This is false")

if num1 == num2 + 3:
    print("This is true")

if num1 > num2:
    print("This is true")

if num1 >= num2:
    print("This is true")

# Check if a list contains a value
available_foods = ["hamburger", "hot-dog", "pizza"]

if "hamburger" in available_foods:
    print("This is America")
```

If something is converted to a boolean, we can then use bool algebra on those values. Here is a reminder of basic bool algebra.

```python
t = True
f = False

t and f # False
t and t # True
f and f # False

t or f # True
t or t # True
f or f # False

# Practical example

num1 = 11
num2 = 5

# Condition: num 1 is above 10 num2 is not zero
# print "ok" if the condition is satisfied 
if (num1 > 10) and num2:
    print("ok")

```
> Remember: Always use parantheses to signal or set precedence in complicated expressions!

So if the condition is true than the block gets executed and if it was false, nothing happened... so far. Here are some examples of the other branch of this expression.

The `else` branch gets executed *instead of* the if branch when the condition is false.

```python
num1 = 22

if num1 == 12:
    print("num1 was 12")
else
    print("num1 was not 12")

```
What if there are more cases than true and false. Here are examples with `elif` branches. You can use however many of these branches. The last `else` block is **not** compulsory.

```python
animal = "cat"

if animal == "dog":
    print("You failed")
elif animal == "cat":
    print("Great choice")
elif animal == "parakeet"
    print("Not bad")
else:
    print("You've gone too far, go back to the cat")

```
It's inportant to note, that only the **first** block thats header is true will be executed.

```python
num = 11

if num > 20:
    print("Number greater than 20")
elif num > 10:
    print("Number greater than 10")
elif num > 0:
    print("Number greater than 0")
elif num > -10:
    print("Number greater than -10")
```
### while loop
Using an if statement is a one-time stop. The code in an if block either runs one time or zero times. With a while loop or while block we can run some code multiple times.

```python
x = 0
while x < 10:
    print(x)
    x = x + 1
```
This code snippet will print the numbers 0 to 9. When the execution reaches the header of the while loop, it checks if the condition is true. If it is true, it executes the while block one time, but instead of continuing with the next line, the header of the while loop is evaluated once again. If it is still true, then the block of code is run again. This continues for all eternety.

**Anything that can be written into the header of an if block can be written to the header of a while block.**

Usually something happens inside the while block that changes whether the header will be true or false in the next round. In our example, we increment the x variable, so in the 11th loop, the header will be false. After this, the execution continues from the next line after the while block.

Lets try out what happens when we forget about changing something to make the header false.

```python
x = 0
while x < 10:
    print("Programming is fun!")
```

Here, we wanted to print a string 10 times, but forget about *loop variable*, so now our program will never exit this while loop, and will continue to print the given line until we stop it somehow.

If our program gets stuck in an *infinite loop* we can stop it by focusing the command line where the program runs and pressing **Ctrl+C**. This keyboard action sends an event to the program which stops it immediately.

Just to demonstrate some other useful usage of the while loop, here is a program that only stops running after the user can correctly spell *Mississippi*

```python
while input("Spell the name of that river: ") != "Mississippi":
    print("Not good, try again!")

print("Nice job")
```
### for loop
A for loop is similar to the while loop in the sense that it will be executed multiple times. However here there is no condition, this loop *iterates* through a collection starting with the first element and finishing with the last. After the last element, the program continues with the line after the for block.

Here is the the first while loop example done with a for loop.

```python
for x in range(10):
    print(x)
```

The header of a for loop starts with the the word for. After that we *create* a variable. This variable will be equal to the next element of the thing we are iterating through. So the first time we enter the for block, the loop variable will be equal to the first element of the thing we are iterating through.

So what is this thing actually? The thing after the *in* word in the header can be anything *iterable*. Iterable things contain other things that are ordered. For example a list contains other types of variables in order, therefore it can be in the header of the for block. A dictionary does not contain an ordered set of items so by default it is not iterable.

But what happens in the above example. The `range` function returns a list of numbers from zero to its argument minus one. So the above code is equivalent to this next one.

```python
for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(x)
```

So without further ado, here is how to print out the collections we learned so far, one element on one line.

```python
fruit_list = ["apple", "pear", "plum"]
for fruit in fruit_list:
    print(fruit)

exam_subjects = ("maths", "hungarian", "history", "physics", "english")
for subject in exam_subjects:
    print(subject)

friends_iq = {"Kiki": 69, "Soma": 2, "Dani": 9001}
# The .keys() method returns a list with the keys from a dictionary
for name in friends_iq.keys():
    print(f"The iq of {name} is {friends_iq[name]}")
```

One other thing. Iterating through a list this way the values in the list cannot be changed. Let's say we have a list conatining numbers and we want to square each number. How can we do this with a for loop?

```python
numbers = [2, 4, 6, 8, 11]
for num in numbers:
    num = num ** 2

print(numbers) # No change: [2, 4, 6, 8, 11]

for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2

print(numbers) # Changed: [4, 16, 36, 64, 121]
```

The solution was to not iterate through the list itself, but figure out its length, and make a list of indexes. By accessing each element via indexing, we can change the value in the original list as shown previously.

## Classes
So far we learned how to define functions and create variables. First let's take a look at variables that 'belong together' by some human logic. These variables can be grouped together within a *class*. Let's create a a new class that can describe a student. We only have to store information about this student that will be relevant to our program. First we'll want to be able to store a unique id, a name, and a birth year of a student. Here is a class that fullfills these requirements.

```python
class Student:
    name = ""
    birth_year = 0
    neptun = ""
```
### Fields and Methods

This is actually a correct class but pretty useless so far. A class is similar to a type, in the sense that a variables type can be `Student` in this case. The variables inside a class are called fields. But in this case these fields cannot be set when creating a new `Student` variable. For that, we will have to define a constructor inside the class definition.

### Writing your own classes

```python
class Student:
    __init__(self, n, b, i): # This is the constructor
        self.name = n
        self.birth_year = b
        self.neptun = i

elek = Student("Teszt Elek", 1999, "ASD123") # Here a variable of type Student is created
```

So lots of things happened here, let's unpack them in order. First line is the header of the class we are creating. Then in the next line, we create a function called the *contructor*. This functions will create the Student variable by assigning value to the class' fields. This function's first argument is `self` which refers to the instance of the class. This argument cannot be provided to the contructor it is automatic when creating a variable. The following arguments can be defined freely. Here we define 3 arguments, through which we can assign values to the 3 fields of this struct.

Functions inside a class whose first argument is `self` are called methods, more on them later.

First let's see how we can access the fields of a class. Assume the last block of code was run before this next one.

```python
print(elek.name)
print(elek.birth_year)

elek.name = "Teveg Elek"
print(elek.name)
```

As we can see, `elek` is the name of the variable and its fields can be accessed with the `.` operator. We can print and also change these fields freely.

What if we wanted to store some of these students results from some subjects. We can use a dictionary for this. We already know the 3 subjects we want to store the results of: maths, physics and programming, so we only need to pass a list of numbers to the constructor.

```python
class Student:
    __init__(self, n, b, i, r: list):
        self.name = n
        self.birth_year = b
        self.neptun = i
        self.results = {"maths": r[0], "physics": r[1], "programming": r[2]}

elek = Student("Teszt Elek", 1999, "ASD123", [2, 2, 5])

# Print the results of elek
for k in elek.results.keys():
    print(f"{k}: {elek.results[k]}")
```

So methods have the self object as the first argument. Methods are functions that relate humanly to the class. Most of the time methods operate on the fields of a class. Let's write a method that returns a boolean, and can be used to determine if a sudent failed or passed (if all the results are above one the student passed). Then use this method to print some general information about elek.

```python
class Student:
    def __init__(self, n, b, i, r: list):
        self.name = n
        self.birth_year = b
        self.neptun = i
        self.results = {"maths": r[0], "physics": r[1], "programming": r[2]}

    def did_pass(self) -> bool:
        ok = True
        for subject in self.results.keys():
            if self.results[subject] == 1:
                ok = False
        return ok

elek = Student("Teszt Elek", 1999, "ASD123", [2, 2, 5])

# Print general information about elek
print(elek.name)
print(elek.birth_year)
print(elek.neptun)
if elek.did_pass():
    print("Passed all his/her/their classes")
else:
    print("Failed one or more class")
```

### str and repr methods or how can I print my classes
We may take it for granted that we can write everything inside the `print()` function, and it will be displayed, but that is not the case with classes we write. Not by default at least.

We can write a special function for our class that will make it possible to print it like a number or a string. This function doesn't take parameters, only `self`, but returns a string which will be printed.

Let's expand our class with this method. This method doesn't just make print usabel, but gives us a way to convert our class to a string. Make it so that the output will be "human readable".

```python
# ...
    def __str__(self):
        return f"{self.name} was born in {self.birth_year}, neptun code: {self.neptun}"
# ...

elek = Student("Teszt Elek", 1999, "ASD123", [2, 2, 5])
print(elek)
```

As it can be seen, not all fields need to be in the final string that is returned.

### Importing libraries

Some functionalities are not available in the basic package of python, but they also don't require any downloads. They can be imported into the project like this.

```python
from random import sample
from random import randint

# Print a random integer from 0 to 100
print(randint(0, 100))

# Print a random element from a list
l = ["apple", "pear", "banana"]
print(sample(l))
```

This way we only imported 2 functions, but we can also import the whole class.

```python
import random
```

### Is everything a class?
No, but it's useful to think like this.

On every variable you may be able to call methods, and every variable may have fields. Also functions may work on one type of variable and not on another one.

## File handling
Reading and writing files is the basic task of programming. Everything is stored in files, so in complex programs file handling can never be avoided.

There are two types of files. **Text files** store information in a coded way, some common coding methods are ANSI or UTF-8. **Binary files** contain raw binary data as in zeros and ones. When opening a file, we can select which type of file to open our file as. After we are done, we also need to close the file.

For now, we will assume that every file we open is an **ANSI coded text file** as they are the easiest to deal with.

To read or write a file, we first need to open it with the `open()` function. This function has 2 arguments. The first is the path to the file we want to open, the second is a mode string. In the latter we can specify how we want to open a file.

  - "r" - Read - No changes will be made to the file.
  - "a" - Append - Writing will be appended to the end of the file if it exists. File will be created if not.
  - "w" - Write - Writing will overwrite the existing contents of the file.

### Read and Write

The standard way to interact with files in python is as follows.

1. Open the file for reading.
2. Read its contents into an appropriate data structure.
3. Close the file (for reading).
4. Make changes to the contents of said data structure.
5. Open the file for writing.
6. Overwrite the file with the updated contents.
7. Close the file (for writing).

Let's write a simple program to demonstrate this. First we will create a file then modify it. The first step of the above list starts in the second code block.

```python
file_name = "example_file.txt"

f = open(file_name, "w")
f.write("Hello from the other file!")
f.close()
```

The data structure in this case will be a string and the operation will be appending another sentence to it.

```python
file_name = "example_file.txt"

f = open(file_name, "r")
content = f.read()
f.close()

content = content + " Bye!"

f = open(file_name, "w")
f.write(content)
f.close()
```

There is also a more correct way to do this. By using **with** blocks, we don't have to open or close files. They open at the start of the block and close at the end.

```python
file_name = "example_file.txt"
content = ""

with open(file_name, "r") as f:
    content = f.read()

content = content + " Bye!"

with open(file_name, "w") as f:
    f.write(content)
```

There are many more useful methods, but they can be learnt on your own.

- **close():** Closes the file
- **flush()**:	Flushes the internal buffer
- **read()**:	Returns the file content
- **readline()**: Returns one line from the file
- **readlines()**:	Returns a list of lines from the file
- **seek()**:	Change the file position
- **tell()**:	Returns the current file position
- **truncate()**:	Resizes the file to a specified size
- **writable()**:	Returns whether the file can be written to or not
- **write()**:	Writes the specified string to the file
- **writelines()**:	Writes a list of strings to the file

## Program arguments
We drew parallels already between a program and a function. Well the same way a function can have arguments, a program can have too. Here is how to access these arguments on python.

The arguments will be stored in a list called `sys.argv`.

```python
from sys import argv

for a in argv:
    print(a)
```

This program prints every argument in a new line. You can test it by running the program the usual way, but adding more words separated with spaces.

```bash
$ python hello.py apple testword "Hello World"
```

## Your first real project
In this part will be a description of a project which you should complete on your own.

Task:

A text file contains information about beers. Every line is a type of beer.
Beers have a name, a price (integer), and a type. These informations are separated by commas.


The program should be able to:
  - Read in a file in the format specified above
  - Provide an option to add a new beer
  - *List all beers sorted by type or price
  - Save newly added beers to the same file it read from
  - Recommend a beer (print a random beer)

A solution can be found in this repository, but I don't recommend looking at it without completing the task first on your own.
