# -*- coding: utf-8 -*-
"""Intermediate Python Programming.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A1s9-_MlWTptlNUhAhNmHLglmj_rAgBz

# **TOPIC-1: List**
"""

mylist = ["Banana", "Apple", "Mango"]
print(mylist)

mylist.append("Charry")

print(mylist)

mylist.insert(1, "Buebarry")
print(mylist)

mylist.pop()  #remove last element

print(mylist)

mylist.remove("Apple") #remove any spec. ele

print(mylist)

mylist.clear() #remove all ele
print(mylist)

mylist = [4,5,67,23,4,]
mylist.sort()
print(mylist)

mylist1 = [4,5,67,23,4]
mylist2 = sorted(mylist1)
print(mylist2)

mylist = [0] * 5
print(mylist)

new_list = mylist1 + mylist2
print(new_list)

mylisst = [2,3,4,5,67,1,3,7]
a = mylisst[1:5]
print(a)

print(mylisst[:5]) #till 4
print(mylisst[1:]) #skip 1 and print all
print(mylisst[::5]) # start from 1 skip 4
print(mylisst[1::]) # skip 1
print(mylisst[2::]) # skip till 2
print(mylisst[::4]) # start form 1 index skip 3
print(mylisst[::-1]) # reverse the list

list_org = ["abanaa", "Apple", "orange"]
list1 = list_org  #if use don't copy the changes not effect on org
print(list1)
list1.append("Charry")
print(list1)
print(list_org)

list_org = ["abanaa", "Apple", "orange"]
list1 = list_org.copy() #if use copy the changes not effect on org
print(list1)
list1.append("Charry")
print(list1)
print(list_org)

mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]  #fastet way to copy one list in another
print(mylist)
print(b)

"""# **Topic-2: Tuples**"""

mytup = "Max", 40, "Bosten"
print(mytup)

item = mytup[0]
item1 = mytup[2]
item2 = mytup[-2]
item3 = mytup[-1]
print(item)
print(item1)
print(item2)
print(item3)

mytup[0] = "Alex" # error tuple can't be change

for i in mytup:
  print(i)

if "Max" in mytup:
  print("yes")
else:
  print(No)

print(len(mytup))

mytup2 = ['z','a','e', 'a', 'b']
print(mytup2.count('a'))

mytup2 = ['z','a','e', 'a', 'b']
mylist = list(mytup)

print(mylist)

mytup3 = tuple(mylist)
print(mytup3)

mytup4 = "Max", 40, "Bosten"
  name, age, city = mytup4
  print(name)
  print(age)
  print(city)

mytup5 = "Max", 40, "Bosten", 4, 5, 6, 3, "My"
print(mytup5[::2])
print(mytup5[::1])
print(mytup5[:2])

mytuple = (1, 2, 3, 4, 5, 7,5)
i1, *i2, i3 = mytuple
print(i1)
print(i2)
print(i3)

"""# **Topic-3: Dictionaries**"""

mydict = {
    "name" : "Mustafa",
    "Class" : "12",
    "Age" : 3,
    "Gemder" : "M"
}
print(mydict)

mydict["Email"] = "FA21"
print(mydict)

del mydict["Class"]

print(mydict)

mydict.pop("Age")
print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict:
  print(mydict["name"])

try:
  print(mydict["name"])
except:
  print("Error")

for key in mydict:
  print(key)

print(mydict.keys())
print(mydict.values())

mydicst = {0: 3, 5: 4, 6: 3, 9:1}
print(mydicst[0])

"""# **Topic-3:  Set**"""

myset = set()
myset.add(3)
myset.add(6)
myset.add(2)
myset.add(4)
myset.add(33)

print(myset)
myset.remove(33)
print(myset)
myset.discard(6)
print(myset)
myset.pop()
print(myset)

if 4 in myset:
  print("yes")

odd = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
prime = {2, 3, 4, 5, 7}

u = odd.union(evens)
print(u)

u = odd.intersection(prime)
print(u)

A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
B = {1, 2, 3, 10, 11, 12}

print(A.difference(B))
print(A.symmetric_difference(B))

print(A.intersection_update(B))

"""# **Topic-3: Strings**"""

mystr = "   Hello   "
myst = mystr.strip()
print(myst)
print(mystr)

my_list = ['a'] * 6
my_str = ''
for i in my_list:
  my_str += i
print(my_str)

mystr = ''.join(my_list)
print(mystr)

"""# **Topic-4: Collections**

Collections : Counter, namedtuple, OrderedDict, defaultdict, deque

"""

from collections import Counter
a = "aaaabbc"
my_co = Counter(a)
print(my_co)
print(my_co.most_common(1))
print(my_co.most_common(2))
print(list(my_co.elements()))

from collections import namedtuple
  Point = namedtuple('Point', 'x,y')
  pt = Point(1, -4)
  print(pt)
  print(pt.x, pt.y)

from collections import OrderedDict
  orderedDict = OrderedDict()
  orderedDict['a'] =1
  orderedDict['b'] =2
  orderedDict['c'] =3
  orderedDict['d'] =4
  print(orderedDict)

  orderedDict = {}
  orderedDict['a'] =1
  orderedDict['b'] =2
  orderedDict['c'] =3
  orderedDict['d'] =4
  print(orderedDict)

from collections import defaultdict
  d = defaultdict(int)
  d['a'] = 1
  d['b'] = 2
  print(d['a'])
  print(d['c']) #default int value

  d = defaultdict(float)
  d['a'] = 1
  d['b'] = 2
  print(d['a'])
  print(d['c']) #default float value

"""# **Topic-4: IterTools**

Itertools: product, perumations, combinations, accumulate, groupby and interfinite iterators
"""

from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))

prod = product(a,b, repeat=2)
print(list(prod))

from itertools import permutations
a = [1, 2, 3]
per = permutations(a)
print(list(per))

per = permutations(a, 2)
print(list(per))

from itertools import combinations
a = [1, 2, 3, 4]
comb = combinations(a,2)
print(list(comb))

from itertools import combinations_with_replace
a = [1, 2, 3, 4]
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

from itertools import accumulate
a = [1, 3, 4, 4]
acc = accumulate(a)
print(a)
print(list(acc))

from itertools import accumulate
import operator
a = [1, 3, 4, 4]
acc = accumulate(a, func = operator.mul)
print(a)
print(list(acc))

from itertools import accumulate
import operator
a = [1, 3, 4, 4]
acc = accumulate(a, func = max)
print(a)
print(list(acc))

from itertools import groupby
def smaller_than_3(x):
  return x<3
a = [1, 2, 3, 4, 5]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
  print(key, list(value))

from itertools import groupby

person = [{'name':'Mustafa', 'age':25}, {'name':'Raza', 'age':29},
 {'name': 'Iqbal', 'age': 54}, {'name': 'Faheem','age': 21}]

group_obj = groupby(person, key=lambda x: x['age'])
for key, value in group_obj:
  print(key, list(value))

"""# **Topic-6: Lambda**

Lambda arguments: expression



"""

add10 = lambda x: x +10
print(add10(5))

def add10_func(x):
  return x + 10

mult = lambda x,y: x*y
print(mult(2,7))

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]  #same work in less line
c = [x*3 for x in a]
print(c)

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)  # filter(func, seq)
print(list(b))

c = [x for x in a if x%2==0]
print(c)

c = [x*2 for x in a if x%2==0]
print(c)

a = [1,2,3,4,5,6]
product

#reduce(func, seq)
from functools import reduce
a = [1,2,3,4]
product_A = reduce(lambda x,y: x*y,a)
print(product_A)

Name = input('Enter your name: ')
print("Hello " + Name)

hours = input('Enter the hours')
pay = input('Enter the pay')
total = int(hours) * int(pay)
print("Pay = ", total)

hours = input("Enter the hours: ")
rate = input("Enter the rate: ")
if type(rate) == str:
  print("Error")
else:
  tot = hours*rate
  print("Total = ", tot)

temp = "5 degree"

cel = 0
fahr = float(len(temp))
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

for i in [2,1,5]:
    print(i)

# Below is code to find the smallest value from a list of values.
# One line has an error that will cause the code to not work as expected. Which line is it?:

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

for n in "banana":
    print(n)

fruit = "banana"
x = fruit[1]
print(x)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
print(pieces)
print(parts)

# What will the following code print?

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))

# What will the following code print?:

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)

import re
x = "My 2 favoriate numbers are 19 and 42"
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[AEIOU]+',x)
print(y)

user = ["Mustafa", "Raza", "Sara"]
print("Raza" in user)
print(user[2])
print(user[-1])

print(user.index("Raza"))

print(user[0:2])
print(user[1:])
print(user[:-2])
print(len(user))
user.append("Aqsa")
print(user)

user += ["Nimra"]  #Add two list
user += ['Moiz']  #Add two list
user.extend(["Iqbal", "Tasleem", "Fatima", "Zehra"])

print(user)

user.insert(0, "Iqbal Hassan")

Mylist = ["Mustafa", 4, "Raza", 3.99, "Sarah", "Aqsa"]
res = []
for i in Mylist:
  if type(i) == str:
    res.append(len(i))

print(res)

user.remove("Mustafa")
print(user)

user.pop()

del user

value = 0
while value <= 10:
  print(value)
  if value == 5:
    break
  value+=1

for x in range(5, 101, 5):
  print(x)

for i in range(40, 0, -4):
  print(i)

def hello():
  print("Hello World!")

hello()

def sum(num1=0, num2=0):
  if(type(num1) is not int or type(num2) is not int):
    return
  return num1+num2

sum("A",2)
sum()

def mul(*args):  #form multiple arguments we use *args and its type is tuple
  print(args)
  print(type(args))

mul("Def", "Jon", "Sara")

def mul_items_named(**kwargs):
  print(kwargs)
  print(type(kwargs))

mul_items_named(First="Mustafa", last="'Hassan")

def add_one(num):
  if(num >= 9):
    return num+1

  total = num+1
  print(total)
  return add_one(total)

add_one(0)

value = "Y"
count = 0

while value:
  count += 1
  print(count)
  if(count == 5):
    break
  else:
    value = 0
    continue

"""# **Rock || Paper || Scissors**"""

import sys
import random
from enum import Enum

class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCISSOR = 3

playagain = True

while playagain:
  playerchoice = input("Enter Choice \n 1->ROCK \n 2->PAPER \n 3->SCISSOR")

  player = int(playerchoice)

  if player<1 or player>3:
    sys.exit("You must enter 1, 2, or 3.")

  computerchoice = random.choice("123")
  computer = int(computerchoice)

  print("\n You chose" + str(RPS(player)).replace('RPS.', '').title()+".")
  print("\n Python chose" + str(RPS(computer)).replace('RPS.', '').title()+".\n")

  if player == 1 and computer==3:
        print(" You Win !")
  elif player == 2 and computer==1:
        print(" You Win !")
  elif player == 3 and computer==2:
        print(" You Win !")
  elif player==computer:
        print("Python won")

  palyagain =   input("\n Play Again? \n Y -> Yes \n N -> NO \n Q -> Quit")

  if playagain.lower() == "y":
        continue
  else:
        print("Thank YOU")
        playagin = False

sys.exit("Bye!")

"""# **Clouser:** is a function having access to the scope of its parent function after the parent function returned."""

def parent_function(person):
  coins = 3

  def play_game():
    nonlocal conis
    conis -= 1

    if conis>1:
      print("\n "+ person + " has " + str(conis) + " conis left.")
    elif conius == 1:
      print("\n "+ person + " has " + str(conis) + " conis left.")
    else:
      print("\n "+ person + " is out of conis.")

  return play_game

  mus = parent_function("Must")
  tafa = parent_function("afa")

  mus()
  mus()

  tafa()

import math
print(math.pi)

import sys
import random
from enum import Enum

random.choice()

from __future__ import print_function
import sys
import random

def guess_number(name='PlayerOne'):
  game_count = 0
  player_wins = 0

  def paly_guess_number():
    nonlocal name
    nonlocal player_wins

    playerchoice = input("\n"+ name + " guess which number I'm thining of...1 2 3")

    if playerchoice not in ["1", "2", "3"]:
      print("Please enter 1, 2, or 3.")
      return paly_guess_number()

    computerchoice = random.choice("123")
    print(name + " you chose "+ playerchoice)
    print("I was thinking about the number "+ computerchoice)

    player = int(playerchoice)
    computer = int(computerchoice)

    def decide_winner(player, computer):
      nonlocal name
      nonlocal player_wins

      if player == computer:
        player_wins += 1
        return f"{name}, you win!"
      else:
        return f"Sorry {name}!"
    game_result  = decide_winner(player, computer)

    print(game_result)

    nonlocal game_count
    game_count += 1

    print(f"\n Game Count: {game_count}")
    print(f"\n {name}'s Win: {player_wins}")
    print(f"\n Your winning percentage: {player_wins/game_count:.2%}")

    print(f"\n Play again. {name}?")

    while True:
      playagin = input("\nY for Yes or \nQ to qiut\n")
      if playagin.lower() == "Y":
        return paly_guess_number()
      else:
        print("\n Thank for playing")
        if __name__ == "__main__":
          sys.exit(f"Bye {name}")
        else:
          return
  return paly_guess_number

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(
      description = "Provide a personlazied game expericence."
  )

  parser.add_argument(
      '-n', '-name', metavar = 'name', required = "True", help='The name of the person playing the game'
   )

  args = parser.parse_args()

  print(f"\n {args.name}, welcome to the Arcade!")

  play_game(agrs.name)

"""# **Project: Counter App**"""

import datetime
user_input = input("Enter your goal with a deadline separatedby colon\n")
input_list = user_input.split(":")

# goal = input_list[0]
deadline = input_list[0]


deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till =  deadline_date - today_date

hours_till = int(time_till.total_seconds()/ 60/ 60)
print(f"Dear User! Time remanning for your goal : {goal} is {hours_till} hours")

"""# **OOP's**"""

class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def make_model(self):
    print(f"I'm a {self.make} {self.model}.")

  def moves(self):
    print("Moves Going..")

mycar = Vehicle('Tesla', 'Model 3')

# print(mycar.make)
# print(mycar.model)

mycar.make_model()
mycar.moves()


your_car = Vehicle('Civi', 'Newf4')
your_car.make_model()
your_car.moves()

class Airplane(Vehicle):
  def moves(self):
    print("File along..")

class Truck(Vehicle):
  def moves(self):
    print("Truck Moving...")

class moter(Vehicle):
  def moves(self):
    print("Bike Moving..")

your_Airplane = Airplane('Private', 'MB29')
your_Truck = Truck('G19', 'Gulish')
your_moter = moter('CD-70', 'Honda')

your_Airplane.make_model()
your_Airplane.moves()

your_Truck.make_model()
your_Truck.moves()

your_moter.make_model()
your_moter.moves()

"""# **OOP Project**"""

class BankAccount:
  def __init__(self, initialAmount, acctName):
    self.balance = initialAmount
    self.name = acctName

    print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")

  def getBalance(self):
    print(f"\n Account '{self.name}' balance = ${self.balance:.2f}")

  def deposit(self, amount):
    self.balance  = self.balance + amount
    print("\n Deposit Complete.")
    self.getBalance()

  def variableTransaction(self, amount):
    if self.balance >= amount:
      return
    else:
      print(f"\n Sorry account '{self.name}' only has a balance of ${self.balance:.2f}")

  def withdraw(self, amount):
    try:
      self.variableTransaction(amount)
      self.balance = self.balance - amount
      print("\nWidhdraw Complete.")
      self.getBalance()
    except:
      print(f'\nWidhdraw Interrupted:')

  def transfer(self, amount, account):
    try:
      print(f'\n*******\n\nBegging Transfer..rocker')
      self.variableTransaction(amount)
      self.withdraw(amount)
      account.deposit(amount)
      print('\n Transfer Complete!')
    except:
      print(f'\nWidhdraw Interrupted:')

class InterestRewardsAcct(BankAccount):
  def deposite(self, amount):
    self.balance = self.balance + (amount * 1.05)
    print(f'\nDeposite Compete.')
    self.getBalance()

class SavingAcct(InterestRewardsAcct):
  def __init__(self, initialAmount, acctName):
    super().__init__(initialAmount, acctName)
    self.fee = 5

  def withdraw(self, amount):
    try:
      self.variableTransaction(amount + self.fee)
      self.balance = self.balance - (amount + self.fee)
      print("\nWithdraw completed.")
      self.getBalance()
    except:
      print(f'\nWidhdraw Interrupted:')


Mustafa = BankAccount(1000, "Mustafa")
Raza = BankAccount(5000, "Raza")

Mustafa.getBalance()
Raza.getBalance()

Mustafa.deposite(500)
Raza.deposit(1000)

Raza.transfer(1000, Mustafa)
Raza.transfer(10, Mustafa)

j