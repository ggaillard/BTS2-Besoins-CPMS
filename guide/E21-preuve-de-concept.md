# Étape 21 — Réaliser une preuve de concept (optionnelle)

> Phase 5 Piloter et mesurer · **Concevoir** + **Mesurer** · Pas d'artefact dédié : résultats dans [M2](../modeles/M2-cahier-recette.md) et [M3](../modeles/M3-bilan.md) · ⏱ 1 séance

## Pourquoi cette étape ?

Une preuve de concept (*PoC*) sert à lever **le doute le plus important** avant d'engager le client : « les bénévoles sauront-ils réserver sur téléphone en moins de 2 minutes ? », « l'assistant répond-il juste à 80 % des questions ? », « l'import des 200 réservations passe-t-il sans erreur ? ». Ce n'est pas une version réduite de toute la solution.

## Comment faire, pas à pas

1. **Choisissez UNE question** : l'hypothèse la plus risquée de votre C5 (conditions de la recommandation) ou de P2 (risque le plus critique).
2. **Écrivez le critère de succès avant** : « PoC réussie si 4 utilisateurs sur 5 réservent en moins de 2 minutes sans aide ».
3. **Construisez le minimum** : un compte de test configuré, un formulaire, un script, un petit jeu d'évaluation de questions… avec des **données fictives**.
4. **Faites tester** par quelqu'un qui n'a pas construit (camarade d'une autre équipe dans le rôle, enseignant).
5. **Mesurez** et reportez dans M2 (tests exécutés) et M3 (« obtenu ou projeté »).
6. **Concluez** : l'hypothèse est-elle confirmée ? Faut-il modifier la recommandation ? Notez la décision dans P3.

## Exemples de questions de PoC

| Doute | PoC possible |
|---|---|
| Les utilisateurs vont-ils y arriver ? | test chronométré sur téléphone avec 5 personnes |
| Les données existantes sont-elles reprenables ? | import du CSV du cas dans l'outil, comptage des erreurs |
| Une IA répond-elle juste ? | 30 questions réelles, réponses de référence, taux de réponses exactes et sourcées |
| Le coût réel est-il celui annoncé ? | configuration complète sur l'offre gratuite, relevé des limites atteintes |

## J'ai fini quand…

- [ ] une seule question, un critère de succès écrit avant ;
- [ ] le résultat est mesuré et reporté dans M2 / M3 ;
- [ ] la conclusion est notée dans le journal.

---
[← Étape 20](E20-securisation.md) · [Parcours](../METHODE.md) · [Étape 22 — Bilan →](E22-bilan.md)
