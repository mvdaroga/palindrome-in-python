import os
# Get the name of current folder
current_dir = os.path.dirname(os.path.abspath(__file__))
# Concatenate the path of current folder with the name of file 
path = os.path.join(current_dir, 'Dictionary.txt')
path_result = os.path.join(current_dir, 'PalindromeDictionary.txt')
# Create an array to store palindrome words
palindrome_elements = []
with open(path, "r") as target:
    for val in target:
        val = val.strip()
        if val.lower() == ''.join(reversed(val)).lower():
            print(val, ' is a palindrome')
            palindrome_elements.append(val)

# Write the palindrome word into new txt file
with open(path_result, 'w') as target:
    for val in palindrome_elements:
        target.write(val + '\n')
   