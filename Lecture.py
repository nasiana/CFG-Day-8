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
pcn_date = input("Enter the date you were issued PCN as DDMMYYYY")
pcn_date_formatted = datetime.strptime(pcn_date, '%d%m%Y')
pcn_date_readable = pcn_date_formatted.date().strftime("%d %b %Y")
# printing initial_date
print("The PCN was issued: {}".format(pcn_date_readable))

# Calculating future dates
# for two years
deadline = pcn_date_formatted + timedelta(days=14)
deadline_formatted = deadline.date().strftime("%d %b %Y")
# printing calculated future_dates
print("The deadline for paying the reduced PCN charge is: {}".format(deadline_formatted))

print("If you pay the PCN penalty by *{}, the amount will be reduced to £65. After that it will be £130"\
    .format(deadline_formatted))

# make this an if-else statement
import datetime
current_time = datetime.datetime.now()
print("Today's date:", current_time)

if current_time < deadline:
    print("As you have paid by {}, you will only have to pay a PCN fine of £65".format(deadline_formatted))
else:
    print("You were issued a PCN on {}. As you have failed to pay by {}, you must pay a PCN fine of £130"\
          .format(pcn_date_readable, deadline_formatted))



    