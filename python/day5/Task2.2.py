import re,string

word = input("Enter a string : ").lower().replace(' ', '')
rev_word = ''.join(reversed(word))
clean_word = re.sub(rf"[{string.punctuation}]", "", word)

if list(word) == list(rev_word):
    print("palindrome")
else:
    print(" not palindrome")

# On initialise word qui contient un string que l'on passe en minuscule et auquel on enleve les espaces et les caractères spéciaux
# On initialise le rev_word qui est simplement la string word mais à l'envers grace à reversed
# On vérifie si notre word est égal à notre rev_word


#Renvoit true si palindrome
def task2_2(text):
    text = re.sub(r"[^A-Za-z]", "", text)
    text = text.lower()
    reversed_text = text[::-1]
    return text == reversed_text

