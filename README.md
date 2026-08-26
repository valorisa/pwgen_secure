# Générateur sécurisé de mots de passe et de phrases de passe

`pwgen_secure` est un générateur interactif en Python permettant de créer des
mots de passe et des phrases de passe aléatoires depuis un terminal.

Le programme utilise le module Python `secrets` pour la génération aléatoire
et `secrets.SystemRandom().shuffle()` pour mélanger les caractères.

## Fonctionnalités

- Génération de mots de passe sécurisés.
- Contraintes exactes sur le nombre de minuscules, majuscules, chiffres et
  caractères spéciaux.
- Génération de plusieurs mots de passe en une seule opération.
- Génération de phrases de passe à partir d'une wordlist.
- Utilisation d'une wordlist intégrée.
- Utilisation d'une wordlist externe.
- Choix du séparateur :
  - espace ;
  - tiret ;
  - underscore ;
  - point ;
  - barre verticale ;
  - virgule ;
  - point-virgule ;
  - caractère Unicode ;
  - caractère thaï ;
  - séparateur personnalisé.
- Longueur minimale configurable dans le code.
- Fonctionnement en mode console interactif.
- Compatibilité avec Linux, macOS et Termux.

## Prérequis

- Python 3.6 ou supérieur.
- Un terminal compatible UTF-8.
- Termux, Linux ou macOS.

Pour utiliser une éventuelle copie automatique vers le presse-papiers sous
Termux, installez également le paquet `termux-api`.

## Installation

### Linux, macOS et Termux

Créez le répertoire du projet :

```bash
mkdir -p ~/Projets/pwgen_secure
cd ~/Projets/pwgen_secure
```

Placez le fichier `password_generator.py` dans ce répertoire.

Rendez le script exécutable :

```bash
chmod +x password_generator.py
```

Lancez le programme avec l'une des commandes suivantes :

```bash
./password_generator.py
```

Ou :

```bash
python3 password_generator.py
```

## Utilisation

Au démarrage, le programme affiche le menu principal :

```text
=== Menu principal ===
1) Générer 1 mot de passe (contraintes EXACTES possibles)
2) Générer un batch de mots de passe
3) Générer une phrase de passe
4) Voir règles / exemples
5) Quitter
```

### Générer un mot de passe

Le programme demande successivement :

1. la longueur souhaitée ;
2. le nombre exact de minuscules ;
3. le nombre exact de majuscules ;
4. le nombre exact de chiffres ;
5. le nombre exact de caractères spéciaux ;
6. les caractères spéciaux à exclure.

La longueur minimale est de 25 caractères.

Pour exclure explicitement l'espace, saisissez :

```text
<space>
```

### Générer un batch

Cette option utilise les mêmes paramètres que la génération d'un mot de passe
unique, mais permet de produire plusieurs mots de passe à la suite.

Chaque mot de passe est affiché sur une ligne distincte.

### Générer une phrase de passe

Le programme demande :

1. la longueur minimale totale ;
2. le séparateur ;
3. le chemin éventuel vers une wordlist.

La phrase de passe contient au minimum trois mots et est construite jusqu'à
atteindre la longueur demandée.

Si aucun chemin de wordlist n'est fourni, le programme utilise la wordlist
intégrée.

Exemple :

```text
arbre๗lune๗nuage๗montagne
```

### Afficher les règles et exemples

Cette option affiche des informations concernant :

- la longueur minimale ;
- les contraintes exactes ;
- l'exclusion de caractères ;
- le token `<space>` ;
- les erreurs liées aux paramètres ;
- des exemples d'utilisation.

### Quitter

L'option `5` quitte proprement le programme.

## Contraintes exactes

Les contraintes exactes s'appliquent aux catégories suivantes :

- caractères minuscules ;
- caractères majuscules ;
- chiffres ;
- caractères spéciaux.

La somme des contraintes ne doit pas dépasser la longueur demandée :

```text
exact_lower + exact_upper + exact_digits + exact_special <= longueur
```

Par exemple :

```text
Minuscules : 10
Majuscules : 8
Chiffres   : 8
Spéciaux   : 6
Longueur   : 32
```

Dans cet exemple :

```text
10 + 8 + 8 + 6 = 32
```

Si la somme des contraintes est inférieure à la longueur totale, les caractères
restants sont sélectionnés dans l'alphabet autorisé.

## Exemples

### Mot de passe avec contraintes exactes

```text
=== Menu principal ===
1) Générer 1 mot de passe (contraintes EXACTES possibles)
2) Générer un batch de mots de passe
3) Générer une phrase de passe
4) Voir règles / exemples
5) Quitter

Choix (1-5): 1
Longueur souhaitée (défaut 25): 32
Nombre EXACT de minuscules (défaut 1): 10
Nombre EXACT de MAJUSCULES (défaut 1): 8
Nombre EXACT de CHIFFRES (défaut 1): 8
Nombre EXACT de SPECIAUX (défaut 1): 6
Caractères spéciaux à EXCLURE: <space>

Mot de passe généré:
aB3...
```

### Phrase de passe avec séparateur personnalisé

```text
Choix (1-5): 3
Longueur minimale totale en caractères: 120
Choix du séparateur: 10
Séparateur personnalisé: ณ
Chemin vers la wordlist:

Phrase de passe générée:
bleuณflammeณnuageณiglooณdauphinณhorizonณ...
```

## Règles de sécurité

- Utilisez `secrets` plutôt que `random` pour générer des secrets.
- Ne publiez jamais de mots de passe en clair dans un dépôt public.
- Évitez de conserver inutilement les résultats générés.
- Protégez les fichiers contenant des secrets avec des permissions restrictives.
- Utilisez un gestionnaire de mots de passe pour conserver les résultats utiles.
- Excluez les caractères problématiques lorsque le mot de passe doit être
  utilisé dans un shell ou un fichier de configuration.
- Utilisez une wordlist suffisamment riche pour les phrases de passe.
- Vérifiez la politique de sécurité du service avant d'utiliser des caractères
  Unicode ou des caractères spéciaux.

## Wordlists

Le programme contient une petite wordlist intégrée afin de fonctionner
immédiatement.

Pour obtenir des phrases de passe plus variées, vous pouvez fournir une
wordlist externe contenant un mot par ligne :

```text
arbre
lumiere
nuage
montagne
riviere
```

Vous pouvez placer cette wordlist dans le répertoire du projet, par exemple :

```text
~/Projets/pwgen_secure/words.txt
```

Indiquez ensuite son chemin lorsque le programme le demande.

## Dépannage

### Erreur de longueur

Si le programme indique que la longueur doit être supérieure ou égale à 25,
saisissez une valeur d'au moins 25.

### Erreur liée aux contraintes exactes

Vérifiez que la somme des contraintes ne dépasse pas la longueur demandée :

```text
exact_lower + exact_upper + exact_digits + exact_special <= longueur
```

### Erreur d'exclusion

Pour exclure l'espace, utilisez exactement le token suivant :

```text
<space>
```

Pour exclure plusieurs caractères, saisissez-les conformément aux indications
affichées par le programme.

### Problèmes d'encodage

Si les caractères Unicode ou thaïs s'affichent incorrectement :

- vérifiez que le terminal utilise UTF-8 ;
- vérifiez la locale du système ;
- utilisez un terminal compatible Unicode.

Sous Termux, l'UTF-8 est généralement activé par défaut.

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

Vous pourrez alors lancer le programme avec :

```bash
pwgen_secure
```

## Alias facultatif

Pour utiliser la commande `pwgen`, ajoutez un alias :

```bash
echo "alias pwgen='pwgen_secure'" >> ~/.bashrc
source ~/.bashrc
```

Rechargez la configuration du shell :

```bash
source ~/.bashrc
```

Vous pourrez ensuite lancer le programme avec :

```bash
pwgen
```

## Vérification du programme

Vérifiez d'abord la syntaxe Python :

```bash
python3 -m py_compile password_generator.py
```

Une absence de sortie indique que la compilation s'est déroulée correctement.

Lancez ensuite le programme :

```bash
./password_generator.py
```

Vérifiez l'état du dépôt Git :

```bash
git status
```

## Personnalisation

Le programme peut être adapté pour :

- remplacer la wordlist intégrée ;
- ajouter de nouveaux séparateurs ;
- ajouter d'autres caractères Unicode ;
- ajouter d'autres caractères thaïs ;
- modifier la longueur minimale ;
- interdire les répétitions de caractères ;
- imposer une répartition plus stricte ;
- ajouter des règles de validation ;
- ajouter un mode non interactif ;
- ajouter des tests automatisés.

La fonction `choose_separator()` peut notamment être modifiée pour ajouter
d'autres séparateurs.

## Fonctionnalités futures

Les évolutions suivantes peuvent être ajoutées :

- mode non interactif avec arguments en ligne de commande ;
- génération avec `--count` et `--length` ;
- contraintes comme `--exact-upper` ;
- export CSV ;
- export JSON ;
- copie automatique vers le presse-papiers Termux ;
- historique local chiffré ;
- chargement automatique d'une wordlist `words.txt` ;
- mémorisation du dernier séparateur utilisé ;
- tests automatisés ;
- intégration dans une pipeline CI/CD.

Exemple d'interface future :

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

Une licence explicite peut être ajoutée selon les besoins du projet, par
exemple :

- MIT ;
- Apache-2.0 ;
- GPL-3.0.

## Contributions

Les contributions, corrections et suggestions sont les bienvenues.

Les améliorations peuvent concerner :

- la sécurité ;
- la validation des paramètres ;
- la qualité des wordlists ;
- l'interface utilisateur ;
- les tests automatisés ;
- l'intégration Termux ;
- l'automatisation via GitHub Actions.
