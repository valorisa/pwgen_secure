#!/usr/bin/env python3
"""
Générateur interactif de mots de passe et phrases de passe (CSPRNG).
- Longueur minimale 25
- Exclusion personnalisée de caractères spéciaux (utiliser "<space>" pour l'espace)
- Contraintes EXACTES pour lower/upper/digits/specials
- Génération de phrases de passe à partir d'une wordlist (fichier ou embarquée)
- Choix de séparateur via menu (inclut quelques séparateurs Unicode/Thaï)
"""

import secrets
import string
import sys
from pathlib import Path

MIN_LENGTH = 25
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
ALL_PUNCT = string.punctuation

# Petite wordlist embarquée en fallback
DEFAULT_WORDS = [
    "arbre", "bleu", "ciel", "dauphin", "embrun", "flamme", "galet", "horizon",
    "igloo", "jardin", "kilo", "lune", "mont", "nuage", "océan", "pierre",
    "quartz", "rêve", "savon", "trèfle", "unique", "verger", "wagon", "zéphyr"
]

def build_filtered_punct(exclude: str) -> str:
    """Retourne la ponctuation sans les caractères exclus."""
    return ''.join(ch for ch in ALL_PUNCT if ch not in exclude)

def gen_password_exact_counts(length: int,
                              exact_lower: int,
                              exact_upper: int,
                              exact_digits: int,
                              exact_special: int,
                              exclude_special_chars: str = "") -> str:
    """
    Génère un mot de passe de `length` en respectant les nombres EXACTS fournis.
    Le reste (si length > somme exacts) est rempli par l'alphabet complet filtré.
    """
    if length < MIN_LENGTH:
        raise ValueError(f"length must be >= {MIN_LENGTH}")
    if any(x < 0 for x in (exact_lower, exact_upper, exact_digits, exact_special)):
        raise ValueError("Exact counts must be >= 0")

    punct = build_filtered_punct(exclude_special_chars)
    total_exact = exact_lower + exact_upper + exact_digits + exact_special
    if total_exact > length:
        raise ValueError("La somme des comptes EXACTS dépasse la longueur demandée")
    if exact_special > 0 and not punct:
        raise ValueError("Aucun caractère spécial disponible après exclusion")

    parts = []
    parts += [secrets.choice(LOWER) for _ in range(exact_lower)]
    parts += [secrets.choice(UPPER) for _ in range(exact_upper)]
    parts += [secrets.choice(DIGITS) for _ in range(exact_digits)]
    parts += [secrets.choice(punct) for _ in range(exact_special)]

    alphabet = LOWER + UPPER + DIGITS + punct
    remaining = length - len(parts)
    if remaining > 0:
        parts += [secrets.choice(alphabet) for _ in range(remaining)]

    secrets.SystemRandom().shuffle(parts)
    return ''.join(parts)

def load_wordlist(path: str):
    """Charge une wordlist depuis un fichier; si fichier manquant, retourne DEFAULT_WORDS."""
    if not path:
        return DEFAULT_WORDS.copy()
    p = Path(path).expanduser()
    if not p.exists():
        print(f"Warning: wordlist '{path}' non trouvée — utilisation de la wordlist embarquée.")
        return DEFAULT_WORDS.copy()
    words = []
    with p.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            w = line.strip()
            if w:
                words.append(w)
    return words if words else DEFAULT_WORDS.copy()

def gen_passphrase(min_chars: int, words: list, separator: str = " ") -> str:
    """Génère une phrase de passe composée de mots choisis aléatoirement jusqu'à atteindre min_chars."""
    if min_chars < MIN_LENGTH:
        min_chars = MIN_LENGTH
    chosen = []
    while True:
        chosen.append(secrets.choice(words))
        candidate = separator.join(chosen)
        if len(candidate) >= min_chars and len(chosen) >= 3:
            return candidate

def prompt_int(prompt: str, default: int) -> int:
    s = input(f"{prompt} (défaut {default}): ").strip()
    if not s:
        return default
    return int(s)

def choose_separator():
    """
    Propose un menu de séparateurs prédéfinis (incluant Unicode/Thaï).
    Retourne le séparateur choisi (chaîne) ou None si annulé.
    """
    # Vous pouvez remplacer/étendre la liste ci-dessous par vos 10 caractères Thaï fournis par Gemini.
    defaults = [
        ("Espace (représenté par '<space>')", "<space>"),
        ("Tiret simple", "-"),
        ("Underscore", "_"),
        ("Point", "."),
        ("Barre verticale", "|"),
        ("Virgule", ","),
        ("Point-virgule", ";"),
        ("Thaï 1 (๗)", "๗"),
        ("Thaï 2 (๐)", "๐"),
        ("Caractère personnalisé", None),
    ]

    print("\nSélectionnez un séparateur :")
    for i, (label, val) in enumerate(defaults, start=1):
        disp = val if val is not None else "<personnalisé>"
        print(f"{i}) {label} -> {disp}")
    print("0) Annuler (retour au menu)")

    while True:
        choice = input("Choix (numéro) : ").strip()
        if not choice:
            # défaut -> espace
            return " "
        if choice == "0":
            return None
        try:
            idx = int(choice)
        except ValueError:
            print("Entrée invalide, tapez un numéro.")
            continue
        if 1 <= idx <= len(defaults):
            label, val = defaults[idx - 1]
            if val is None:
                custom = input("Saisir le séparateur souhaité (ou '<space>' pour espace) : ")
                if "<space>" in custom:
                    custom = custom.replace("<space>", " ")
                return custom
            if val == "<space>":
                return " "
            return val
        else:
            print("Numéro hors plage, réessayez.")

def interactive_menu():
    print("Générateur sécurisé — mode interactif")
    print("Ctrl-C pour quitter à tout moment.\n")
    while True:
        try:
            print("=== Menu principal ===")
            print("1) Générer 1 mot de passe (contraintes EXACTES possibles)")
            print("2) Générer un batch de mots de passe")
            print("3) Générer une phrase de passe")
            print("4) Voir règles / exemples")
            print("5) Quitter")
            choice = input("Choix (1-5): ").strip()

            if choice == "1":
                handle_generate(single=True)
            elif choice == "2":
                handle_generate(single=False)
            elif choice == "3":
                handle_passphrase()
            elif choice == "4":
                show_rules()
            elif choice == "5":
                print("Au revoir.")
                return
            else:
                print("Choix invalide, réessayez.\n")

        except KeyboardInterrupt:
            print("\nInterrompu. Au revoir.")
            return

def handle_generate(single: bool):
    try:
        length = prompt_int("Longueur souhaitée", MIN_LENGTH)
        length = max(length, MIN_LENGTH)

        print("\n--- Contraintes EXACTES (entrez 0 pour aucune) ---")
        exact_lower = prompt_int("Nombre EXACT de minuscules", 1)
        exact_upper = prompt_int("Nombre EXACT de MAJUSCULES", 1)
        exact_digits = prompt_int("Nombre EXACT de CHIFFRES", 1)
        exact_special = prompt_int("Nombre EXACT de SPECIAUX", 1)

        exclude = input('Caractères spéciaux à EXCLURE (tapez tels quels; utilisez "<space>" pour espace; laisser vide = aucun): ').strip()
        if "<space>" in exclude:
            exclude = exclude.replace("<space>", " ")

        if single:
            try:
                pwd = gen_password_exact_counts(length, exact_lower, exact_upper, exact_digits, exact_special, exclude)
            except ValueError as e:
                print("Erreur:", e, "\n")
                return
            print("\nMot de passe généré:\n" + pwd)
            print("Longueur:", len(pwd))
            print("Ponctuation exclue:", repr(exclude))
            print()
        else:
            count = prompt_int("Combien d'items générer", 10)
            print("\nBatch — output:")
            for _ in range(max(1, count)):
                try:
                    print(gen_password_exact_counts(length, exact_lower, exact_upper, exact_digits, exact_special, exclude))
                except ValueError as e:
                    print("Erreur lors de la génération:", e)
                    break
            print()
    except ValueError:
        print("Entrée invalide (attendu entier). Recommencez.\n")

def handle_passphrase():
    try:
        print("\n--- Génération de phrase de passe ---")
        min_chars = prompt_int("Longueur minimale totale en caractères (min 25)", MIN_LENGTH)
        sep = choose_separator()
        if sep is None:
            print("Opération annulée, retour au menu.\n")
            return
        wordlist_path = input("Chemin vers wordlist (une ligne = un mot) ou laisser vide pour default: ").strip()
        if "<space>" in wordlist_path:
            wordlist_path = wordlist_path.replace("<space>", " ")
        words = load_wordlist(wordlist_path) if wordlist_path else DEFAULT_WORDS.copy()
        passphrase = gen_passphrase(min_chars, words, separator=sep)
        print("\nPhrase de passe générée:\n" + passphrase)
        print("Longueur:", len(passphrase), "| Nombre de mots:", len(passphrase.split(sep)))
        print()
    except ValueError:
        print("Entrée invalide. Recommencez.\n")

def show_rules():
    print("\nRègles / exemples :")
    print(f"- Longueur minimale enforceée : {MIN_LENGTH}")
    print("- Pour exclure l'espace, tapez '<space>' dans le champ d'exclusion.")
    print("- Si la somme des EXACTS dépasse la longueur, une erreur sera affichée.")
    print("- Si vous excluez tous les caractères spéciaux mais demandez des spéciaux > 0, cela provoquera une erreur.")
    print("- Pour la phrase de passe, fournissez une wordlist (fichier texte) si vous voulez de meilleurs mots; sinon la wordlist embarquée sera utilisée.")
    print("- Le menu de séparateurs propose quelques caractères Thaï par défaut; vous pouvez remplacer/étendre cette liste dans la fonction choose_separator().")
    print()
    input("Appuyez sur Entrée pour revenir au menu...\n")

if __name__ == "__main__":
    interactive_menu()
