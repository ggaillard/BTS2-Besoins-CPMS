# Du besoin exprimé à la mise en place

**BTS SIO SLAM — 2e année** · Lycée Simone-Weil, Saint-Priest-en-Jarez · 2026-2027

> **Concevoir · Piloter · Mesurer · Sécuriser**

Cinq organisations ont exprimé un besoin. Aucune ne l'a exprimé clairement, et aucune ne sait ce qu'elle peut raisonnablement obtenir.
Votre équipe en prend une en charge : vous **recueillez** son besoin auprès des personnes concernées, vous **déterminez ce qui est faisable** et vous **préparez la mise en place** — en suivant une méthode et en produisant les artefacts qu'un professionnel produirait.

Le code n'est pas le cœur de ce travail. Il est même possible que la bonne réponse soit de ne pas en écrire.

---

## Les cinq cas

| # | Organisation | Secteur | Ce qu'elle demande | Ce qui rend le cas difficile |
|---|---|---|---|---|
| 1 | [**Refuge SPA Forez-Pilat**](cas/01-spa-forez-pilat/) | Association de protection animale | « Une appli comme les grandes SPA » | Sept membres, sept besoins ; budget nul ; bénévoles de 20 à 75 ans ; données d'adoptants |
| 2 | [**Commune de Saint-Roch-en-Forez**](cas/02-mairie-saint-roch/) | Collectivité territoriale | « Un Doctolib des salles, avec paiement par carte » | Argent public, règles de la comptabilité publique, accessibilité, agents qui n'ont rien demandé |
| 3 | [**Cabinet de kinésithérapie des Tilleuls**](cas/03-cabinet-kine-tilleuls/) | Santé libérale | « Un agent vocal IA qui prend les rendez-vous » | Données de santé, secret professionnel, patients âgés, solution sur mesure risquée |
| 4 | [**Maison Bérard, traiteur**](cas/04-traiteur-maison-berard/) | Artisanat, commerce | « Un site où le client compose son menu et paie » | Deux gérants en désaccord, un incident allergène, saison qui n'attend pas |
| 5 | [**Office de tourisme des Hautes-Chaumes**](cas/05-office-tourisme-hautes-chaumes/) | Établissement public, tourisme | « Un assistant IA qui répond 24 h/24 » | Informations qui changent chaque jour, neutralité envers les prestataires, trois langues, AI Act |

Chaque dossier contient une présentation de l'organisation, le **besoin tel qu'il a été exprimé** (`besoin-exprime.md`), la liste des interlocuteurs que vous pouvez rencontrer et des documents de travail (données fictives).

## La méthode

Tout est dans [**METHODE.md**](METHODE.md). En résumé :

```
 J0 ─► 1. Recueillir ─► J1 Besoin validé ─► 2. Analyser ─► 3. Faisabilité ─► J2 Go / No-go
                                                                                  │
 J4 Bilan ◄─ 5. Piloter et mesurer ◄─ J3 Plan validé ◄─ 4. Préparer la mise en place ◄┘
```

| | Artefacts |
|---|---|
| **Concevoir** | C1 Parties prenantes · C2 Guide d'entretien · C3 Comptes rendus · C4 Fiche besoins · C5 Étude de faisabilité · C6 Dossier de solution |
| **Piloter** | P1 Plan de projet · P2 Registre des risques · P3 Journal de bord · P4 Plan de déploiement |
| **Mesurer** | M1 Situation de départ et indicateurs · M2 Cahier de recette · M3 Bilan |
| **Sécuriser** | S1 Données et DICP · S2 Fiche RGPD · S3 Plan de sécurisation |

Les modèles sont dans [`modeles/`](modeles/), les critères d'évaluation dans [GRILLE-EVALUATION.md](GRILLE-EVALUATION.md).

## Démarrer (séance 1)

1. **Formez votre équipe** (3 ou 4) et répartissez les rôles : animateur·rice, secrétaire, responsable qualité, responsable sécurité. Les rôles tournent à chaque jalon.
2. **Créez le dépôt de l'équipe** à partir de celui-ci : bouton **Use this template → Create a new repository**, en **privé**, nommé `cpms-<cas>-<equipe>` (ex. `cpms-spa-equipe3`). Invitez vos coéquipiers et l'enseignant.
3. **Choisissez ou recevez votre cas**, lisez son `README.md` puis son `besoin-exprime.md`. Ne proposez encore aucune solution.
4. **Préparez GitHub** :
   - *Milestones* : `J1 Besoin validé`, `J2 Go-No-go`, `J3 Plan validé`, `J4 Bilan` ;
   - *Labels* : `concevoir`, `piloter`, `mesurer`, `securiser`, `recit`, `risque` ;
   - un tableau *Projects* (vue Kanban) relié au dépôt.
5. **Ouvrez le journal de bord** : copiez `modeles/P3-journal-de-bord.md` dans `livrables/` et remplissez la première entrée.
6. **Préparez le premier entretien** (C1 puis C2) et demandez un rendez-vous à l'enseignant, qui jouera votre interlocuteur.

## Vérifier où vous en êtes

```bash
python3 outils/verifier.py            # état de tous les livrables
python3 outils/verifier.py --jalon J2 # uniquement ce qui est attendu au jalon J2
```

Le script signale les artefacts manquants, les commentaires `<!-- … -->` non remplacés et les mentions « Usage de l'IA » non remplies. Il ne juge pas la qualité : c'est le rôle des critères en bas de chaque modèle et de la grille.

## Organisation du dépôt

```
├── README.md               ← vous êtes ici
├── METHODE.md              ← phases, jalons, artefacts, règles du jeu
├── GRILLE-EVALUATION.md
├── cas/                    ← les 5 organisations et leurs documents
├── modeles/                ← les 16 modèles d'artefacts
├── livrables/              ← VOS artefacts (voir livrables/README.md)
├── outils/verifier.py
└── .github/ISSUE_TEMPLATE/ ← modèles de tickets : récit utilisateur, risque
```

*Toutes les organisations, personnes et données de ce dépôt sont fictives. Les numéros de téléphone utilisent la plage réservée à la fiction par l'ARCEP.*
