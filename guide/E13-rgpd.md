# Étape 13 — Rédiger la fiche RGPD du traitement

> Phase 3 Faisabilité · **Sécuriser** · Artefact : [S2 Fiche RGPD](../modeles/S2-fiche-rgpd.md) (une par traitement) · Jalon **J2** · ⏱ 1 h 30

## Pourquoi cette étape ?

Toute organisation qui traite des données personnelles doit pouvoir dire **pourquoi** elle les collecte, **sur quelle base légale**, **combien de temps** elle les garde et **comment** elle les protège. C'est ce que contient le registre des traitements exigé par le RGPD. Écrire cette fiche **avant** de choisir définitivement la solution permet d'éliminer ce qui est interdit (et de supprimer ce qui est inutile).

## Ce dont vous avez besoin

- [S1](../modeles/S1-donnees-dicp.md) : l'inventaire des données.
- [C4](../modeles/C4-fiche-besoins.md) : la finalité (l'énoncé du besoin) et le périmètre.
- Le scénario recommandé en [C5](../modeles/C5-etude-faisabilite.md) : qui héberge ? (sous-traitant)
- Références : [le registre des traitements (CNIL)](https://www.cnil.fr/fr/RGDP-le-registre-des-activites-de-traitement), [la liste des traitements soumis à AIPD (CNIL)](https://www.cnil.fr/fr/liste-traitements-aipd-requise).

## Comment faire, pas à pas

1. **Découpez en traitements** : un traitement = **une finalité**. « Gérer les adoptions » et « gérer les dons » sont deux traitements, donc deux fiches (`S2-fiche-rgpd-adoptions.md`, `S2-fiche-rgpd-dons.md`). Commencez par le traitement principal de votre recommandation.
2. **Remplissez le tableau §1**. Les rubriques délicates :

   | Rubrique | Comment la remplir |
   |---|---|
   | **Responsable de traitement** | l'organisation (pas vous, pas l'éditeur du logiciel) |
   | **Sous-traitant** | l'éditeur ou l'hébergeur qui traite les données pour son compte |
   | **Base légale** | une des 6 : **consentement**, **contrat** (ou mesures précontractuelles), **obligation légale**, **intérêt légitime**, **mission d'intérêt public**, sauvegarde des intérêts vitaux. Justifiez en une phrase. Le consentement n'est **pas** la base par défaut. |
   | **Données sensibles** | si oui, lesquelles et quelle exception de l'article 9 permet de les traiter — sinon, les **retirer** |
   | **Durées de conservation** | une durée **par catégorie**, avec la raison (« la saison + 1 an pour contester un forfait ») |

3. **§2 Minimisation** : pour **chaque** donnée collectée aujourd'hui ou proposée par l'outil, posez la question « est-ce **nécessaire** à la finalité ? ». Décidez : garder, supprimer, remplacer (ex. date de naissance → tranche d'âge ; adresse complète → commune ; photocopie d'un justificatif → simple vérification visuelle, notée « vu le … »).
4. **§3 Information et droits** : rédigez en annexe le texte d'information (5 à 10 lignes : qui, pourquoi, combien de temps, quels droits, qui contacter) et dites comment une personne exerce ses droits.
5. **§4 AIPD** : parcourez la liste CNIL et les 9 critères européens (données sensibles, personnes vulnérables, grande échelle, croisement, usage innovant, surveillance systématique, évaluation / notation, décision automatique, exclusion d'un droit). **Deux critères ou plus** → AIPD en principe requise. Concluez en une phrase argumentée.
6. **§5 IA** : si la solution envoie des données à un modèle d'IA, où sont-elles traitées ? Réutilisées pour l'entraînement ? Les usagers sont-ils **informés qu'ils échangent avec une IA** (obligation de transparence de l'AI Act, en vigueur depuis le 2 août 2026) ?

## Exemple

[S2 du club de handball](../exemples/hbc-val-de-furan/S2-fiche-rgpd.md) : base légale « contrat d'adhésion », 4 données supprimées par minimisation, AIPD non requise (1 critère sur 9), argumentée.

## Pièges à éviter

- Mettre « consentement » partout.
- « Durée : illimitée » ou « le temps nécessaire ».
- Oublier les données collectées **aujourd'hui** (formulaires papier, messageries) : la minimisation commence par elles.

## J'ai fini quand…

- [ ] une fiche par traitement principal, base légale justifiée ;
- [ ] durées de conservation chiffrées ;
- [ ] au moins une donnée supprimée ou remplacée par minimisation ;
- [ ] conclusion AIPD argumentée.

---
[← Étape 12](E12-faisabilite-telos-couts.md) · [Parcours](../METHODE.md) · [Étape 14 — Registre des risques →](E14-risques-projet.md)
