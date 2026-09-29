# Étape 22 — Faire le bilan (produit et projet)

> Phase 5 Piloter et mesurer · **Mesurer** + **Piloter** · Artefacts : [M3 Bilan](../modeles/M3-bilan.md), clôture de [P3](../modeles/P3-journal-de-bord.md) et [P2](../modeles/P2-registre-risques.md) · Jalon **J4** · ⏱ 1 h 30 + oral de 10 min

## Pourquoi cette étape ?

Le bilan répond à deux questions distinctes : **la solution a-t-elle résolu le problème ?** (produit, indicateurs M1) et **avons-nous bien mené le projet ?** (délais, charges, risques). La seconde est celle qui vous fait progresser : c'est aussi elle qui nourrit votre portefeuille E5.

## Ce dont vous avez besoin

- [M1](../modeles/M1-indicateurs.md) (départ et cibles), [M2](../modeles/M2-cahier-recette.md) exécuté, résultats de la [preuve de concept](E21-preuve-de-concept.md) si vous en avez fait une.
- [P1](../modeles/P1-plan-projet.md) (charges et dates prévues), [P2](../modeles/P2-registre-risques.md), [P3](../modeles/P3-journal-de-bord.md) (temps passé réel).

## Comment faire, pas à pas

1. **Copiez le modèle** : `cp modeles/M3-bilan.md livrables/`.
2. **§1 Produit** : pour chaque KPI de M1, départ / cible / **obtenu** — ou **projeté** si la solution n'est pas réellement en service (dites-le, et expliquez sur quoi repose la projection : PoC, recette, exemple d'une organisation comparable).
3. **Expliquez chaque écart** par une cause identifiable (« 3 matchs publiés le mercredi »), pas par « manque de temps ».
4. **§2 Projet** : charge prévue (P1) vs réelle (somme des temps de P3), dates, périmètre livré.
5. **§3 Risques** : lesquels se sont produits ? La parade a-t-elle fonctionné ? Fermez ou mettez à jour les tickets.
6. **§4 Retour du client** : sa réaction, **verbatim**.
7. **§5 Ce que nous referions autrement** : au moins 3 actions **concrètes** pour votre prochain projet.
8. **§6 Portefeuille E5** : chaque membre indique quelles compétences du référentiel ce projet lui permet de justifier, **avec l'artefact qu'il a produit comme preuve** (voir le tableau en bas de la [grille](../GRILLE-EVALUATION.md)).
9. **Clôturez le journal P3** (bilan de fonctionnement) et lancez `python3 outils/verifier.py --jalon J4`.
10. **Oral J4** (10 min) : le problème de départ en un chiffre, ce qui a été décidé, ce qui a été obtenu, ce que vous avez appris.

## Exemple

[M3 du club de handball](../exemples/hbc-val-de-furan/M3-bilan.md) : 5 KPI comparés, écarts expliqués, 3 actions d'amélioration, compétences E5 par membre.

## J'ai fini quand…

- [ ] chaque KPI est comparé à son départ ;
- [ ] les écarts sont expliqués par des causes ;
- [ ] 3 actions d'amélioration concrètes ;
- [ ] `verifier.py --jalon J4` n'affiche plus de ✗.

---
[← Étape 21](E21-preuve-de-concept.md) · [Parcours](../METHODE.md)
