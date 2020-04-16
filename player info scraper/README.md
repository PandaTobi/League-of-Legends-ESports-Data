Pseudocode for retrieve_player_data.py's Future:
file = file(links.txt)
while True:
    name = Ask for name
    for line in file:
        if the line ends with name

Goal:
Asking for names in a while True loop. Iterating through the links.txt file to check what link
corresponds with that name (if there is no link try: suggesting names that have the similar 
letters[1])

[1]: Okay, so my idea is that you can check what entries have the same first letters. It'll be
a pain to extract the names from the linkNames file, so I'll create a new txt file (names.txt
will serve this purpose). 
###Edit: jkjk using levesomething distance to find "similarity-level" between the inputted
name and the names we will iterate through. Likely, I can simplify this. Basic algorithm will be
found below. Note that the simplified version will be much less robust than the leve-thing
algorithm (here's the link: https://www.datacamp.com/community/tutorials/fuzzy-string-python)
as if they aren't equal in length, so putting the function in a seperate script and importing
it is always a possiblility.

def string_differences(string1, string2)
    if len(string1) == len(string2):
        for i
