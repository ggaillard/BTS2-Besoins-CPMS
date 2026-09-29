#!/usr/bin/env python3
"""Vérifie l'état des livrables de l'équipe (méthode CPMS).

Usage :
    python3 outils/verifier.py              # tous les jalons
    python3 outils/verifier.py --jalon J2   # ce qui est attendu jusqu'au jalon J2 inclus

Le script ne juge pas la qualité ; il repère ce qui manque :
  - artefact absent ;
  - champs ⟪…⟫ restants (chaque marqueur doit être remplacé par votre contenu) ;
  - mention « Usage de l'IA » non remplie ;
  - cases « Critères de qualité » non cochées.
Code de sortie : 0 si tout est complet pour le jalon demandé, 1 sinon.
"""
import argparse
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
LIVRABLES = RACINE / "livrables"

# (préfixe de fichier, libellé, jalon, nombre minimal d'exemplaires)
ATTENDUS = [
    ("C1-", "Carte des parties prenantes", "J1", 1),
    ("C2-", "Guide d'entretien", "J1", 3),
    ("C3-", "Compte rendu d'entretien", "J1", 3),
    ("M1-", "Situation de départ et indicateurs", "J1", 1),
    ("S1-", "Données et besoins DICP", "J1", 1),
    ("P3-", "Journal de bord", "J1", 1),
    ("C4-", "Fiche besoins", "J2", 1),
    ("C5-", "Étude de faisabilité", "J2", 1),
    ("S2-", "Fiche RGPD", "J2", 1),
    ("P2-", "Registre des risques", "J2", 1),
    ("C6-", "Dossier de solution", "J3", 1),
    ("P1-", "Plan de projet", "J3", 1),
    ("P4-", "Plan de déploiement", "J3", 1),
    ("M2-", "Cahier de recette", "J3", 1),
    ("S3-", "Plan de sécurisation", "J3", 1),
    ("M3-", "Bilan", "J4", 1),
]
ORDRE = ["J1", "J2", "J3", "J4"]
VERBE = {"C": "Concevoir", "P": "Piloter", "M": "Mesurer", "S": "Sécuriser"}

A_COMPLETER = re.compile(r"⟪")
IA_VIDE = re.compile(r"\*\*Usage de l'IA\*\*\s*:\s*(⟪.*?⟫)?\s*$", re.MULTILINE)
CASE_VIDE = re.compile(r"\[ \]")


def analyser(fichier: Path) -> list[str]:
    texte = fichier.read_text(encoding="utf-8")
    problemes = []
    n = len(A_COMPLETER.findall(texte))
    if n:
        problemes.append(f"{n} champ(s) ⟪…⟫ non remplacé(s)")
    if "**Usage de l'IA**" in texte and IA_VIDE.search(texte):
        problemes.append("« Usage de l'IA » non renseigné")
    crit = texte.split("**Critères de qualité**", 1)
    if len(crit) == 2:
        vides = len(CASE_VIDE.findall(crit[1].split("\n", 1)[0]))
        if vides:
            problemes.append(f"{vides} critère(s) de qualité non coché(s)")
    return problemes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--jalon", choices=ORDRE, help="ne vérifier que ce qui est attendu jusqu'à ce jalon")
    args = parser.parse_args()
    limite = ORDRE.index(args.jalon) if args.jalon else len(ORDRE) - 1

    fichiers = sorted(p for p in LIVRABLES.glob("*.md") if p.name != "README.md")
    complet = True
    print(f"Livrables dans {LIVRABLES.relative_to(RACINE)}/ — jusqu'au jalon {ORDRE[limite]}\n")
    for jalon in ORDRE[: limite + 1]:
        print(f"── {jalon} " + "─" * 60)
        for prefixe, libelle, j, minimum in ATTENDUS:
            if j != jalon:
                continue
            trouves = [f for f in fichiers if f.name.startswith(prefixe)]
            code = prefixe.rstrip("-")
            entete = f"  {code:<3} {VERBE[code[0]]:<10} {libelle:<36}"
            if len(trouves) < minimum:
                complet = False
                print(f"{entete} ✗ {len(trouves)}/{minimum} fichier(s)")
                continue
            soucis = {f.name: analyser(f) for f in trouves}
            if any(soucis.values()):
                complet = False
                print(f"{entete} ◐")
                for nom, liste in soucis.items():
                    if liste:
                        print(f"        {nom} : " + " ; ".join(liste))
            else:
                print(f"{entete} ✓")
        print()
    print("Complet pour ce jalon." if complet else "Incomplet : voir les lignes ✗ et ◐ ci-dessus.")
    return 0 if complet else 1


if __name__ == "__main__":
    sys.exit(main())
