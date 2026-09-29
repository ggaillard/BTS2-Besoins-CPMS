# Étape 17 — Planifier la mise en place (lots, planning, RACI, budget)

> Phase 4 Préparer la mise en place · **Piloter** · Artefact : [P1 Plan de projet](../modeles/P1-plan-projet.md) · Jalon **J3** · ⏱ 1 h 30

## Pourquoi cette étape ?

Une bonne solution mal organisée échoue. Le plan de projet répond à quatre questions que tout décideur pose : **quoi** (les lots), **quand** (le planning), **qui** (le RACI), **combien** (charges et budget).

## Ce dont vous avez besoin

- [C6](../modeles/C6-dossier-solution.md) (ce qu'il faut mettre en place), [C5](../modeles/C5-etude-faisabilite.md) (coûts), [P2](../modeles/P2-registre-risques.md) (risques à intégrer au planning), l'échéance du client.

## Comment faire, pas à pas

1. **Copiez le modèle** : `cp modeles/P1-plan-projet.md livrables/`.
2. **Découpez en 4 à 6 lots**, chacun avec un **livrable vérifiable**. Lots presque toujours présents : paramétrage ou développement, reprise des données, recette, formation et lancement, suivi.
3. **Estimez la charge** de chaque lot en heures (ou jours·homme). Méthode simple : découpez en tâches d'une heure à une demi-journée et additionnez ; ajoutez 20 % d'aléas.
4. **Planifiez** avec le diagramme de Gantt Mermaid du modèle : remplacez les dates et les durées. Faites **partir du jalon imposé** par le client et remontez le temps.
5. **Créez les jalons** dans GitHub (*Issues → Milestones*) avec les mêmes dates.
6. **RACI** : une ligne par activité, une colonne par acteur.
   - **R** — *Responsible* : fait le travail (plusieurs possibles) ;
   - **A** — *Accountable* : rend des comptes, valide — **un seul par ligne** ;
   - **C** — *Consulted* : donne son avis avant ;
   - **I** — *Informed* : est prévenu après.
   Les décisions de l'organisation (signer, dépenser, généraliser) ont toujours un **A côté client**.
7. **Budget** : reprenez C5, séparez argent et temps, et dites **qui paie**.
8. **Gouvernance** : fréquence des points d'avancement, qui tranche un désaccord.

## Exemple

[P1 du club de handball](../exemples/hbc-val-de-furan/P1-plan-projet.md) : 5 lots, 18 h, Gantt, RACI avec un seul A par ligne.

## Pièges à éviter

- Oublier la formation et l'accompagnement dans les charges.
- Un RACI où l'équipe étudiante est **A** partout.
- Un planning qui ignore les contraintes du client (saison, conseil municipal, vacances).

## J'ai fini quand…

- [ ] lots avec livrables et charges ;
- [ ] Gantt cohérent avec l'échéance, jalons reportés dans GitHub ;
- [ ] un seul A par ligne du RACI ;
- [ ] budget cohérent avec C5.

---
[← Étape 16](E16-dossier-solution.md) · [Parcours](../METHODE.md) · [Étape 18 — Déploiement →](E18-deploiement.md)
