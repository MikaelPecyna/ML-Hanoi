
<p align="center">
	<img src="asset/python-logo.png" alt="Logo Python" height="60" style="margin-right: 30px;"/>
	<img src="asset/POITIERS-UNIVERSITE-CMJN-2014.png" alt="Logo Université de Poitiers" height="60" style="margin: 0 30px;"/>
	<img src="asset/OIP.flo3TJvE-Fb8I1TsmJn8DAAAAA.webp" alt="Logo UFR" height="60" style="margin-left: 30px;"/>
</p>


# 🏗️ Tour de Hanoï – Intelligence Artificielle & Simulation

## 📑 Table des matières

- [🏗️ Tour de Hanoï – Intelligence Artificielle \& Simulation](#️-tour-de-hanoï--intelligence-artificielle--simulation)
  - [📑 Table des matières](#-table-des-matières)
- [🇬🇧 Tower of Hanoi – AI \& Simulation](#-tower-of-hanoi--ai--simulation)
  - [📑 Table of Contents](#-table-of-contents)
  - [🚀 Overview](#-overview)
  - [📂 Project Structure](#-project-structure)
  - [🧩 Main Features](#-main-features)
  - [🛠️ Usage](#️-usage)
  - [📖 Code Example](#-code-example)
  - [🧠 Key Concepts](#-key-concepts)
  - [✨ Customization](#-customization)
  - [👨‍💻 Author](#-author)
  - [📜 License](#-license)
  - [🚀 Présentation](#-présentation)
  - [📂 Structure du projet](#-structure-du-projet)
  - [🧩 Fonctionnalités principales](#-fonctionnalités-principales)
  - [🛠️ Utilisation](#️-utilisation)
  - [📖 Extrait de code](#-extrait-de-code)
  - [🧠 Concepts clés](#-concepts-clés)
  - [✨ Personnalisation](#-personnalisation)
  - [👨‍💻 Auteur](#-auteur)
  - [📜 Licence](#-licence)
# 🇬🇧 Tower of Hanoi – AI & Simulation

<details>
<summary>Click to expand English version</summary>

<p align="center">
	<img src="asset/python-logo.png" alt="Python Logo" height="60" style="margin-right: 30px;"/>
	<img src="asset/POITIERS-UNIVERSITE-CMJN-2014.png" alt="Poitiers University Logo" height="60" style="margin: 0 30px;"/>
	<img src="asset/OIP.flo3TJvE-Fb8I1TsmJn8DAAAAA.webp" alt="UFR Logo" height="60" style="margin-left: 30px;"/>
</p>

## 📑 Table of Contents

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Main Features](#-main-features)
- [Usage](#-usage)
- [Code Example](#-code-example)
- [Key Concepts](#-key-concepts)
- [Customization](#-customization)
- [Author](#-author)
- [License](#-license)

## 🚀 Overview

This project offers a complete simulation and automatic solver for the classic Tower of Hanoi puzzle, featuring:
- An efficient data structure to represent the game state
- Utility functions for manipulation and analysis
- An automatic solving algorithm with step-by-step tracing
- Beautiful console output to visualize the game

## 📂 Project Structure

```
Hanoi/
│
├── JeuHanoi.py         # Main class for game management and display
├── utils.py            # Utility functions (rules, situations, moves...)
├── main.py             # Main script: automatic solving and display
├── README.md           # This file!
└── ...                 # (tests, notebooks, etc.)
```

## 🧩 Main Features

- **Faithful simulation** of the Tower of Hanoi (3 pegs, 3 disks)
- **Readable and aesthetic console display** of each state
- **Detection of already encountered situations** to avoid cycles
- **Strict rule enforcement** (no larger disk on a smaller one)
- **Move history** and step count

## 🛠️ Usage

1. **Install dependencies**

Only `numpy` is required (usually included in scientific Python distributions):

```bash
pip install numpy
```

2. **Run the simulation**

In the project folder, run:

```bash
python main.py
```

You will see each step of the solution, with the game state after every move.

## 📖 Code Example

```python
from JeuHanoi import JeuHanoi
from utils import *

jeu = JeuHanoi()
jeu.nombre_palet[0] = 3
jeu.pic[0,0] = 3
jeu.pic[0,1] = 2
jeu.pic[0,2] = 1
jeu.printJeu()
```

## 🧠 Key Concepts

- **Binary encoding of situations** for fast duplicate detection
- **Move simulation** on copies to test validity
- **Clear separation** between game logic and utilities

## ✨ Customization

You can easily:
- Change the number of disks (adapt the class and utilities)
- Change the rule order in `main.py` to explore other strategies
- Add tests or visualizations

## 👨‍💻 Author

Mikael Pecyna  
Master 2 – Machine Learning  
Université de Lille

## 📜 License

Academic project – free to use and modify for educational purposes.

</details>

Bienvenue dans ce projet Python de simulation et de résolution automatique du célèbre casse-tête de la Tour de Hanoï !

## 🚀 Présentation

Ce projet propose une modélisation complète du jeu de la Tour de Hanoï, avec :
- Une structure de données efficace pour représenter l’état du jeu
- Des fonctions utilitaires pour manipuler et analyser les situations
- Un algorithme automatique de résolution, traçant chaque étape
- Un affichage graphique en console pour suivre l’évolution du jeu

## 📂 Structure du projet

```
Hanoi/
│
├── JeuHanoi.py         # Classe principale de gestion du jeu et de l’affichage
├── utils.py            # Fonctions utilitaires (règles, situations, déplacements...)
├── main.py             # Script principal : résolution automatique et affichage
├── README.md           # Ce fichier !
└── ...                 # (tests, notebooks, etc.)
```

## 🧩 Fonctionnalités principales

- **Simulation fidèle** de la Tour de Hanoï (3 pics, 3 disques)
- **Affichage console** lisible et esthétique de chaque état
- **Détection des situations déjà rencontrées** pour éviter les cycles
- **Respect strict des règles** (aucun disque plus grand sur un plus petit)
- **Historique des coups** et nombre d’étapes

## 🛠️ Utilisation

1. **Installation des dépendances**

Ce projet nécessite uniquement `numpy` (installé par défaut dans la plupart des distributions scientifiques Python) :

```bash
pip install numpy
```

2. **Lancement de la simulation**

Dans le dossier du projet, exécutez :

```bash
python main.py
```

Vous verrez s’afficher chaque étape de la résolution, avec l’état du jeu après chaque coup.

## 📖 Extrait de code

```python
from JeuHanoi import JeuHanoi
from utils import *

jeu = JeuHanoi()
jeu.nombre_palet[0] = 3
jeu.pic[0,0] = 3
jeu.pic[0,1] = 2
jeu.pic[0,2] = 1
jeu.printJeu()
```

## 🧠 Concepts clés

- **Codage binaire des situations** pour une détection rapide des doublons
- **Simulation de coups** sur des copies pour tester la validité
- **Séparation claire** entre logique du jeu et utilitaires

## ✨ Personnalisation

Vous pouvez facilement :
- Modifier le nombre de disques (adapter la classe et les utilitaires)
- Changer l’ordre des règles dans `main.py` pour explorer d’autres stratégies
- Ajouter des tests ou des visualisations

## 👨‍💻 Auteur

Mikael Pecyna  
Master 2 – EUR Software Design and Development 
Université de Poitiers 

## 📜 Licence

Projet académique – libre d’utilisation et de modification à des fins pédagogiques.
