'''
Write a Python Program to remove the nth index character from a non-empty string.
Input & Output Format:
Input consists of a string and one integer.
The first input consists of a string.
The second input refers to the index position.
The output consists of a string.
'''
def remove_nth_character(input_string, index):
    if index < 0 or index >= len(input_string):
        return "Invalid index."
    new_string = input_string[:index] + input_string[index + 1:]
    return new_string
user_input = input("Enter a string: ")
index_input = int(input("Enter the index position to remove: "))
result = remove_nth_character(user_input, index_input)
print("String after removing the character:", result)

