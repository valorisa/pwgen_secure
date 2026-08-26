# Générateur sécurisé de mots de passe et phrases de passe

---

## Description

**pwgen_secure** est un script Python interactif (mode console) permettant de générer :

- des **mots de passe** cryptographiquement sûrs (CSPRNG) avec contraintes **EXACTES** sur le nombre de minuscules, majuscules, chiffres et caractères spéciaux ;
- des **phrases de passe** composées de mots aléatoires tirés d'une wordlist (fichier ou wordlist embarquée) avec choix de séparateur (y compris caractères Unicode/Thaï) via un menu interactif.

Le script privilégie la sécurité : toutes les sélections aléatoires utilisent le module `secrets` de Python et le mélange final utilise `secrets.SystemRandom().shuffle()`.

---

## Prérequis

- Python 3.6 ou supérieur.
- Terminal supportant l'encodage UTF-8 (recommandé pour utiliser des séparateurs Unicode/Thaï).
- (Optionnel) Sous Termux : installer `termux-api` si vous souhaitez copier directement dans le presse‑papiers (`termux-clipboard-set`).

---

## Installation (Termux / Linux / macOS)

1. Ouvrez votre terminal.
2. Créez le répertoire de projet et placez‑vous dedans :

   ```bash
   cd ~/Projets
   mkdir -p pwgen_secure
   cd pwgen_secure
Créez le script password_generator.py. Par exemple, collez la version fournie par l'auteur dans un fichier ou utilisez la commande cat <<'EOF' qui a été fournie précédemment pour écrire le script.

Rendez le script exécutable :

bash

chmod +x password_generator.py
Lancez le script :

bash

./password_generator.py
# ou
python3 password_generator.py
Utilisation (menu interactif)
Au lancement, le script affiche un menu principal clair :

1) Générer 1 mot de passe (contraintes EXACTES possibles)

Saisissez la longueur (longueur minimale 25 enforced).
Indiquez le nombre EXACT de minuscules, MAJUSCULES, chiffres et spéciaux (0 pour aucune).
Indiquez les caractères spéciaux à exclure (laisser vide pour aucun ; utilisez <space> pour indiquer explicitement l'espace).
Le script valide que la somme des comptes EXACTS ne dépasse pas la longueur demandée et génère le mot de passe voulu.
2) Générer un batch de mots de passe

Même interface que l'option 1, mais vous pouvez demander plusieurs éléments d'un coup. Le script imprime chaque mot de passe sur une ligne.
3) Générer une phrase de passe

Saisissez la longueur minimale en caractères (min 25).
Choisissez un séparateur via un menu prédéfini (espace, tiret, underscore, ponctuation, ou caractères Unicode/Thaï). Vous pouvez aussi saisir un séparateur personnalisé.
Indiquez un chemin vers une wordlist (un mot par ligne) ou laissez vide pour utiliser la wordlist embarquée.
Le script assemble des mots aléatoires jusqu'à atteindre la longueur minimale et au moins 3 mots.
4) Voir règles / exemples

Affiche des notes d'utilisation et des exemples (exclusion d'espace avec <space>, comportement si contraintes incompatibles, etc.).
5) Quitter

Quitte le programme proprement.
Exemples d'interaction
Exemple rapide : générer un mot de passe unique.

yaml

=== Menu principal ===
1) Générer 1 mot de passe (contraintes EXACTES possibles)
...
Choix (1-5): 1
Longueur souhaitée (défaut 25): 32
Nombre EXACT de minuscules (défaut 1): 10
Nombre EXACT de MAJUSCULES (défaut 1): 8
Nombre EXACT de CHIFFRES (défaut 1): 8
Nombre EXACT de SPECIAUX (défaut 1): 6
Caractères spéciaux à EXCLURE (...): <space>
Mot de passe généré:
aB3... (chaîne de 32 caractères)
Exemple : générer une phrase de passe avec séparateur Thaï.

yaml

Choix (1-5): 3
Longueur minimale totale en caractères (min 25) (défaut 25): 120
Sélectionnez un séparateur : (choisir le numéro correspondant au caractère Thaï)
Chemin vers wordlist (laisser vide pour default):
Phrase de passe générée:
arbre๗lune๗nuage๗...
Options et comportements importants
Longueur minimale : le script force une longueur minimale de 25 caractères pour les mots de passe et les phrases de passe afin d'améliorer la sécurité par défaut.
Exclusion de caractères spéciaux : indiquez les caractères à exclure (p. ex. \" ou \) ; pour exclure explicitement l'espace, saisissez <space>.
Contraintes EXACTES : le script permet de demander un nombre exact de caractères par catégorie (lower / upper / digits / special). La somme des comptes EXACTS ne doit pas dépasser la longueur. Si elle est inférieure, le reste est rempli avec un alphabet complet filtré.
Wordlist : par défaut, une petite wordlist embarquée est utilisée. Pour de meilleures phrases de passe, fournissez une wordlist riche (par exemple la liste EFF/Diceware formatée).
Sécurité et bonnes pratiques
Toujours utiliser secrets (CSPRNG) pour générer des secrets : ce script suit cette recommandation.
Ne stockez jamais de mots de passe en clair dans un dépôt public. Si vous exportez un batch, protégez le fichier (permissions strictes, chiffrement).
Préférez copier les mots de passe dans un gestionnaire de mots de passe sécurisé (Bitwarden, 1Password, KeePassXC).
Attention aux caractères spéciaux problématiques dans certains systèmes (ex. " ou \) : excluez-les si nécessaire.
Les phrases de passe basées sur une wordlist de qualité (Diceware/EFF) fournissent une bonne entropie si les mots sont choisis correctement.
Optionnel — installer globalement / alias
Rendre le script accessible depuis n'importe où :

bash

# Copier dans ~/bin et rendre exécutable
mkdir -p ~/bin
cp ~/Projets/pwgen_secure/password_generator.py ~/bin/pwgen_secure
chmod +x ~/bin/pwgen_secure

# S'assurer que ~/bin est dans le PATH (ajoutez ceci à ~/.profile ou ~/.bashrc si nécessaire)
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.profile
source ~/.profile

# Optionnel : créer un alias
echo "alias pwgen='pwgen_secure'" >> ~/.bashrc
source ~/.bashrc
Ensuite lancez simplement :

bash

pwgen
# ou
pwgen_secure
Export en lot (CSV/JSON)
Le script fourni est interactif. Si vous souhaitez un mode non-interactif (par ex. --count, --length, --exact-upper, --csv out.csv), il est possible d'ajouter des arguments CLI et une option d'export CSV/JSON pour intégrer le script dans des workflows/CI. Indiquez le format souhaité et le comportement (écrire en mode append, écraser, inclure métadonnées, etc.).

Personnalisation
Remplacez ou étendez la wordlist embarquée dans le script ou fournissez un fichier words.txt dans le répertoire ~/Projets/pwgen_secure et indiquez son chemin à l'exécution.
Modifiez la fonction choose_separator() pour y insérer vos propres caractères Thaï (ou toute autre liste).
Si vous souhaitez interdire des répétitions de caractères, ou forcer des distributions plus strictes, ces règles peuvent être ajoutées.
Dépannage
Encodage / caractères étranges : assurez-vous que votre terminal utilise UTF-8. Sous Termux cela est généralement activé par défaut.
Erreur length must be >= 25 : indiquez une longueur >= 25.
Erreur liée à la somme des EXACTS : vérifiez que la somme de exact_lower + exact_upper + exact_digits + exact_special ≤ longueur.
Problème d'exclusion : pour exclure l'espace, entrez le token <space>.
Fonctionnalités futures proposées
Intégration automatique avec le presse‑papiers Termux (termux-clipboard-set) pour copier la sortie.
Mode non‑interactif / arguments CLI pour automatisation et export CSV/JSON.
Historique local chiffré des sorties (optionnel, avec mot de passe maître).
Préchargement automatique d'une wordlist words.txt dans le répertoire projet si absent.
Licence
Le script est fourni « tel quel » à titre d'exemple. Si vous souhaitez une licence explicite, indiquez laquelle (MIT, Apache‑2.0, GPLv3, ...), et un en‑tête de licence sera ajouté au dépôt.

Contact / améliorations
Si vous souhaitez que j'ajoute l'une des fonctionnalités suivantes, précisez laquelle :

ajout du mode non‑interactif (arguments CLI et export CSV/JSON) ;
intégration termux-clipboard-set pour copier automatiquement le mot/phrase généré dans le presse‑papiers Termux ;
insertion automatique d'une wordlist words.txt dans le répertoire projet si absent ;
ajout d'une option pour mémoriser le dernier séparateur sélectionné (préférence).
Fin du README.md

vbnet


Si vous préférez, je peux aussi :
- vous fournir un ensemble de commandes split (comme je l'ai fait avant) mais avec plus petits morceaux encore — à vous de dire la taille maximale de bloc que votre terminal accepte sans tronquer ;  
- générer un petit script shell (quelques lignes) qui télécharge le README depuis une URL publique (si vous acceptez que je crée un gist/public paste) — sinon je peux vous guider pour créer le gist vous-même.

Quelle option vous convient le mieux ?

Oui. Le contenu fourni est exploitable, mais il est actuellement mélangé avec des indications de copie, des balises de langage isolées (`markdown`, `bash`, `yaml`, `vbnet`) et quelques formulations incohérentes. Voici une version **nettoyée, structurée et directement utilisable comme `README.md`**.

> Les blocs internes sont correctement délimités afin d’éviter les problèmes de copier-coller et de rendu Markdown. Le script peut utiliser `secrets`, le module Python recommandé pour générer des valeurs aléatoires adaptées aux mots de passe et autres secrets [1].

````markdown
# Générateur sécurisé de mots de passe et de phrases de passe

`pwgen_secure` est un générateur interactif en Python permettant de créer des mots de passe et des phrases de passe aléatoires depuis un terminal.

Le programme utilise le module Python `secrets`, conçu pour produire des valeurs aléatoires cryptographiquement sûres. Il utilise également `secrets.SystemRandom().shuffle()` pour mélanger les caractères générés.

## Fonctionnalités

- Génération de mots de passe sécurisés.
- Contraintes exactes sur le nombre de :
  - minuscules ;
  - majuscules ;
  - chiffres ;
  - caractères spéciaux.
- Génération de plusieurs mots de passe en une seule opération.
- Génération de phrases de passe à partir d'une wordlist.
- Wordlist intégrée par défaut.
- Utilisation d'une wordlist externe.
- Choix du séparateur :
  - espace ;
  - tiret ;
  - underscore ;
  - ponctuation ;
  - caractères Unicode ;
  - caractères thaïs ;
  - séparateur personnalisé.
- Longueur minimale configurable.
- Fonctionnement en mode console interactif.
- Compatibilité avec Linux, macOS et Termux.

## Prérequis

- Python 3.6 ou supérieur.
- Un terminal compatible UTF-8.
- Termux, Linux ou macOS.

Pour utiliser la copie automatique vers le presse-papiers sous Termux, installez également le paquet `termux-api`.

## Installation

### Linux, macOS et Termux

Créez le répertoire du projet :

```bash
mkdir -p ~/Projets/pwgen_secure
cd ~/Projets/pwgen_secure
```

Placez ensuite le fichier `password_generator.py` dans ce répertoire.

Rendez le script exécutable :

```bash
chmod +x password_generator.py
```

Lancez le programme avec l'une des commandes suivantes :

```bash
./password_generator.py
```

ou :

```bash
python3 password_generator.py
```

## Utilisation

Au démarrage, le programme affiche le menu principal :

```text
=== Menu principal ===
1) Générer 1 mot de passe
2) Générer un batch de mots de passe
3) Générer une phrase de passe
4) Voir les règles et exemples
5) Quitter
```

### 1. Générer un mot de passe

Le programme demande successivement :

1. la longueur souhaitée ;
2. le nombre exact de minuscules ;
3. le nombre exact de majuscules ;
4. le nombre exact de chiffres ;
5. le nombre exact de caractères spéciaux ;
6. les caractères spéciaux à exclure.

La longueur minimale est de 25 caractères.

La somme des contraintes exactes ne doit pas dépasser la longueur demandée :

```text
exact_lower + exact_upper + exact_digits + exact_special <= longueur
```

Si la somme est inférieure à la longueur totale, les caractères restants sont sélectionnés dans l'alphabet autorisé.

Pour exclure explicitement l'espace, saisissez :

```text
<space>
```

### 2. Générer un batch

Cette option fonctionne comme l'option précédente, mais permet de générer plusieurs mots de passe à la suite.

Chaque mot de passe est affiché sur une ligne distincte.

Cette fonctionnalité est pratique pour créer rapidement plusieurs secrets destinés à des environnements de test ou à des comptes distincts.

### 3. Générer une phrase de passe

Le programme demande :

1. la longueur minimale totale ;
2. le séparateur ;
3. le chemin éventuel vers une wordlist.

La phrase de passe contient au minimum trois mots et est construite jusqu'à atteindre la longueur demandée.

Si aucun chemin de wordlist n'est fourni, le programme utilise la wordlist intégrée.

Exemple conceptuel :

```text
arbre๗lune๗nuage๗montagne
```

## Exemples

### Mot de passe avec contraintes exactes

```text
=== Menu principal ===
1) Générer 1 mot de passe
2) Générer un batch de mots de passe
3) Générer une phrase de passe
4) Voir les règles et exemples
5) Quitter

Choix (1-5): 1
Longueur souhaitée (minimum 25): 32
Nombre exact de minuscules: 10
Nombre exact de majuscules: 8
Nombre exact de chiffres: 8
Nombre exact de caractères spéciaux: 6
Caractères spéciaux à exclure: <space>

Mot de passe généré:
aB3...
```

Dans cet exemple, la somme des contraintes est égale à 32 :

```text
10 + 8 + 8 + 6 = 32
```

### Phrase de passe avec séparateur thaï

```text
Choix (1-5): 3
Longueur minimale totale (minimum 25): 120
Sélectionnez un séparateur: ๗
Chemin vers la wordlist: 

Phrase de passe générée:
arbre๗lune๗nuage๗montagne๗...
```

## Règles importantes

### Longueur minimale

Le programme impose une longueur minimale de 25 caractères pour les mots de passe et les phrases de passe.

Cette valeur peut être modifiée dans le code si votre politique de sécurité impose une autre limite.

### Contraintes exactes

Les contraintes exactes s'appliquent séparément aux catégories suivantes :

- caractères minuscules ;
- caractères majuscules ;
- chiffres ;
- caractères spéciaux.

Par exemple, avec les paramètres suivants :

```text
Minuscules : 10
Majuscules : 8
Chiffres   : 8
Spéciaux   : 6
Longueur   : 40
```

Les 32 premiers caractères répondent exactement aux contraintes. Les 8 caractères restants sont choisis dans l'alphabet autorisé.

### Exclusion de caractères

Vous pouvez indiquer une ou plusieurs exclusions.

Exemples :

```text
"
```

```text
\|
```

Pour exclure l'espace, utilisez le mot-clé spécial :

```text
<space>
```

Cette possibilité est utile lorsque le mot de passe doit être compatible avec un shell, une URL, un fichier de configuration ou un système qui interprète certains caractères.

## Wordlists

Le programme contient une petite wordlist intégrée afin de fonctionner immédiatement.

Pour obtenir une meilleure entropie et des phrases de passe plus variées, utilisez une wordlist plus importante et correctement sélectionnée, par exemple une wordlist compatible avec Diceware ou EFF.

La wordlist externe doit contenir un mot par ligne :

```text
arbre
lumiere
nuage
montagne
riviere
```

Vous pouvez placer un fichier `words.txt` dans le répertoire du projet, puis fournir son chemin lorsque le programme le demande.

## Sécurité

- Utilisez toujours `secrets` plutôt que `random` pour générer des mots de passe ou des jetons.
- Ne publiez jamais de mots de passe en clair dans un dépôt Git public.
- Protégez les fichiers contenant des résultats générés.
- Utilisez des permissions restrictives pour les fichiers sensibles.
- Évitez de conserver inutilement un historique des mots de passe générés.
- Utilisez de préférence un gestionnaire de mots de passe comme Bitwarden, 1Password ou KeePassXC.
- Excluez les caractères problématiques lorsque les mots de passe doivent être utilisés dans des scripts ou des fichiers de configuration.
- Pour les phrases de passe, utilisez une wordlist suffisamment riche et adaptée à l'objectif de sécurité.

## Installation globale

Vous pouvez rendre le programme accessible depuis n'importe quel répertoire :

```bash
mkdir -p ~/bin
cp ~/Projets/pwgen_secure/password_generator.py ~/bin/pwgen_secure
chmod +x ~/bin/pwgen_secure
```

Ajoutez ensuite `~/bin` au `PATH` si nécessaire :

```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.profile
source ~/.profile
```

Vous pourrez alors lancer le programme directement :

```bash
pwgen_secure
```

## Alias facultatif

Pour utiliser la commande `pwgen`, ajoutez un alias :

```bash
echo "alias pwgen='pwgen_secure'" >> ~/.bashrc
source ~/.bashrc
```

Vous pourrez ensuite lancer le programme avec :

```bash
pwgen
```

## Dépannage

### Erreur liée à la longueur

Si le programme affiche une erreur indiquant que la longueur doit être supérieure ou égale à 25, indiquez une valeur d'au moins 25.

### Erreur liée aux contraintes exactes

Vérifiez que la somme des contraintes ne dépasse pas la longueur demandée :

```text
exact_lower + exact_upper + exact_digits + exact_special <= longueur
```

### Problèmes d'encodage

Si les caractères Unicode ou thaïs s'affichent incorrectement :

- vérifiez que le terminal utilise UTF-8 ;
- vérifiez la locale du système ;
- utilisez un terminal compatible Unicode.

Sous Termux, l'UTF-8 est généralement activé par défaut.

### Problème avec l'espace

Pour exclure explicitement l'espace, saisissez :

```text
<space>
```

## Personnalisation

Le programme peut être adapté pour :

- remplacer la wordlist intégrée ;
- ajouter de nouveaux séparateurs ;
- ajouter d'autres caractères thaïs ou Unicode ;
- interdire les répétitions de caractères ;
- imposer une répartition plus stricte ;
- modifier la longueur minimale ;
- ajouter des politiques de validation spécifiques ;
- intégrer un mode non interactif.

La fonction `choose_separator()` peut notamment être modifiée pour ajouter vos propres séparateurs.

## Fonctionnalités futures

Les évolutions suivantes peuvent être ajoutées :

- mode non interactif avec arguments en ligne de commande ;
- génération avec `--count` et `--length` ;
- contraintes telles que `--exact-upper` ;
- export CSV ;
- export JSON ;
- copie automatique vers le presse-papiers Termux ;
- historique local chiffré ;
- chargement automatique d'une wordlist `words.txt` ;
- mémorisation du dernier séparateur utilisé ;
- tests automatisés ;
- intégration dans une pipeline CI/CD.

Un exemple d'interface future pourrait être :

```bash
pwgen_secure \
  --count 10 \
  --length 32 \
  --exact-lower 10 \
  --exact-upper 8 \
  --exact-digits 8 \
  --exact-special 6 \
  --csv passwords.csv
```

## Licence

Le script est fourni « tel quel », à titre d'exemple.

Une licence explicite peut être ajoutée selon le besoin du projet :

- MIT ;
- Apache-2.0 ;
- GPLv3.

## Contributions

Les contributions, corrections et suggestions sont les bienvenues.

Les améliorations possibles concernent notamment :

- la sécurité ;
- la validation des paramètres ;
- la qualité des wordlists ;
- l'interface utilisateur ;
- les tests automatisés ;
- l'intégration Termux ;
- l'automatisation via GitHub Actions.

