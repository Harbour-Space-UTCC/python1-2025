# count
word = "Peepat loves Shinshin"
print(word.count("in"))
print(word.count(" "))
print(word.count("shin"))

# replace
# new_word = word.replace("e", "o")
# new_word = word.replace("Shinshin", "Sigma")
new_word = word.replace(" ", "")
print(new_word)

print(word.upper())
print(word.capitalize())
print(word.lower())

word = "Peepat loves arm"
word = """
Peep\tat
lov  es
arm
"""
# any number of spaces
# any number of \n \t
print(word.split())

word = "ABCDE"
print(word.isalpha())

