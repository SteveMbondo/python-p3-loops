#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count >= 1:
      print(count)
      count -= 1
      if count == 0:
         print("Happy New Year!")
      
happy_new_year()


def square_integers(int_list):
    # code goes here!
    squared_list = []
    for i in int_list:
       squared_value = i ** 2
       squared_list.append(squared_value)
    return squared_list
print(square_integers([1, 2, 3]))

def fizzbuzz():
    # code goes here!
    for number in range(1, 101):
       if number % 3 == 0 and number % 5 == 0:
          print("FizzBuzz")
       elif number % 3 == 0:
          print("Fizz")
       elif number % 5 == 0:
          print("Buzz")
       else:
          print(number)
fizzbuzz()
