"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: David Krbušek
email: davidkrbusek@gmail.com
"""

users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123"]
Texts = [
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley""",
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present"""
]

# Začátek programu
# Přihlášení a ověření uživatele 
input_user = isinstance((f"Enter username: "), str) and input(f"Enter username: ").lower()
input_password = input(f"Enter password: ")
print("-" * 41)
if input_user in users and input_password in passwords:
    print(f"Welcome to the app, {input_user.title()}!")
    print("We have 3 texts to be analyzed.")
else:
    print(f"Unregistered user, terminating the program for {input_user.title()}")
    exit()
print("-" * 41)

# Výběr text k analýze + ověření vstupu
input_text = input(f"Enter a number btw. (1-{len(Texts)}) to select: ")
print("-" * 41)
if not input_text.isdigit():
    print("Invalid input, not a number, terminating the program")
    exit()
if int(input_text) not in range(len(Texts) + 1):
    print("Invalid input, number not in range, terminating the program")
    exit()

# Analýza textu
word_list = Texts[int(input_text) - 1].split()
sample = {}
for word in word_list:
    non_dot_word = word.strip(",.")
    if non_dot_word not in sample:
        sample[non_dot_word] = 1    
    else:
        sample[non_dot_word] += 1  

# Výpis výsledků analýzy
print(f"There are {len(word_list)} words in the selected text.") # Počet slov v textu
print(f"There are {len([word for word in word_list if word.istitle()])} titlecase words in the text.") # Počet slov v textu s velkým počátečním písmenem;
print(f"There are {len([word for word in word_list if word.isupper()])} uppercase words in the text.") # počet slov v textu s velkými písmeny
print(f"There are {len([word for word in word_list if word.islower()])} lowercase words in the text.") # Počet slov v textu s malými písmeny
print(f"There are {len([word for word in word_list if word.isdigit()])} numeric strings.") # Počet čísel v textu
print(f"The sum of all the numbers is  {sum([int(word) for word in word_list if word.isdigit()])}") # Součet všech čísel v textu
print("-" * 41)

# Počet slov podle délky
print(f"LENGTH | OCCURRENCES      | NR. OF WORDS")
print("-" * 41)
length_fr = {}
for word in word_list:
    length = len(word)
    length_fr[length] = length_fr.get(length, 0) + 1

for length in sorted(length_fr.keys()):
    stars = '*' * length_fr[length]
    print(f"{length:>6} | {stars:>16} | {length_fr[length]:>12}")

print(f"Thank you for using the app, {input_user.title()}!")