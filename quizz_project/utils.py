"""Module utils.
Ce module contient des fonctions utilitaires.
"""

__author__ = "gueneb_a"


def clear_screen():
    """Efface la console."""
    import os
    os.system("cls" if os.name == "nt" else "clear")
