### Trello
https://trello.com/invite/b/6808a4fcd356f64015eea791/ATTI7c9ea6917b8b5e9f72b8033676076e41817B07D7/devopsboardgroupe12

## Calculatrice en Ligne de Commande
![Python Tests](https://github.com/Tamim94/Calculatrice/workflows/Python%20Tests/badge.svg)
Un projet Python simple qui implémente une calculatrice avec interface en ligne de commande permettant d'effectuer des opérations mathématiques de base.

### Fonctionnalités
Addition de deux nombres
Soustraction de deux nombres
Multiplication de deux nombres
Division de deux nombres (avec gestion de la division par zéro)
Interface en ligne de commande intuitive
### Prérequis
Python 3.6 ou version ultérieure
### Structure du Projet
```plaintext
calculator/
│
├── calculator/
│   ├── __init__.py
│   ├── calculator.py   # Fonctions mathématiques
│   └── cli.py          # Interface en ligne de commande
│
├── tests/
│   ├── __init__.py
│   └── test_calculator.py  # Tests unitaires
│
├── main.py             # Point d'entrée du programme
└── README.md           # Ce fichier
```
Installation
Cloner ce dépôt :

git clone https://github.com/Tamim94/calculatrice-cli.git
cd calculatrice-cli

(Optionnel) Créer et activer un environnement virtuel :
```plaintext
python -m venv venv
```
# Sur Windows:
```plaintext
venv\Scripts\activate
```
# Sur macOS/Linux:
```plaintext
source venv/bin/activate
```
Utilisation
Exécutez le programme avec les arguments suivants :

Le nom de l'opération : addition, soustraction, multiplication ou division
Le premier nombre
Le deuxième nombre
Exemples
### Addition
```plaintext
python main.py addition 5 3
# Résultat: 8.0
```
### Soustraction
```plaintext
python main.py soustraction 10 4
# Résultat: 6.0
```
### Multiplication
```plaintext
python main.py multiplication 6 7
# Résultat: 42.0
```

### Division
```plaintext
python main.py division 20 5
# Résultat: 4.0
```

# Workflow CI/CD (GitHub Actions)
Ce projet utilise GitHub Actions pour l'intégration et la vérification continues. Le workflow est défini dans .github/workflows/python-tests.yml.  
Déclencheurs : Le workflow s'exécute à chaque push ou pull_request sur la branche master.
Job test :
Configure l'environnement Python.
Installe les dépendances (si requirements.txt existe).
Effectue le linting du code avec flake8.
Exécute les tests unitaires (unittest discover).
Calcule la couverture de test (coverage).
Teste la fonctionnalité de base via l'interface en ligne de commande (main.py).
Job deploy (Vérification du déploiement) :
S'exécute uniquement après le succès du job test et sur un push vers la branche master.
Configure l'environnement Python et installe les dépendances.
Effectue une vérification supplémentaire de la fonctionnalité de l'application en exécutant des commandes CLI spécifiques.
Génère un résumé de la vérification dans le rapport du workflow GitHub Actions.
Le badge en haut de ce README indique l'état actuel du workflow sur la branche master.