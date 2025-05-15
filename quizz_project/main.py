"""Module main.
Point d'entrée du programme interactif de quiz.
"""

__author__ = "gueneb_a"


import os
from quizz import Quiz
from user import UserManager
import utils


def main_menu() -> str:
    """Affiche le menu interactif et retourne le choix de l'utilisateur."""
    print("\n=== Générateur de Quiz ===")
    print("1. Jouer au quiz")
    print("2. Voir mes résultats")
    print("3. Quitter")
    choix = input("Votre choix : ")
    return choix.strip()


def play_quiz():
    """Permet à l'utilisateur de jouer un quiz."""
    username = input("Entrez votre nom d'utilisateur : ").strip()
    questions_file = os.path.join("data", "questions.json")
    if not os.path.exists(questions_file):
        print("Le fichier de questions est introuvable.")
        return

    quiz = Quiz.load_from_file(questions_file)
    if not quiz.questions:
        print("Aucune question n'est disponible dans le quizz.")
        return

    print(f"\nThème du quizz : {quiz.theme}")
    score, correct, total = quiz.administer()
    print(
        f"\nRésultat : {score} points sur 100 "
        f"({correct}/{total} bonnes réponses)"
    )

    user_file = os.path.join("data", "utilisateurs.json")
    user_manager = UserManager(user_file)
    user_manager.update_user(username, quiz.theme, score)


def view_results():
    """Affiche les résultats de l'utilisateur enregistrés."""
    username = input("Entrez votre nom d'utilisateur : ").strip()
    user_file = os.path.join("data", "utilisateurs.json")
    user_manager = UserManager(user_file)
    results = user_manager.get_user_results(username)
    if results:
        print(f"\nRésultats pour {username} :")
        for res in results:
            print(
                f"Thème : {res['theme']}, Score : {res['score']}, "
                f"Date : {res['date']}"
            )
    else:
        print("Aucun résultat trouvé pour cet utilisateur.")


def main():
    """Boucle principale du menu interactif."""
    while True:
        choix = main_menu()
        if choix == "1":
            play_quiz()
        elif choix == "2":
            view_results()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
