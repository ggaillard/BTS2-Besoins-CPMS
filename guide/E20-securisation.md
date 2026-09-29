# Étape 20 — Rédiger le plan de sécurisation

> Phase 4 Préparer la mise en place · **Sécuriser** · Artefact : [S3 Plan de sécurisation](../modeles/S3-plan-securisation.md) · Jalon **J3**, mesures vérifiées à **J4** · ⏱ 1 h 30

## Pourquoi cette étape ?

S1 a dit **ce qui** doit être protégé et à quel point. S3 dit **contre quoi** et **comment**. Pour une petite organisation, les menaces réalistes sont rarement des pirates sophistiqués : ce sont un ancien membre qui garde ses accès, un mot de passe partagé, un fichier perdu, un outil qui ferme. Le plan doit traiter **ces** menaces-là, avec des mesures que l'organisation peut vraiment appliquer.

## Ce dont vous avez besoin

- [S1](../modeles/S1-donnees-dicp.md) (notes DICP, failles de l'existant), [S2](../modeles/S2-fiche-rgpd.md), [C6](../modeles/C6-dossier-solution.md) (comptes, hébergement).
- Référence : [guide d'hygiène informatique de l'ANSSI](https://messervices.cyber.gouv.fr/guides/guide-dhygiene-informatique) (42 mesures ; piochez celles qui s'appliquent).

## Comment faire, pas à pas

1. **Copiez le modèle** : `cp modeles/S3-plan-securisation.md livrables/`.
2. **§1 Scénarios de menace** : partez de chaque donnée notée **3 ou 4** dans S1 et de chaque faille de l'existant. Pour chacune : **qui** pourrait nuire (ancien membre, usager curieux, erreur interne, fournisseur, attaquant opportuniste), **comment**, quel critère DICP est touché. Cotez vraisemblance et gravité (1 à 4).
3. **§2 Mesures** : au moins une par scénario. Mélangez :
   - **techniques** : comptes nominatifs, double authentification, droits limités, chiffrement, mises à jour ;
   - **organisationnelles** : procédure de départ d'un membre, règle « jamais de pièce médicale par messagerie », changement d'un code, charte d'une page.
   Pour chacune, indiquez l'**effort** et le **responsable**, et le test M2 qui la vérifie.
4. **§3 Comptes et droits** : un tableau par profil — ce qu'il voit, ce qu'il modifie, ce qu'il **ne doit pas** voir.
5. **§4 Sauvegarde** : règle **3-2-1** (3 copies, 2 supports différents, 1 hors site) adaptée à l'organisation, et un **test de restauration** daté : une sauvegarde jamais restaurée n'est pas une sauvegarde.
6. **§5 Continuité et réversibilité** : que fait-on si l'outil est indisponible une semaine ? Comment récupère-t-on les données si on veut en changer ?
7. **§6 Risques résiduels** : ce qui reste, et **qui côté client l'accepte** (nom, date).

## Exemple

[S3 du club de handball](../exemples/hbc-val-de-furan/S3-plan-securisation.md) : 5 menaces réalistes, 6 mesures dont la moitié organisationnelles, test de restauration daté.

## Pièges à éviter

- Recopier une liste générique (rançongiciel, attaque par déni de service…) sans lien avec le cas.
- Des mesures que l'organisation ne peut pas appliquer (« recruter un responsable sécurité »).
- Oublier la réversibilité : rester prisonnier d'un outil est un risque.

## J'ai fini quand…

- [ ] chaque scénario a au moins une mesure ;
- [ ] au moins une mesure organisationnelle ;
- [ ] test de restauration planifié ;
- [ ] risques résiduels acceptés par le client.

**Jalon J3** : C6, P1, P4, M2, S3 doivent être commités.

---
[← Étape 19](E19-recette.md) · [Parcours](../METHODE.md) · [Étape 21 — Preuve de concept (optionnelle) →](E21-preuve-de-concept.md)
