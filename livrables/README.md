# Livrables de l'équipe

Placez ici **vos** artefacts, copiés depuis [`../modeles/`](../modeles/) et complétés.

## Nommage

| Artefact | Nom du fichier |
|---|---|
| Un seul exemplaire | le nom du modèle : `C1-parties-prenantes.md`, `C4-fiche-besoins.md`, `S2-fiche-rgpd.md`… |
| Un exemplaire par entretien (C2, C3) | `C2-guide-entretien-<interlocuteur>.md`, `C3-compte-rendu-<interlocuteur>.md` — ex. `C3-compte-rendu-soigneuse.md` |
| Une fiche RGPD par traitement (S2) | `S2-fiche-rgpd-<traitement>.md` — ex. `S2-fiche-rgpd-adoptions.md` |
| Fichiers joints (maquettes, calculs, photos) | dans `livrables/annexes/`, référencés depuis l'artefact |

## Première ligne de chaque artefact

Remplacez les champs d'en-tête (cas, équipe, date) et **remplacez chaque marqueur `⟪ … ⟫`** (y compris les exemples `⟪ex. …⟫`) par votre contenu : un marqueur restant signifie une rubrique non traitée, c'est ce que compte `outils/verifier.py`. Cochez les critères de qualité `[x]` quand ils sont vraiment remplis.

## Calculs

Les chiffres de M1 et M3 qui proviennent des fichiers CSV du cas doivent être **reproductibles** : joignez le script (Python, tableur, requête SQL) dans `livrables/annexes/` et indiquez dans M1 comment le relancer.

Exemple pour démarrer (Python + pandas) :

```python
import pandas as pd
df = pd.read_csv("cas/03-cabinet-kine-tilleuls/documents/journal-appels.csv", sep=";")
print(df["pris_par"].value_counts(normalize=True))
```
