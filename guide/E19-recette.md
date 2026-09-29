# Étape 19 — Écrire (puis exécuter) le cahier de recette

> **Mesurer** · Artefact : [M2 Cahier de recette](../modeles/M2-cahier-recette.md) · rédigé en Phase 4 (**J3**), exécuté en Phase 5 (**J4**) · ⏱ 1 h 30

## Pourquoi cette étape ?

La recette, c'est le moment où **le client** vérifie que ce qu'on lui livre fait bien ce qui était convenu. Les tests s'écrivent **avant** la mise en place, à partir des critères d'acceptation de C4 : sinon on teste ce qu'on a fait, pas ce qu'on avait promis.

## Ce dont vous avez besoin

- [C4](../modeles/C4-fiche-besoins.md) : récits Must et leurs scénarios Gherkin, ENF.
- [S3](../modeles/S3-plan-securisation.md) : les mesures de sécurité à vérifier (vous pouvez écrire M2 et S3 en parallèle).

## Comment faire, pas à pas

1. **Copiez le modèle** : `cp modeles/M2-cahier-recette.md livrables/`.
2. **§1 Stratégie** : **qui** exécute (un utilisateur réel, pas l'équipe), **où** (compte de test, données fictives).
3. **Transformez chaque scénario Gherkin en test** :

   | Gherkin (C4) | Colonne de M2 |
   |---|---|
   | Étant donné… | Préconditions |
   | Quand… | Étapes (numérotées, cliquables par quelqu'un qui découvre) |
   | Alors… | Résultat attendu |

4. **Ajoutez** :
   - au moins **deux tests de sécurité** : quelqu'un qui ne devrait pas voir une donnée essaie de la voir ; un compte désactivé essaie de se connecter ;
   - un test de **réversibilité** : export des données ;
   - un test par **ENF** chiffrée (chronométrer, tester sur téléphone…).
5. **Au jalon J4** (ou sur votre preuve de concept), faites exécuter, remplissez « Obtenu », « OK / KO », et ouvrez un ticket par anomalie.
6. **§3 Procès-verbal** : recette prononcée, avec réserves (lesquelles) ou refusée. Signée côté client.

## Exemple

[M2 du club de handball](../exemples/hbc-val-de-furan/M2-cahier-recette.md) : 9 tests dont 3 de sécurité et 1 de réversibilité ; un KO corrigé ; recette prononcée avec réserves.

## Pièges à éviter

- Des tests que seul le concepteur sait exécuter.
- « Résultat attendu : ça marche ».
- Considérer un KO comme un échec : c'est à ça que sert la recette.

## J'ai fini quand…

- [ ] 100 % des Must ont au moins un test ;
- [ ] au moins 2 tests de sécurité et 1 de réversibilité ;
- [ ] (J4) le PV est rempli et signé.

---
[← Étape 18](E18-deploiement.md) · [Parcours](../METHODE.md) · [Étape 20 — Plan de sécurisation →](E20-securisation.md)
