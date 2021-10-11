# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# demo 1
# input always returns a string value
name = input('What is your name? ')
print('Hello, {}'.format(name))

# exercise
friends = int(input("How many friends are there in total plus you?"))
pizzas = friends * 0.5

print('You need {} pizzas for {} friends'.format(pizzas, friends))

# for loops
for i in range(5):
    print(i)

# exercise, did myself
user_word = input("Give me a word")
for i in range(5):
    user_encoding = "ABCDEF"
    user_encoded = user_encoding.join(user_word)

print(user_encoded)

# While Loops

# exercise

from datetime import datetime, timedelta

# Using current time
pcn_date = input("Enter the date you were issued PCN as dd/mm/yyyy")
# printing initial_date
print("pcn_date", str(pcn_date))

pcn_date_formatted = datetime.strptime(pcn_date, '%d%m%Y')

# Calculating future dates
# for two years
future_date_after_14days = pcn_date_formatted + timedelta(days=14)

# printing calculated future_dates
print('future_date_after_14days', str(future_date_after_14days))

print("If you pay the PCN penalty by *{}, the amount will be reduced to £65".format(future_date_after_14days))

# make this an if-else statement