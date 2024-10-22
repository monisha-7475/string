'''
Write a  Python Program to calculate the number of words and characters present in a string.
Input & Output Format:
Input consists of a string.
Output consists of two integers.
First output refers to the count of the words.
Second output refers to the count of the characters in a given string,
'''
def count_words_and_characters(input_string):
    words = input_string.split()
    word_count = len(words)
    character_count = len(input_string)
    print(word_count)
    print(character_count)
user_input = input("Enter a string: ")
count_words_and_characters(user_input)
