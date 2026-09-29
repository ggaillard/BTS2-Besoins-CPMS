# Étape 12 — Comparer trois scénarios (TELOS, coûts) et recommander

> Phase 3 Faisabilité · **Concevoir** · Artefact : [C5 Étude de faisabilité et scénarios](../modeles/C5-etude-faisabilite.md) · Jalon **J2** · ⏱ 2 h

## Pourquoi cette étape ?

C'est le cœur du jalon J2 : vous devez dire au client **ce qu'il faut faire, et pourquoi**. Une recommandation est convaincante quand on voit qu'elle résulte d'une comparaison honnête, pas d'une préférence. La grille TELOS garantit que vous n'oubliez aucun angle : technique, argent, droit, humain, délai.

## Ce dont vous avez besoin

- [C4](../modeles/C4-fiche-besoins.md) (récits Must, ENF), [M1](../modeles/M1-indicateurs.md) (chiffres), [S1](../modeles/S1-donnees-dicp.md) (données sensibles).
- Votre comparatif de l'[étape 11](E11-rechercher-solutions.md).
- Les contraintes de budget et de délai recueillies en entretien.

## Comment faire, pas à pas

1. **Copiez le modèle** : `cp modeles/C5-etude-faisabilite.md livrables/`.
2. **Définissez trois scénarios** (au moins) :
   - **S0 — Sans développement** : réorganiser, fixer une règle, mieux utiliser ce qui existe. Il n'est jamais « pour la forme » : écrivez-le comme si c'était la bonne réponse.
   - **S1 — Solution du marché** : la mieux placée de votre comparatif.
   - **S2 — Sur mesure** : ce qu'il faudrait développer, héberger, maintenir.
   Des scénarios **hybrides** sont possibles (S1 + S0 pour une partie des utilisateurs).
3. **Comptez les Must couverts** par chaque scénario.
4. **Notez chaque critère TELOS de 0 à 3**, avec **une phrase de justification et une source** :

   | Critère | Questions à se poser | Un 0 (éliminatoire), c'est par exemple… |
   |---|---|---|
   | **T**echnique | Matériel, réseau, compétences disponibles ? **Qui maintiendra dans 2 ans ?** | personne pour corriger un bug après votre départ |
   | **É**conomique | Coût total sur 3 ans (y compris temps humain) vs gain chiffré (M1) ? | abonnement supérieur au budget annuel |
   | **L**égal | Données sensibles, hébergement, règles du secteur, argent public, accessibilité, IA ? | données de santé chez un hébergeur non certifié |
   | **O**pérationnel | Les vrais utilisateurs vont-ils l'adopter ? Que change-t-on dans leurs habitudes ? | exclut les utilisateurs sans smartphone alors qu'ils font le travail |
   | Calendaire (**S**chedule) | Faisable avant l'échéance du client ? | prêt après la saison qui compte |

5. **Calculez le coût sur 3 ans** : achat + abonnements + hébergement + formation + **heures de maintenance × un taux** (même bénévole : le temps a une valeur). Écrivez vos hypothèses.
6. **Listez les risques majeurs** de chaque scénario (ils nourriront P2 et S3).
7. **Écrivez la recommandation** : GO sur tel scénario **ou** NO-GO argumenté, **3 arguments maximum**, reliés à la grille, et les **conditions** de réussite (« si 90 % des familles sont inscrites en 3 semaines »). Un NO-GO sur le développement, avec une alternative, est une vraie recommandation.
8. **Après l'oral J2**, remplissez le §6 : la décision du client, ses réserves.

## Exemple

[C5 du club de handball](../exemples/hbc-val-de-furan/C5-etude-faisabilite.md) : S2 éliminé par un 0 en calendaire ; S0 et S1 à égalité de points, départagés par les Must couverts et la confidentialité.

## Pièges à éviter

- Des notes sans justification, ou toutes à 2.
- Un S0 caricatural (« ne rien faire ») pour faire gagner S2.
- Oublier que **vous** ne serez plus là pour maintenir un développement.
- Une recommandation qui contredit la grille sans l'expliquer.

## J'ai fini quand…

- [ ] 3 scénarios, dont un sans développement ;
- [ ] chaque note est justifiée et sourcée ;
- [ ] les coûts sur 3 ans incluent le temps humain ;
- [ ] la recommandation découle de la grille et donne ses conditions.

---
[← Étape 11](E11-rechercher-solutions.md) · [Parcours](../METHODE.md) · [Étape 13 — Fiche RGPD →](E13-rgpd.md)
