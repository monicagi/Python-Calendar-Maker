""" Name: Monica Guevara
    Class: CSC 4800
    Assignment: Lab #2

    This program displays a whole year calendar for the indicated year"""

import math
import sys

def ask():
    """The ask function does not take any parameters. It asks the user what year they want a calendar for.
        Then it calls the display function passing the given year as an argument"""
    year = input("What year would you like to see a calendar for: ")

    # Converts the user input to an int and calls the display function
    display(int(year))

def find_month(m, y):
    """The find_month function accepts two parameters the (m) stands for the month and the (y) for the year.
        Given the number symbol for the month it finds the string equivalent for it. The function returns a
        string with the month and the year"""

    if(m == 1):
        st = "\t\tJanuary "
        st = st + str(y)


    elif (m == 2):
        st = "\n\n\t\tFebruary "
        st = st + str(y)


    elif (m == 3):
        st = "\n\n\t\tMarch  "
        st = st + str(y)


    elif (m == 4):
        st = "\n\n\t\tApril "
        st = st + str(y)

    elif (m == 5):
        st = "\n\n\t\tMay "
        st = st + str(y)

    elif (m == 6):
        st = "\n\n\t\tJune "
        st = st + str(y)

    elif (m == 7):
        st = "\n\n\t\tJuly "
        st = st + str(y)

    elif (m == 8):
        st = "\n\n\t\tAugust "
        st = st + str(y)

    elif (m == 9):
        st = "\n\n\t\tSeptember "
        st = st + str(y)

    elif (m == 10):
        st = "\n\n\t\tOctober "
        st = st + str(y)

    elif (m == 11):
        st = "\n\n\t\tNovember "
        st = st + str(y)

    elif (m == 12):
        st = "\n\n\t\tDecember "
        st = st + str(y)

    return st

def week():
    """The week function accepts has no parameters. It returns the days in a week"""
    return ("Sun Mon Tue Wed Thu Fri Sat")

def get_days(m,y):
    """The get_days function has two parameters the (m) stands for months and the (y) for the year. It returns how many
        days a month has and checks if it is a leap year by calling the leap function passing the year"""

    if(m == 1 or m == 3 or m== 5 or m == 7 or m == 8 or m == 10 or m == 12):
        return 31

    if(m == 2):
        return leap(y)

    if(m == 4 or m == 6 or m == 9 or m == 11):
        return 30

def leap(y):
    """The leap function accepts one parameter (y) stands for the year and it checks if the year is a leap year and
        returns the number of days"""
    if(((y %4) == 0 and (y%100) != 0) or y % 100 == 0):
        return 29

    else:
        return 28

def find_start(y):
    """The find start function has one parameter the (y) stands for the year and it returns the day
        January starts in"""
    return (y + math.floor((y - 1) / 4) - math.floor((y - 1) / 100) + math.floor((y - 1) / 400)) % 7

def print_days(m,y,s):
    """The print_days function has three parameters the (m) stands for the month the (y) for the year and the (s)
        for the position. It prints the days of the month and returns the last postion or day the month stopped in"""
    i = 1
    j = 0

    # Declares and initializes a static variable k to save the position of the last day in the month
    print_days.k = 0

    while i <= get_days(m,y):
        # Prints a space until it finds where the month starts
        if(i == 1 and s != 7):
            while(j != s):
                print("   ", end= ' ')
                j = j + 1

        # Prints the number
        if(j < 7):
            print("%2i" %(i), end='  ')
            i = i + 1
            j = j + 1
            print_days.k = j

        else:
            j = 0
            print()
            print_days.k = j

    return print_days.k

def display(y):
    """The display function accepts one parameter (y) the year. It creates a file and sets the system output to
        print to the file. It then calls the find_month, week, find_start, and print_days functions. It closes the
        file and returns the output to the console or screen"""
    i = 1

    # Creates a file
    filex = 'calendar' + str(y) + '.txt'

    # Assigns the output to the file
    sys.stdout= open(filex, "w")

    while i <= 12:
        print(find_month(i, y))
        print(week())

        if(i == 1):
            s = find_start(y)

        s = print_days(i, y, s)

        i = i+1
    # Closes the file
    sys.stdout.close()

    # Returns the output to the screen or console
    sys.stdout = sys.__stdout__


if __name__ == '__main__':
#Calls the ask function
    ask()



























