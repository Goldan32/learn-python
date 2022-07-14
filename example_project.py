# This project is utterly useless, but demonstrates some of the basic functionalities of Python

# Task:
# A text file contains information about beers. Every line is a type of beer.
# Beers have a name, a price (integer), and a type. These informations are separated by commas.
#
# The program should be able to:
#   - Read in a file in the format specified above
#   - Provide an option to add a new beer
#   - * List all beers sorted by type or price
#   - Save newly added beers to the same file it read from
#   - Recommend a beer (print a random beer)

from random import sample
beer_types = {"IPA", "Lager", "Cheap"}
beerFileName = "beers.txt"

class Beer:
    def __init__(self, btype: str, name: str, price: int):
        self.beerType = btype
        self.name = name
        self.price = price

    @staticmethod
    def parseFromLine(line: str):
        parts = [x.strip() for x in line.split(",")]
        return Beer(parts[2], parts[0], parts[1])

    @staticmethod
    def getBeerFromUser():
        print("Adding new beer.")
        print("Name: ", end="")
        name = input()
        print("Type: ", end="")
        beerType = input()
        print("Price: ", end="")
        price = int(input())
        return Beer(beerType, name, price)

    def __str__(self):
        return f"{self.name}, {self.price}, {self.beerType}"

    def __repr__(self):
        return str(self)


def menu(beer_list: list) -> bool:
    print("""Select what you want to do (Type a number):
1) List all beers
2) Get a random beer
3) Add a new beer""")
    print("Option: ", end='')

    num = int(input())
    # Works from 3.10
    match num:
        case 1:
            for beer in beer_list:
                print(beer)
            return True
        case 2:
            random_beer = sample(beer_list, 1)
            print(*random_beer)
            return True
        case 3:
            beer_list.append(Beer.getBeerFromUser())
            return True
        case _:
            print("Invalid option, choose a number between 1-3")
            return False

def main():
    beer_list = []
    with open(beerFileName, "r") as f:
        beer_list = [Beer.parseFromLine(line) for line in f]
        while not menu(beer_list):
            pass

    with open(beerFileName, "w") as f:
        for b in beer_list:
            f.write(str(b) + "\n")

if __name__ == "__main__":
    main()
