# Démarrer — votre première séance, minute par minute

> Vous ne savez pas par où commencer ? C'est normal. Suivez cette page dans l'ordre, sans sauter d'étape.
> À la fin de la séance, vous aurez : une équipe, un dépôt, un cas compris, une carte des parties prenantes et un premier guide d'entretien prêt.

## Avant tout : ce qu'on attend de vous

On ne vous demande **pas** de programmer une application. On vous demande de faire ce que fait un technicien ou un consultant quand une organisation l'appelle :

1. **écouter** et comprendre le vrai problème ;
2. **chiffrer** la situation ;
3. **comparer** les solutions possibles, y compris ne rien développer ;
4. **recommander** et **préparer** une mise en place réaliste, **mesurable** et **sûre**.

Pour ça, vous suivrez le [parcours en 22 étapes](METHODE.md). Chaque étape a une **fiche méthode** (comment faire), un **modèle** (le document à remplir) et un **exemple rédigé** (le même document rempli pour un petit club de handball).

---

## Séance 1

### ⏱ 0:00 – 0:15 · Comprendre la démarche (toute la classe)

- Lisez la section [« La méthode en une minute »](METHODE.md#1-la-méthode-en-une-minute).
- Regardez le **diagramme d'activité** de la méthode (même section) : il montre qui fait quoi et quand le client valide.
- Parcourez l'[exemple rédigé du club de handball](exemples/hbc-val-de-furan/README.md) : lisez son besoin exprimé, puis ouvrez son [C4](exemples/hbc-val-de-furan/C4-fiche-besoins.md) §1 et §2. Remarquez comment « une appli » est devenu un **problème** à résoudre.

### ⏱ 0:15 – 0:45 · Installer l'équipe et le dépôt → [fiche étape 0](guide/E00-installer-equipe-et-depot.md)

- [ ] Équipe de 3 ou 4 ; rôles répartis (animateur, secrétaire, qualité, sécurité).
- [ ] Dépôt créé avec **Use this template**, privé, nommé `cpms-<cas>-<equipe>` ; coéquipiers et enseignant invités.
- [ ] Jalons `J1` à `J4`, étiquettes `concevoir`, `piloter`, `mesurer`, `securiser`, `recit`, `risque`.
- [ ] Tableau *Projects* créé.
- [ ] `livrables/P3-journal-de-bord.md` copié depuis le modèle, tableau de l'équipe rempli.

### ⏱ 0:45 – 1:00 · Choisir ou recevoir votre cas

| # | Cas | Pour commencer |
|---|---|---|
| 1 | Refuge SPA Forez-Pilat | [README](cas/01-spa-forez-pilat/README.md) |
| 2 | Commune de Saint-Roch-en-Forez | [README](cas/02-mairie-saint-roch/README.md) |
| 3 | Cabinet de kinésithérapie des Tilleuls | [README](cas/03-cabinet-kine-tilleuls/README.md) |
| 4 | Maison Bérard, traiteur | [README](cas/04-traiteur-maison-berard/README.md) |
| 5 | Office de tourisme des Hautes-Chaumes | [README](cas/05-office-tourisme-hautes-chaumes/README.md) |

- [ ] Ouvrez les tickets de la phase 1 (un par artefact : C1, C2, C3, M1, S1), rattachés au jalon J1.

### ⏱ 1:00 – 1:45 · Lire le besoin exprimé → [fiche étape 1](guide/E01-lire-le-besoin-exprime.md)

- [ ] Chacun lit seul le `README.md` puis le `besoin-exprime.md` de votre cas (10 min).
- [ ] Ensemble : classez chaque phrase en 🟥 problème / 🟦 solution imaginée / 🟩 contrainte.
- [ ] Écrivez au moins 5 questions à poser en entretien, dont une par « solution imaginée ».
- [ ] Notez une contradiction et un oubli.

### ⏱ 1:45 – 2:30 · Cartographier les parties prenantes → [fiche étape 2](guide/E02-parties-prenantes.md)

- [ ] `cp modeles/C1-parties-prenantes.md livrables/`
- [ ] Regardez d'abord l'[exemple C1](exemples/hbc-val-de-furan/C1-parties-prenantes.md).
- [ ] Remplissez les §1 à §4 ; choisissez **qui interroger en premier** (quelqu'un qui vit le problème).
- [ ] Commit : `git commit -m "C1 : parties prenantes v1 (closes #n)"`.

### ⏱ 2:30 – 3:15 · Préparer le premier entretien → [fiche étape 3](guide/E03-preparer-entretien.md)

- [ ] `cp modeles/C2-guide-entretien.md livrables/C2-guide-entretien-<interlocuteur>.md`
- [ ] Regardez l'[exemple C2](exemples/hbc-val-de-furan/C2-guide-entretien-coach.md).
- [ ] 3 objectifs, 6 à 8 questions ouvertes, une question sur les chiffres, une sur les données, une sur les contraintes.
- [ ] Lisez-le à voix haute : moins de 10 minutes ?
- [ ] Commit, puis **demandez un créneau d'entretien** à l'enseignant pour la séance 2.

### ⏱ 3:15 – 3:30 · Clôturer la séance

- [ ] Entrée « Séance 1 » du journal de bord : météo, fait, décisions, prévu, temps passé.
- [ ] `python3 outils/verifier.py --jalon J1` : C1 doit être ◐ ou ✓, le reste ✗ (c'est normal).
- [ ] Tout est poussé (`git push`).

---

## Et ensuite ?

| Séance | Vous faites | Fiches |
|---|---|---|
| 2 | Entretiens, comptes rendus, chiffrage des CSV, inventaire des données | [E04](guide/E04-mener-entretien-compte-rendu.md) · [E05](guide/E05-chiffrer-situation-depart.md) · [E06](guide/E06-donnees-et-dicp.md) |
| 3 | Entretiens complémentaires, validation des comptes rendus → **J1** ; reformulation du besoin | [E07](guide/E07-reformuler-le-besoin.md) |
| 4 | Récits utilisateur, indicateurs, DICP, recherche de solutions, faisabilité | [E08](guide/E08-recits-gherkin-moscow.md) · [E09](guide/E09-indicateurs.md) · [E11](guide/E11-rechercher-solutions.md) · [E12](guide/E12-faisabilite-telos-couts.md) |
| 5 | RGPD, risques, **oral J2**, puis dossier de solution | [E13](guide/E13-rgpd.md) · [E14](guide/E14-risques-projet.md) · [E15](guide/E15-presenter-go-no-go.md) · [E16](guide/E16-dossier-solution.md) |
| 6 | Plan de projet, déploiement, recette, sécurisation → **J3** | [E17](guide/E17-plan-projet-raci.md) · [E18](guide/E18-deploiement.md) · [E19](guide/E19-recette.md) · [E20](guide/E20-securisation.md) |
| 7 | Preuve de concept (optionnelle), bilan, **oral J4** | [E21](guide/E21-preuve-de-concept.md) · [E22](guide/E22-bilan.md) |

Le détail de chaque étape est dans le [parcours](METHODE.md).
