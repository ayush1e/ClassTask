# 1. unique element function
l = [1,2, 2, 3, 4, 1, 5]
def unique_elements(lst):
    return list(set(lst))

print("Unique elements in the list:\n")
print(unique_elements(l))

#2. list rotation

def reverse_list(list, i, j):
    while(i < j):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        i += 1
        j -= 1

list1 = [1,2,3,4,5]

def rotate_list(lst, d):
    n = len(lst)
    d = d % n   
    reverse_list(lst, 0, n-1)
    reverse_list(lst, 0, d-1)
    reverse_list(lst, d, n-1)
    return lst

print("\nRotated list:\n")
print(rotate_list(list1, 2))


#3find the longest word

sentence = "Python is an amazing programming language"
longest_word = ""
for word in sentence.split():
    if(len(word) > len(longest_word)):
        longest_word = word

print("Longest word:", longest_word)


# 4. Sum of digit function

def sumOfDigits(n):
    total = 0
    while(n > 0):
        total = total + (n % 10)
        n //= 10
    return total

print("Sum of digits in 12345:", sumOfDigits(12345))

#5 . character frequency
def charFrequency(str):
    freq = {}
    for char in str:
        freq[char] = freq.get(char, 0) + 1
    return freq

print("Character frequency in 'hello world':")
print(charFrequency("hello world"))


#6. number divisible by 3 or 5

def divisible_by_3_or_5(n):
    if n < 0:
        print("Please enter a positive number")
    else:
        return [i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0]

print("Numbers divisible by 3 or 5 up to 100:")
print(divisible_by_3_or_5(100))



#7. reverse words in a string

def reverse_words(s):
    words = s.split()
    words.reverse()
    return ' '.join(words)

print("Reversed words in the string:")
print(reverse_words("Python is fun"))

#8.  *
#   ***
#  ***** print diamond pattern


for i in range(1, 4):
    for j in range(3, i, -1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()


#9 . count consonants
def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char not in vowels and char.isalpha():
            count += 1
    return count

print("Number of consonants in 'Hello World':", count_consonants("Hello World"))


#10. number guessing game random function

import random

def number_guessing_game():
    num = random.randint(1, 5)
    attempts = 0
    while True:
        guess = int(input("Guess the number (between 1 and 5): "))
        attempts += 1
        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {num} in {attempts} attempts.")
            break

number_guessing_game()
