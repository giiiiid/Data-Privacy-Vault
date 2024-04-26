import re
import nltk
import bcrypt

word = "I am good"

# tokens = re.findall(r's+', word)
# print(tokens)
tokens = word.split(" ")
print(tokens)

user = str(input("type a word: "))
if user in tokens:
    print(True)
