# Check if a word is an anagrams
# Example:
# find_anagrams1=("hello", "ellion") --> False
# find_anagrams2=("racecar", "car race") --> True


def find_anagrams(word, anagram):
    word = input("Enter the first anagrams word: ")
    anagram = input("Enter the second anagram word: ")
    # [assignment] Add your code here
    if sorted(word.strip().lower()) == sorted(anagram.strip().lower()):
        return ("Anagram is correct")
    else:
        return ("Anagram is wrong")



print (find_anagrams("a", "b"))

