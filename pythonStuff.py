# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Print string
# !/bin/python3

# Print string

print("hello world")

print('\n')  # new line

# math
print("math time")
print(50 + 50)  # addition
print(50 - 50)  # minus
print(50 - 50 + 50 * 50)  # something
print(50 ** 2)  # 50 times 50
print(50 // 5)

print('\n')  # new line

# variables & methodes
print("fun with variables and methodes")
quote = "all is fair in love and war"
print(len(quote))  # length
print(quote.upper())  # upper
print(quote.lower())  # lower
print(quote.title())  # title

name = "hasan"
age = 29  # int int(29)
gpa = 3.7  # float float(3.7)

print(int(age))
print(int(29.9))  # doesn not round
print("my name is " + name + " and  I am " + str(age) + " years old.")

print('\n')  # new line

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')  # new line

# funtions
print("Now, some funtions")


def who_am_i():
    name = "hasan"
    age = 21
    print("my name is " + name + " and  I am " + str(age) + " years old.")


who_am_i()


# adding in pramaters
def add_one_hundert(num):
    print(num + 100)


add_one_hundert(100)


# add in multipale paramters
def add(x, y):
    print(x + y)


add(7, 7)
add(123, 234)


# using return

def multiply(x, y):
    return x * y


print(multiply(7, 9))


def square_root(x):
    return x ** .5


print(square_root(16))

print('\n')  # new line

# boolean expressions (True or False)
print("boolean expressions")
bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

# relational and boolean operatiors

greater_then = 7 > 5
less_then = 5 < 7
greter_then_equal_to = 7 >= 7
less_then_equal_to = 7 <= 7

print(greater_then, less_then, greter_then_equal_to, less_then_equal_to)

test_and = (7 > 5) and (5 < 7)  # both of them has to be true
test_or = (7 > 5) or (5 < 7)  # if one ture then the statment is true
test_not = not True


# Lists
print("Lists Have brackets")
movies = ["mad max", "infinty war", "the hangover", "spiderman across the univers"]

print(movies[0])
print(movies[0:2])
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))

movies.append("Jaws") #add movies
print(movies)

movies.pop()  #remove movies
print(movies)

movies.pop(2)
print(movies)

movies = ["mad max", "infinty war", "the hangover", "spiderman across the univers"]
person = ["meath", "jack", "leah", "jeff"]
combined = zip(movies, person)
print(list(combined))

print('\n')

#Tuples
print("Tuples have parentheses and cannot change")
grades = ("a", "b", "c", "d", "f")
print(grades[1])

#Looping
print('\n')

print("For loops - start to finish of iterate:")
vegetables = ["cucumber", "spinach", "cabage"]
for x in vegetables:
        print(x)

print('\n')

print("While loops - execute as long as true:")
i = 1
while i < 10:
    print(i)
    i += 1

print('\n')
#importing
print("importing is important")

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt
print(dt.now())

def new_line():
    print('\n')

new_line()

#Advance strings
print("advance strings:")
my_name = "hasan"
print(my_name[0]) #first innitial
print(my_name[-1]) #last letter

sentence = "This is a sentence."

print(sentence[:4]) #first word
print(sentence[-9:-1]) #last word

print(sentence.split()) #split sentence by delimeter

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

print('\n'.join(sentence_split))

quoteception = "I said 'give me all the money'"
print(quoteception)

quoteception = "I said, \"give me all the money\""
print(quoteception)


#day 4...


print("A" in "Apple")


letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

too_much_space = "             hello                         "
print(too_much_space.strip())

full_name = "asan Uguz"
print(full_name.replace("asan", "Hasan"))
print(full_name.find("Uguz"))


movie = "The Hangover"
print("My favorite movie is {}.".format(movie))

def favorite_book(title, author):
    fav = "My favorite books is \"{}\", which is written by {}".format(title, author)
    return fav

print(favorite_book("dune", "frank harbert"))

new_line()

#Dictinories
print("Dictiories are keys and values:")
drinks = {"White Russians": 7, 'Old fashion': 10, 'Lemon Drop': 8, 'Buttery Nipple': 6} #drink is key price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Fina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy", "Mort"]}
print(employees)

employees["Marketing"] = employees.pop("IT")
employees["Cleaning"] = employees.pop("Finance")
print(employees)

employees["Legal"] = ["Mr. fround"] #add new key: value
print(employees)

employees.update({"Sales": ["Annie", "Andie"]})
print(employees)

drinks["White Russians"] = 8
print(drinks)

print(drinks.get("White Russians"))
print(drinks.get("Martini"))

#List and dictinories
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]
person = ["Heath", "Bob", "Leah", "Jeff"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}

print(movie_dictionary)