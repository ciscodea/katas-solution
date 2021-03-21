"""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

"""

def solution(s):
    n = 2
    list = [s[i:i+n] for i in range(0, len(s), n)]
    
    for i in range(len(list)):
        if len(list[i]) == 1:
                   list[i] = list[i] + '_'
                
    return list
        
        
"""
Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
"""

def order(sentence):
    if sentence == "":
        return sentence
    else:        
        list = ["","","","","","","","","",""]
        for i in sentence.split():
            for j in i:
                if j.isdigit():
                    list[int(j)] = i
                    
        list.remove("")
        str = " ".join(x for x in list)
        
    return str.strip()

"""
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""
from collections import Counter

def find_it(seq):
    
    dir = dict((i, seq.count(i)) for i in seq)
    
    for key in dir:
        if dir[key] % 2 != 0:
            return key
    
   
"""
Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. 
Young B knows she runs faster than A, and furthermore has not finished her cabbage.
When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. 
How long will it take B to catch A?
More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?
The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the nearest second) or a string in some languages.
If v1 >= v2 then return nil,
"""
def race(v1, v2, g):
    if v1 >= v2:
        return None
    if v1 > 0 and v2 > 0 and g > 0:
        diference = v2 - v1
        seconds = (g * 3600) / diference 
        return [int(seconds / 3600), int((seconds % 3600) / 60), int(seconds % 60)]
"""
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
import string

def is_pangram(s):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in alphabet:
        if char not in s.lower():
            return False
        
    return True
            
"""
n this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
"""
def alphabet_position(text):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = text.lower()
    text = text.replace(" ", "")
    alphabet_position = ""
    for letter in text:
          
        try:
            position = alphabet.index(letter) + 1
            alphabet_position += str(position) + " "
        except:
            print("")
    return alphabet_position.strip()

"""
Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
"""
def spin_words(sentence):
    result = []
    for word in sentence.split():
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)


"""
Find the missing term in an Arithmetic Progression

You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.
"""

def find_missing(sequence):
    n = sequence[1] - sequence[0]
    n = sequence[2] - sequence[1]

    for i in range(0, len(sequence)):
        if sequence[i] + n == sequence[i+1]:
            continue
        else:
            return sequence[i] + n
