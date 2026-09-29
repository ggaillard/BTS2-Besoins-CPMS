# S2 — Fiche RGPD du traitement · *exemple rédigé*

> **Sécuriser** · Phase 3 · à rendre pour **J2**
>
> Traitement : **Organisation des matchs des équipes jeunes** (convocations, réponses, covoiturage)

## 1. Description du traitement

| Rubrique | Contenu |
|---|---|
| Nom du traitement | Convocations et covoiturage des équipes jeunes |
| Responsable de traitement | HBC Val-de-Furan, représenté par son président |
| Sous-traitant(s) | Éditeur de l'application de gestion d'équipe (hébergement UE selon ses conditions, vérifié le 12/10) |
| Finalité(s) | Convoquer les joueurs aux matchs, recueillir leur présence, organiser les trajets |
| Base légale | **Exécution du contrat d'adhésion** au club : participer aux compétitions fait partie de ce que la famille attend de l'adhésion |
| Personnes concernées | Joueurs mineurs, leurs parents, entraîneurs |
| Catégories de données | Prénom, nom, équipe, présence ; nom, téléphone, e-mail des parents ; places de voiture proposées |
| Données sensibles (art. 9) ? | **Non** — les questionnaires de santé et certificats sont explicitement exclus de l'outil |
| Destinataires | Entraîneur de l'équipe ; bureau (secrétaire) ; parents de l'équipe : **uniquement** les prénoms des joueurs et les places de voiture, pas les coordonnées |
| Transferts hors UE | Aucun selon l'éditeur ; clause à vérifier dans le contrat de sous-traitance |
| Durées de conservation | Comptes et réponses : la saison en cours + 1 an (contestation d'un forfait) ; suppression des familles qui ne renouvellent pas leur licence au 31 octobre |
| Mesures de sécurité | → S3 |

## 2. Minimisation

| Donnée envisagée | Vraiment nécessaire à la finalité ? | Décision |
|---|---|---|
| Date de naissance complète | Non : seule la catégorie (U11, U13…) sert | **remplacée par l'équipe** |
| Adresse postale des familles | Non : le covoiturage se fait depuis la salle | **supprimée** — point de rendez-vous = parking de la salle |
| Photo du joueur | Non | **supprimée** (désactivée dans l'application) |
| Numéro de licence | Non pour convoquer | **non importé** |

> 💡 **Pourquoi ?** L'application proposait par défaut photo et date de naissance. La minimisation, c'est **désactiver** ce qui ne sert pas la finalité, même si l'outil le permet.

## 3. Information et droits des personnes

- Information : texte ajouté au formulaire d'adhésion et affiché à la réunion de lancement (annexe : 8 lignes : qui, pourquoi, combien de temps, droits, contact).
- Droits : demande par e-mail à la secrétaire ; suppression du compte possible par le parent dans l'application.
- Moins de 15 ans : **le compte est celui du parent**, pas de l'enfant.

## 4. Faut-il une AIPD ?

- Critères du CEPD remplis : **personnes vulnérables** (mineurs) — 1 critère sur 9.
- Non remplis : données sensibles, grande échelle (112 joueurs), croisement de données, usage innovant, surveillance systématique, décision automatisée…
- Le traitement ne figure pas dans la liste CNIL des traitements soumis à AIPD.
- **Conclusion : AIPD non requise**, un seul critère étant rempli ; nous le justifions ici et la fiche sera revue si l'outil ajoute des fonctions (géolocalisation, photos).

## 5. Si la solution utilise de l'IA

Sans objet.

---
**Critères de qualité** — [x] base légale justifiée · [x] durées de conservation chiffrées · [x] au moins une donnée supprimée par minimisation · [x] conclusion AIPD argumentée
**Usage de l'IA** : aucun.
