from english_words import english_words_lower_set
import random

words_list = list(english_words_lower_set)
wguess = random.choice(words_list)
vguess = ["_"] * len(wguess)


def looser(penalty):
    if penalty >= 12:
        print("You lose!")
        return False
    else:
        return True


def hangman():
    penalty = 0
    while looser(penalty):
        print(" ".join(vguess))
        user_input = input(
            f"Enter a letter or the whole word (Penalties left: {12 - penalty}): "
        ).lower()

        if len(user_input) == 1:
            if user_input in wguess:
                for i, char in enumerate(wguess):
                    if char == user_input:
                        vguess[i] = user_input
            else:
                penalty += 1
                print(f"Wrong letter! {12 - penalty} penalties left.")

        else:
            if user_input == wguess:
                print("You win!")
                break
            else:
                penalty += 5
                print(
                    f"Wrong word! You lose 5 penalties. {12 - penalty} penalties left."
                )

        if "".join(vguess) == wguess:
            print("You win!")
            break
        elif not looser(penalty):
            print(f"You lose :(, the word was: {wguess}")
            break


hangman()
# Importation du module english_words pour accéder à la liste des mots anglais en minuscules
# Importation du module random pour choisir un mot aléatoire

# Conversion du set english_words_lower_set en liste pour pouvoir utiliser random.choice
# Sélection aléatoire d'un mot dans la liste words_list, stocké dans wguess
# Initialisation de vguess comme une liste de underscores "_", un par lettre du mot à deviner

# Définition de la fonction looser qui vérifie si le joueur a perdu
#   - Si le nombre de pénalités est >= 12, affiche "You lose!" et retourne False (fin de partie)
#   - Sinon, retourne True (la partie continue)

# Définition de la fonction hangman, cœur du jeu
#   - Initialisation de penalty à 0 (nombre d'erreurs du joueur)
#   - Boucle while qui continue tant que looser(penalty) retourne True
#     - Affiche l'état actuel du mot (lettres devinées et underscores)
#     - Demande à l'utilisateur d'entrer une lettre ou le mot entier, en affichant les pénalités restantes
#     - Si l'entrée fait 1 caractère (une lettre)
#       - Si la lettre est dans le mot, remplace les underscores correspondants par la lettre
#       - Sinon, incrémente penalty de 1 et affiche le nombre de pénalités restantes
#     - Si l'entrée fait plusieurs caractères (tentative de deviner le mot entier)
#       - Si le mot est correct, affiche "You win!" et sort de la boucle
#       - Sinon, incrémente penalty de 5 et affiche le nombre de pénalités restantes
#     - Si toutes les lettres sont devinées (vguess rejoint wguess), affiche "You win!" et sort de la boucle
#     - Si looser(penalty) retourne False, affiche le mot et "You lose :(" puis sort de la boucle

# Appel de la fonction hangman pour lancer le jeu