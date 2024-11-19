#!/usr/bin/env python3

# def happy_new_year():
#     i = 10
    
#     while i > 0:
#         print(i)
#         i -=1
#     print("Happy New Year!")
    
def happy_new_year():
    i = 1
    
    while i < 11:
        print(11 - i)
        i +=1
    print('Happy New Year!')
# happy_new_year()

# def square_integers(int_list):
    
#     return [num ** 2 for num in int_list ]

def square_integers(int_list):
    
    int_list2 = [list ** 2 for list in int_list ] #keep int_list bc this is what we want to loop through and create a new list assigned to variable 
    
    return int_list2
# print(square_integers([1, 2, 3, 4, 5]))

# Write a function fizzbuzz() that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

# def fizzbuzz():
#     for x in range(1, 101, 3):
#         print("Fizz")
        
#     for x in range(1, 101, 5):
#         print("Buzz")
    
#     for x in range(1, 101, 3 and 5):
#         print("FizzBuzz")


def fizzbuzz():
    for num in range(1, 101):  #this gives us number 1-100
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        

fizzbuzz()
