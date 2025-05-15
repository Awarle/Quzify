"""Module quiz.
Ce module définit les classes Question et Quiz pour gérer un quiz.
"""

__author__ = "gueneb_a"

import json


class Question:
    """Représente une question de quiz."""

    def __init__(self, id: int, theme: str, question: str,
                 options: list, reponse: str):
        """
        Initialise une question.

        Args:
            id (int): L'identifiant de la question.
            theme (str): Le thème de la question.
            question (str): Le texte de la question.
            options (list): Liste des options proposées.
            reponse (str): La réponse correcte.
        """
        self.id = id
        self.theme = theme
        self.question = question
        self.options = options
        self.reponse = reponse

    def ask(self) -> bool:
        """
        Affiche la question et attend la réponse de l'utilisateur.

        Returns:
            bool: True si la réponse est correcte, False sinon.
        """
        print(f"\n{self.question}")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
        reponse_utilisateur = input("Votre réponse (numéro) : ").strip()
        try:
            index = int(reponse_utilisateur) - 1
            if index < 0 or index >= len(self.options):
                print("Réponse invalide.")
                return False
            if self.options[index] == self.reponse:
                print("Correct !")
                return True
            else:
                print(f"Faux ! La bonne réponse était : {self.reponse}")
                return False
        except ValueError:
            print("Entrée non valide.")
            return False


class Quiz:
    """Gère l'ensemble des questions d'un quiz."""

    def __init__(self, questions: list):
        """
        Initialise un quiz.

        Args:
            questions (list): Liste d'objets Question.
        """
        self.questions = questions
        self.theme = questions[0].theme if questions else "Général"

    @classmethod
    def load_from_file(cls, filepath: str) -> "Quiz":
        """
        Charge les questions depuis un fichier JSON.

        Args:
            filepath (str): Chemin du fichier JSON.

        Returns:
            Quiz: Un objet Quiz contenant les questions chargées.
        """
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            questions = []
            for item in data:
                q = Question(
                    id=item.get("id"),
                    theme=item.get("theme"),
                    question=item.get("question"),
                    options=item.get("options"),
                    reponse=item.get("reponse")
                )
                questions.append(q)
            return cls(questions)
        except Exception as e:
            print("Erreur lors du chargement du quiz :", e)
            return cls([])

    def administer(self) -> tuple:
        """
        Administre le quiz en posant toutes les questions à l'utilisateur.

        Returns:
            tuple: (score, nombre_correct, nombre_total)
        """
        correct = 0
        total = len(self.questions)
        for q in self.questions:
            if q.ask():
                correct += 1
        score = int((correct / total) * 100) if total > 0 else 0
        return score, correct, total
