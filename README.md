# Quizify
# Objectifs 🎯
Consolider toutes les notions vues pendant les deux semaines :
Structures fondamentales (variables, conditions, boucles, fonctions)
Programmation orientée objet (classes, héritage, polymorphisme, propriété)
Gestion avancée de fichiers (CSV, JSON)
Gestion des exceptions et erreurs
Algorithmes simples (tri, recherche, etc.)
Favoriser la modularité et la réutilisation du code

# Consignes 📌
Vous allez développer une application interactive de génération de quiz. L’utilisateur pourra répondre à des quiz thématiques, suivre sa progression, et ses résultats seront sauvegardés automatiquement.

🔑 Fonction clé : Utilisez la fonction input() pour créer un prompt interactif, clair et intuitif pour l'utilisateur.

🔧 Fonctions attendues (Base obligatoire)
1. Chargement et affichage d’un quiz
Charger les questions depuis un fichier JSON
Afficher les questions une par une et attendre la réponse utilisateur
2. Calcul automatique du score
Calculer le résultat du quiz
Afficher un résumé clair : score obtenu, réponses correctes/incorrectes
3. Sauvegarde des résultats
Enregistrer automatiquement le score et la progression dans un fichier utilisateurs.json
4. Menu interactif
Menu simple (jouer, voir résultats, quitter)
5. Gestion d’erreurs et exceptions
Traitement des erreurs utilisateurs (entrées incorrectes, fichiers absents, etc.)

# 🌟 Bonus (pour se challenger davantage)
Ajouter un timer pour limiter le temps de réponse à chaque question
Charger les questions depuis une API externe (par exemple Open Trivia Database)
Générer des quiz personnalisés en fonction des préférences utilisateur
Implémenter un scoreboard global (CSV) avec classement

# 🚩 Bonus de Bonus (niveau avancé)
Développement d'une interface graphique avec Tkinter ou d’une interface CLI stylisée avec Rich
Générer un système de recommandations intelligentes (questions les plus souvent ratées)
Création d’un système de badges/récompenses utilisateur

# 📂 Structure du projet
quiz_project/
├── main.py         # Point d'entrée du programme
├── quiz.py         # Classes Quiz, Question, etc.
├── user.py         # Gestion des utilisateurs et scores
├── utils.py         # Fonctions utilitaires
├── data/
│  ├── questions.json    # Banque des questions
│  └── utilisateurs.json  # Progression des utilisateurs
└── bonus/
  ├── timer.py       # Gestion du temps (bonus)
  ├── api.py        # Requête API externe (bonus)
  └── scoreboard.csv    # Tableau des scores global (bonus)
  
# 📁 Exemples de fichiers
# ✅ Exemple de questions.json
[
 {
  "id": 1,
  "theme": "Python",
  "question": "Quelle est la sortie de print(type(3)) ?",
  "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"],
  "reponse": "<class 'int'>"
 },
 {
  "id": 2,
  "theme": "Histoire",
  "question": "En quelle année Christophe Colomb a-t-il découvert l'Amérique ?",
  "options": ["1492", "1620", "1776", "1945"],
  "reponse": "1492"
 }
]

# ✅ Exemple de utilisateurs.json
{
 "Alice": {
  "scores": [
   {"theme": "Python", "score": 80, "date": "2024-04-15"},
   {"theme": "Histoire", "score": 60, "date": "2024-04-15"}
  ]
 },
 "Bob": {
  "scores": [
   {"theme": "Python", "score": 100, "date": "2024-04-15"}
  ]
 }
}

# ✅ Exemple de scoreboard.csv (bonus)
Utilisateur,Theme,Score,Date
Alice,Python,80,2024-04-15
Alice,Histoire,60,2024-04-15
Bob,Python,100,2024-04-15

# 🚀 Conclusion et conseils
Commencez par réaliser les fonctionnalités obligatoires, testez-les, puis attaquez les bonus.
Travaillez par modules (fichiers séparés) pour garder un code clair et modulaire.
Utilisez Git tout au long pour sauvegarder régulièrement votre avancement.
Bon courage et surtout : prenez plaisir à coder ! 🎉
