**This gudie is not meant to be taken seriously, I created it for my freinds who I'll be teaching face to face with much more in depth explanations.**

# Python for ~~Dummies~~ Dumbasses
Enjoy.

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

### Creating your first "project"
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



## First, let's just talk about programming
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
std::String = "False"
std::bool = false;
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
### List
### Dictionary
### Tuple

## Control flow
### if statement
### while loop
### for loop

## Classes
### Fields and Methods
### Importing libraries
### Writing your own classes
### Is everythings a class?

## File handling
### Read
### Write and Append



