# Étape 16 — Décrire la solution retenue

> Phase 4 Préparer la mise en place · **Concevoir** · Artefact : [C6 Dossier de solution](../modeles/C6-dossier-solution.md) · Jalon **J3** · ⏱ 2 h

## Pourquoi cette étape ?

Le client a dit oui à un scénario. Il faut maintenant le décrire assez précisément pour que quelqu'un d'autre puisse le **mettre en place** : quels écrans, quelle organisation des données, quels comptes, et pourquoi ces choix. Les décisions importantes sont écrites (ADR) pour qu'on sache plus tard pourquoi on les a prises.

## Ce dont vous avez besoin

- [C5](../modeles/C5-etude-faisabilite.md) : le scénario retenu et les réserves du client (§6).
- [C4](../modeles/C4-fiche-besoins.md) : récits Must, ENF.
- [S1](../modeles/S1-donnees-dicp.md) et [S2](../modeles/S2-fiche-rgpd.md) : données, droits, minimisation.

## Comment faire, pas à pas

1. **Copiez le modèle** : `cp modeles/C6-dossier-solution.md livrables/`.
2. **§1 — La solution en une page** : qui fait quoi, avec quoi, à quel moment. Un non-informaticien doit comprendre.
3. **§2 — Un écran par récit Must**, au minimum :
   - solution **du marché** → créez un compte de test, configurez-le avec des **données fictives**, faites des **captures** ;
   - solution **sur mesure** → maquette (outil de maquettage gratuit, ou papier photographié) ;
   - solution **sans outil** (S0) → le document d'organisation lui-même (planning type, message type, affiche).
   Rangez les images dans `livrables/annexes/` et insérez-les : `![Écran US-01](annexes/us01.png)`.
4. **§3 — Architecture** : un schéma Mermaid avec les **acteurs**, les **outils** et les **flux de données** (qui envoie quoi à qui). Précisez l'hébergement et la localisation des données, les comptes et leurs droits, les liens avec l'existant.
5. **§4 — ADR** : une fiche pour chaque décision **difficile à défaire** (choix de l'outil, modèle de comptes, hébergement, ce qu'on ne reprend pas). Toujours : contexte, options, décision, conséquences **positives et négatives**.
6. **§5 — Reprise des données** : d'où viennent-elles, en quel état, comment on les reprend (ou pourquoi on ne les reprend pas). Ouvrez les vrais fichiers avant d'estimer.

## Exemple

[C6 du club de handball](../exemples/hbc-val-de-furan/C6-dossier-solution.md) : captures de l'outil configuré, schéma des flux, 2 ADR (outil du marché ; comptes au nom des parents).

## Pièges à éviter

- Des maquettes remplies de vraies données personnelles : **toujours fictives**.
- Oublier les écrans des utilisateurs secondaires (l'administrateur, celui qui n'a pas de smartphone).
- Un schéma d'architecture purement technique (serveurs, ports) sans les personnes.

## J'ai fini quand…

- [ ] chaque Must a son écran ou son document ;
- [ ] au moins 2 ADR ;
- [ ] hébergement, localisation des données et droits sont précisés ;
- [ ] la reprise de l'existant est traitée.

---
[← Étape 15](E15-presenter-go-no-go.md) · [Parcours](../METHODE.md) · [Étape 17 — Plan de projet →](E17-plan-projet-raci.md)
