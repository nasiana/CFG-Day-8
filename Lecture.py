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

# exercise
user_word = input("Give me a word")
for i in range(5):
    user_encoding = "ABCDEF"
    print(user_encoding.join(user_word))