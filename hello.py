#!/usr/bin/env python3

def talking_duck(sentence, num):
    temp = sentence + " Quack." * num
    return temp

def hello():
    print("Hello Everyone!")

def square(num):
    num = num ** 2

def main():
    print("Hello World!")

    num_integer = 42
    print(num_integer)

    num_integer = num_integer + 1
    print(num_integer)

    num_float = 3.14
    whole_float = 42.0

    print(3.9 + 2.1)

    str1 = 'This is " a string'
    str2 = "This is ' also a string"
    str3 = f"The value of a variable is {num_integer}"

    str4 = """ This
    is
    multiple
    lines"""

    print(str3)

    print("quack " * 3)

    print("Hello" + " " + "World")

    var_t = True #bool
    fake_var_t = "True" #string

    five = "5"
    five_num = int(five)
    five = str(five_num)
    print(five_num + 3, five + '3')

    print("line1", end=' ')
    print("line2")

    print("alma\nkorte")

    hello()
    hello()
    hello()

    square(num_integer)
    print(num_integer)

    #num = int(input("Enter a number: "))

    #duck = talking_duck("I am a duck.", num)
    #print(duck)

    people = []
    person1 = "John"
    people.append(person1)
    people.append("Joe")
    print(people)
    people[1] = "Not Joe"
    print(people)
    print(len(people))
    print(people[-1])
    



if __name__ == "__main__":
    main()


