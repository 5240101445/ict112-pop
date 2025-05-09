"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# 1. Reverse the string "Programming"
text = "Programming"
reversed_text = text[::-1]
print("1. Reversed string:", reversed_text)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# 2. Get user's full name and print initials in uppercase
full_name = input("2. Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.strip().split()]) + "."
print("   Initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string 
"""
# 3. Check if a given string is a palindrome
word = input("3. Enter a word to check if it's a palindrome: ")
if word == word[::-1]:
    print("   It's a palindrome.")
else:
    print("   It's not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into 
"""
# 4. Count the number of words in a sentence
sentence = input("4. Enter a sentence: ")
word_count = len(sentence.strip().split())
print("   Word count:", word_count)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# 5. Replace "is" with "was" in a given string
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print("5. Modified string:", modified_string)



