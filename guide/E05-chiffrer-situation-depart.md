# Étape 5 — Chiffrer la situation de départ

> Phase 1 Recueillir · **Mesurer** · Artefact : [M1 Situation de départ et indicateurs](../modeles/M1-indicateurs.md), §1 · Jalon **J1** · ⏱ 1 h 30

## Pourquoi cette étape ?

« Ça prend beaucoup de temps », « on perd des clients » : tant que ce n'est pas chiffré, c'est une impression. En chiffrant **l'avant**, vous gagnez deux choses : un **argument** pour convaincre le client à J2 (« vos devis envoyés en 3 jours sont signés deux fois plus souvent ») et un **point de comparaison** pour prouver au bilan que la solution a amélioré quelque chose.

## Ce dont vous avez besoin

- Les chiffres notés dans vos [C3](../modeles/C3-compte-rendu-entretien.md) (§3).
- Les fichiers de données de votre cas :

| Cas | Fichiers | Questions pour démarrer (à vous de trouver les réponses) |
|---|---|---|
| 1 — SPA | [`animaux.csv`](../cas/01-spa-forez-pilat/documents/animaux.csv), [`planning-promenades.csv`](../cas/01-spa-forez-pilat/documents/planning-promenades.csv) | Combien de sorties par chien sur deux semaines ? Quels chiens n'apparaissent jamais ? Qui promène les chiens « orange » et « rouge » ? Combien de sorties dont on ne sait pas si elles ont eu lieu ? Les données sont-elles propres (formats de date, statuts) ? |
| 2 — Mairie | [`reservations-2025.csv`](../cas/02-mairie-saint-roch/documents/reservations-2025.csv) | Combien de réservations par an, par salle, par type de demandeur ? Y a-t-il des conflits (même salle, même jour) ? Des réservations passées jamais payées ? Des cautions litigieuses ? |
| 3 — Kiné | [`journal-appels.csv`](../cas/03-cabinet-kine-tilleuls/documents/journal-appels.csv), [`rendez-vous-non-honores.csv`](../cas/03-cabinet-kine-tilleuls/documents/rendez-vous-non-honores.csv) | Combien d'appels par jour ? Qui décroche le matin, l'après-midi ? Pour quels motifs ? Combien de minutes de séance interrompues ? Quel taux d'absence, et qui sont les patients récidivistes ? |
| 4 — Traiteur | [`demandes-devis-2025.csv`](../cas/04-traiteur-maison-berard/documents/demandes-devis-2025.csv) | Combien de demandes restent sans devis ? Quel délai d'envoi ? Le taux de signature dépend-il du délai ? Quelle part de mariages, de repas d'entreprise ? Combien de devis relancés ? |
| 5 — Office de tourisme | [`journal-demandes.csv`](../cas/05-office-tourisme-hautes-chaumes/documents/journal-demandes.csv), [`faq-interne.md`](../cas/05-office-tourisme-hautes-chaumes/documents/faq-interne.md) | Quelle part des demandes arrive hors horaires ? Quel délai de réponse à l'écrit ? Quelle part trouve sa réponse dans la FAQ ? Dans quelles langues ? Quelles catégories dominent ? |

## Comment faire, pas à pas

1. **Copiez le modèle** : `cp modeles/M1-indicateurs.md livrables/`. Vous ne remplissez que le **§1** pour J1.
2. **Listez 4 à 6 grandeurs** qui décrivent le problème (fréquence, durée, volume, taux d'erreur, coût). Chaque grandeur doit être reliée à un constat de vos C3.
3. **Calculez** à partir des fichiers, **au tableur ou en Python** :

   *Au tableur* : ouvrir le CSV (séparateur **point-virgule**, encodage UTF-8), *Insertion → Tableau croisé dynamique*, glisser une colonne en lignes et la même en valeurs (nombre).

   *En Python (pandas)* — dans un Codespace ou sur votre poste :

   ```python
   import pandas as pd
   df = pd.read_csv("cas/<votre-cas>/documents/<fichier>.csv", sep=";")

   df.head()                                   # voir les premières lignes
   df["colonne"].value_counts()                # combien de lignes par valeur
   df["colonne"].value_counts(normalize=True)  # la même chose en proportions
   df.groupby("colonne_a")["colonne_b"].mean() # une moyenne par groupe
   pd.crosstab(df["colonne_a"], df["colonne_b"], normalize="index")  # tableau croisé en %
   df[df["colonne"] == "valeur"]               # filtrer les lignes
   df.duplicated(["col1", "col2"]).sum()       # compter les doublons sur deux colonnes
   ```

4. **Enregistrez votre calcul** dans `livrables/annexes/` (le script `.py` ou le tableur), pour qu'on puisse le **refaire**.
5. **Remplissez le tableau** : valeur, période, **méthode**, source, et dites si c'est **mesuré** (fichier) ou **estimé** (entretien).
6. **Confrontez** fichier et entretiens : si quelqu'un dit « deux doubles réservations » et que le fichier en montre trois, c'est une découverte à noter (C3 §5, question à poser).

## Exemple

[M1 du club de handball](../exemples/hbc-val-de-furan/M1-indicateurs.md) et son [annexe de calcul](../exemples/hbc-val-de-furan/annexes/calcul-taux-reponse.md).

## Pièges à éviter

- Donner un chiffre sans dire d'où il vient ni comment le recalculer.
- Moyenner des choses qui ne se comparent pas (le matin et l'après-midi, février et juillet) : **découpez**.
- Oublier que les fichiers sont des **extraits** (deux semaines, un mois) : précisez la période.

## J'ai fini quand…

- [ ] au moins 4 grandeurs chiffrées, chacune avec méthode et source ;
- [ ] mesuré et estimé sont distingués ;
- [ ] le calcul est dans `livrables/annexes/` et peut être relancé.

---
[← Étape 4](E04-mener-entretien-compte-rendu.md) · [Parcours](../METHODE.md) · [Étape 6 — Inventorier les données →](E06-donnees-et-dicp.md)
