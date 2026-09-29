# Cas 3 — Cabinet de kinésithérapie des Tilleuls

> Professionnels de santé libéraux · prise de rendez-vous et accueil téléphonique · **organisation fictive**

## L'organisation

| | |
|---|---|
| Statut | 4 masseurs-kinésithérapeutes libéraux associés en société civile de moyens (SCM) : ils partagent les locaux et la secrétaire, chacun a sa patientèle |
| Personnel | 1 secrétaire salariée de la SCM, 20 h par semaine (le matin) ; 1 kinésithérapeute collaborateur 3 jours par semaine |
| Activité | ≈ 110 séances par jour ; rééducation post-opératoire, rhumatologie, pédiatrie respiratoire l'hiver |
| Ouverture | 7 h 30 – 20 h du lundi au vendredi, samedi matin |
| Situation | Commune périurbaine ; forte demande, délai de 3 à 5 semaines pour un nouveau patient |

## L'informatique aujourd'hui

- Chaque kiné utilise le même **logiciel métier** de kinésithérapie (dossier patient, facturation à l'Assurance maladie avec la carte Vitale, agenda). L'agenda est commun, mais le logiciel n'est installé que sur les postes du cabinet.
- Le téléphone fixe sonne sur le poste de la secrétaire le matin, puis bascule sur un répondeur l'après-midi ; les kinés rappellent entre deux patients.
- Une **liste d'attente** papier (nom, téléphone, pathologie, prescripteur) est posée sur le bureau d'accueil.
- Les rappels de rendez-vous ne sont pas envoyés.
- Une adresse mail générique est relevée « quand on a le temps ».

## Ce qui vous est confié

Les associés se disent « noyés sous le téléphone ». L'un d'eux a vu une démonstration d'agent vocal à base d'IA dans un salon professionnel et voudrait « la même chose ». Ils attendent de votre équipe une étude sérieuse : qu'est-ce qui est faisable, à quel coût, avec quels risques, et comment le mettre en place sans désorganiser le cabinet.

Lisez d'abord [`besoin-exprime.md`](besoin-exprime.md).

## Par où commencer ?

1. **Ne cherchez pas encore de solution.** Suivez le [parcours de la méthode](../../METHODE.md) ; pour la première séance, [DEMARRER.md](../../DEMARRER.md).
2. **Lisez ce README en entier**, puis [`besoin-exprime.md`](besoin-exprime.md), en appliquant la [fiche de l'étape 1](../../guide/E01-lire-le-besoin-exprime.md) : séparez problèmes, solutions imaginées et contraintes.
3. **Cartographiez les interlocuteurs** ci-dessous avec la [fiche de l'étape 2](../../guide/E02-parties-prenantes.md) et choisissez qui interroger en premier.
4. **Préparez votre premier entretien** ([étape 3](../../guide/E03-preparer-entretien.md)).
5. **Ouvrez les fichiers de données** avant la séance 2 : ils serviront à chiffrer la situation ([étape 5](../../guide/E05-chiffrer-situation-depart.md)).

### Quel document sert à quoi

| Document | Ce qu'il contient | Étapes où vous en aurez besoin |
|---|---|---|
| [`besoin-exprime.md`](besoin-exprime.md) | la note vocale du gérant | 1 (lire), 2 (C1) |
| [`documents/journal-appels.csv`](documents/journal-appels.csv) | une semaine d'appels entrants | 5 (M1) |
| [`documents/rendez-vous-non-honores.csv`](documents/rendez-vous-non-honores.csv) | un mois de rendez-vous manqués | 5 (M1), 6 (S1) |

## Interlocuteurs que vous pouvez rencontrer

| Personne | Rôle |
|---|---|
| Julien Rey | Kinésithérapeute associé, gérant de la SCM, à l'origine de la demande |
| Claire Bonnefoy | Kinésithérapeute associée, la plus ancienne du cabinet |
| Samia Haddad | Secrétaire |
| Thomas Vernet | Kinésithérapeute collaborateur, 28 ans |
| Un·e patient·e | Patient·e régulier·ère, 67 ans, rééducation après prothèse de genou |

## Documents fournis

| Fichier | Contenu |
|---|---|
| [`documents/journal-appels.csv`](documents/journal-appels.csv) | Relevé des appels entrants d'une semaine, tenu à la main par la secrétaire à la demande du gérant |
| [`documents/rendez-vous-non-honores.csv`](documents/rendez-vous-non-honores.csv) | Les rendez-vous non honorés de mars 2026, extraits du logiciel métier (sur **2 350 séances programmées** ce mois-là) ; les patients sont pseudonymisés |

Toutes les données sont fictives.
