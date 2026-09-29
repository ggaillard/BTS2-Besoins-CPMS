# Étape 2 — Cartographier les parties prenantes

> Phase 1 Recueillir · **Concevoir** · Artefact : [C1 Carte des parties prenantes](../modeles/C1-parties-prenantes.md) · Jalon **J1** · ⏱ 45 min

## Pourquoi cette étape ?

Un projet échoue rarement pour une raison technique ; il échoue parce qu'on a oublié quelqu'un : celui qui décide et n'a pas été convaincu, celui qui devra utiliser l'outil et ne le voulait pas, celui dont on traite les données sans le lui dire. C1 vous oblige à les nommer **avant** d'aller en entretien, et vous dit **qui interroger en premier**.

## Ce dont vous avez besoin

- Le README de votre cas (tableau « Interlocuteurs que vous pouvez rencontrer »).
- Vos notes de l'[étape 1](E01-lire-le-besoin-exprime.md) (oublis, contradictions).

## Comment faire, pas à pas

1. **Copiez le modèle** : `cp modeles/C1-parties-prenantes.md livrables/`.
2. **Listez tout le monde**, en trois cercles :
   - ceux qui sont **dans** l'organisation et **cités** dans le besoin exprimé ;
   - ceux qui sont dans l'organisation mais **pas cités** (les agents, les bénévoles discrets, la personne qui fait déjà le travail à la main) ;
   - ceux qui sont **dehors** : clients, usagers, familles, partenaires, autorités (CNIL, administration, fédération…), personnes dont on traite les données.
3. **Pour chacun, remplissez** : ce qu'il **attend**, ce qu'il **craint** (souvent plus révélateur), son **influence** sur la décision (1 à 3) et son **intérêt** pour le projet (1 à 3).
4. **Placez-les dans la matrice** (le graphique `quadrantChart` du modèle) : remplacez la ligne d'exemple par une ligne par personne, `Nom: [intérêt, influence]` avec des valeurs entre 0 et 1.
5. **Répondez aux quatre questions** du §3 : qui décide, qui paie, qui utilise, de qui traite-t-on les données. Si c'est la même personne partout, vous avez mal cherché.
6. **Planifiez les entretiens** (§4) : **commencez par quelqu'un qui vit le problème au quotidien**, pas forcément par le décideur. Pour chacun, écrivez **ce que vous voulez apprendre de lui**.
7. **Commitez** et fermez le ticket.

## Exemple

[C1 du club de handball](../exemples/hbc-val-de-furan/C1-parties-prenantes.md) : le besoin vient du président, mais le premier entretien est avec un entraîneur ; les entraîneurs mineurs sont repérés comme oubliés.

## Pièges à éviter

- Recopier la liste des interlocuteurs du README sans rien ajouter.
- Oublier les personnes dont on traite les données (adoptants, patients, enfants…) : elles ne parlent pas, mais le RGPD les protège.
- Remplir « Ce qu'elle craint » par « rien ».

## J'ai fini quand…

- [ ] au moins une partie prenante n'était pas citée dans le besoin exprimé ;
- [ ] le décideur, le financeur et les utilisateurs sont identifiés ;
- [ ] 2 ou 3 entretiens sont planifiés, chacun avec un objectif ;
- [ ] les critères de qualité en bas du modèle sont cochés.

---
[← Étape 1](E01-lire-le-besoin-exprime.md) · [Parcours](../METHODE.md) · [Étape 3 — Préparer un entretien →](E03-preparer-entretien.md)
