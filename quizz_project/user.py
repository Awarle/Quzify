"""Module user.
Ce module gère les utilisateurs et la sauvegarde de leurs scores
dans un fichier JSON.
"""

__author__ = "gueneb_a"


import json
import os
import datetime


class UserManager:
    """Gère la lecture et l'écriture des scores utilisateurs."""

    def __init__(self, filepath: str):
        """
        Initialise le gestionnaire d'utilisateurs.

        Args:
            filepath (str): Chemin du fichier JSON de sauvegarde.
        """
        self.filepath = filepath
        self.users = {}
        self.load()

    def load(self):
        """Charge les utilisateurs depuis le fichier JSON."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    self.users = json.load(f)
            except Exception as e:
                print("Erreur lors du chargement des utilisateurs :", e)
                self.users = {}
        else:
            self.users = {}

    def save(self):
        """Sauvegarde les utilisateurs dans le fichier JSON."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.users, f, indent=4)
        except Exception as e:
            print("Erreur lors de la sauvegarde des utilisateurs :", e)

    def update_user(self, username: str, theme: str, score: int):
        """
        Ajoute un score pour l'utilisateur donné.

        Args:
            username (str): Nom de l'utilisateur.
            theme (str): Thème du quiz.
            score (int): Score obtenu.
        """
        today = str(datetime.date.today())
        if username not in self.users:
            self.users[username] = {"scores": []}
        result = {"theme": theme, "score": score, "date": today}
        self.users[username]["scores"].append(result)
        self.save()

    def get_user_results(self, username: str) -> list:
        """
        Retourne les scores de l'utilisateur.

        Args:
            username (str): Nom de l'utilisateur.

        Returns:
            list: Liste des scores enregistrés pour l'utilisateur.
        """
        return self.users.get(username, {}).get("scores", [])
