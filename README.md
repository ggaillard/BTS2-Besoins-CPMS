# Du besoin exprimé à la mise en place

**BTS SIO SLAM — 2e année** ·

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

## Par où commencer ?

| Vous êtes… | Ouvrez |
|---|---|
| en **première séance** | 👉 [**DEMARRER.md**](DEMARRER.md) — la séance 1 minute par minute |
| à une étape donnée | 👉 [**METHODE.md**](METHODE.md) — le parcours en 22 étapes, avec pour chacune la fiche, le modèle, l'exemple et les documents de votre cas |
| perdu devant un modèle | 👉 l'[**exemple rédigé**](exemples/hbc-val-de-furan/README.md) du même artefact, puis la [**fiche méthode**](guide/README.md) de l'étape |
| en train de chercher à **visualiser un processus** ou à **faire un choix** | 👉 les [**diagrammes UML**](guide/schemas-uml.md) et les [**arbres de décision**](guide/arbres-de-decision.md) ; pour dessiner les vôtres : l'[**aide-mémoire UML**](guide/aide-memoire-uml-mermaid.md) |
| bloqué sur un mot | 👉 le [**lexique**](guide/lexique.md) |
| en train de vous demander comment vous serez évalués | 👉 [GRILLE-EVALUATION.md](GRILLE-EVALUATION.md) |

## La méthode en bref

```
 J0 ─► Phase 1 Recueillir ─► J1 Besoin validé ─► Phase 2 Analyser ─► Phase 3 Faisabilité ─► J2 Go / No-go
       (étapes 0-6)                               (étapes 7-10)        (étapes 11-15)            │
 J4 Bilan ◄─ Phase 5 Piloter et mesurer ◄─ J3 Plan validé ◄─ Phase 4 Préparer la mise en place ◄─┘
             (étapes 21-22)                                  (étapes 16-20)
```

| | Artefacts (un modèle chacun dans [`modeles/`](modeles/), un exemple dans [`exemples/`](exemples/hbc-val-de-furan/)) |
|---|---|
| 🟦 **Concevoir** | C1 Parties prenantes · C2 Guide d'entretien · C3 Comptes rendus · C4 Fiche besoins · C5 Étude de faisabilité · C6 Dossier de solution |
| 🟧 **Piloter** | P1 Plan de projet · P2 Registre des risques · P3 Journal de bord · P4 Plan de déploiement |
| 🟩 **Mesurer** | M1 Situation de départ et indicateurs · M2 Cahier de recette · M3 Bilan |
| 🟥 **Sécuriser** | S1 Données et DICP · S2 Fiche RGPD · S3 Plan de sécurisation |

## Vérifier où vous en êtes

```bash
python3 outils/verifier.py            # état de tous les livrables
python3 outils/verifier.py --jalon J2 # uniquement ce qui est attendu au jalon J2
```

Le script signale les artefacts manquants, les marqueurs `⟪ … ⟫` non remplacés et les mentions « Usage de l'IA » non remplies. Il ne juge pas la qualité : c'est le rôle des critères en bas de chaque modèle et de la grille.

## Organisation du dépôt

```
├── README.md               ← vous êtes ici
├── DEMARRER.md             ← la première séance, pas à pas
├── METHODE.md              ← le parcours en 22 étapes, jalons, règles du jeu
├── GRILLE-EVALUATION.md
├── guide/                  ← fiches méthode, diagrammes UML, arbres de décision, aide-mémoire UML, lexique
├── exemples/               ← les 16 artefacts rédigés sur un mini-cas (club de handball)
├── cas/                    ← les 5 organisations et leurs documents
├── modeles/                ← les 16 modèles d'artefacts à copier
├── livrables/              ← VOS artefacts (voir livrables/README.md)
├── outils/verifier.py
└── .github/ISSUE_TEMPLATE/ ← modèles de tickets : récit utilisateur, risque
```

*Toutes les organisations, personnes et données de ce dépôt sont fictives. Les numéros de téléphone utilisent la plage réservée à la fiction par l'ARCEP.*
