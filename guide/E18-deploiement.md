# Étape 18 — Préparer le déploiement et l'accompagnement

> Phase 4 Préparer la mise en place · **Piloter** · Artefact : [P4 Plan de déploiement et d'accompagnement](../modeles/P4-plan-deploiement.md) · Jalon **J3** · ⏱ 1 h

## Pourquoi cette étape ?

Le jour de la mise en service, ce ne sont pas des informaticiens qui utilisent la solution : ce sont des bénévoles, des agents, des secrétaires, des clients. Si personne ne les a prévenus, formés ni rassurés, ils reviendront à l'ancienne méthode en une semaine. Et si ça tourne mal, il faut savoir **quand** et **comment** revenir en arrière.

## Ce dont vous avez besoin

- [C1](../modeles/C1-parties-prenantes.md) (qui est concerné, qui craint quoi), [C6](../modeles/C6-dossier-solution.md) (reprise des données), [P1](../modeles/P1-plan-projet.md) (dates), [P2](../modeles/P2-registre-risques.md) (risques d'adoption).

## Comment faire, pas à pas

1. **Copiez le modèle** : `cp modeles/P4-plan-deploiement.md livrables/`.
2. **Choisissez la stratégie de bascule** et justifiez-la :

   | Stratégie | Quand l'utiliser |
   |---|---|
   | Big bang | peu d'utilisateurs, faible risque, ancien système impossible à garder |
   | **Pilote puis généralisation** | beaucoup d'utilisateurs, incertitude sur l'adoption — le plus fréquent |
   | Double fonctionnement | quand on ne peut pas se permettre de perdre une information pendant la transition (limité dans le temps !) |

3. **Écrivez le critère de retour arrière** : un seuil chiffré (« moins de 70 % d'inscrits à 3 semaines ») et la décision associée.
4. **Listez les étapes de mise en service** dans l'ordre, avec une **vérification** pour chacune. La première est toujours : **sauvegarder l'existant**.
5. **Un public = une action d'accompagnement** : reprenez chaque partie prenante de C1 et écrivez ce qui change pour elle et comment vous l'aidez (démonstration, tutoriel d'une page, affiche, permanence, appel personnel pour ceux qui sont éloignés du numérique).
6. **Communication** : qui annonce quoi, à qui, quand. Le message officiel vient de l'organisation, pas de vous.
7. **Après** : qui répond aux questions le premier mois ? Qui administre ensuite ? Avec quelle documentation ?

## Exemple

[P4 du club de handball](../exemples/hbc-val-de-furan/P4-plan-deploiement.md) : pilote sur 3 équipes, double fonctionnement de 3 semaines, retour arrière à moins de 70 % d'inscrits.

## Pièges à éviter

- Un plan qui ne parle que de technique.
- Oublier les personnes sans smartphone ou peu à l'aise.
- Un double fonctionnement sans date de fin (tout le monde reste sur l'ancien).

## J'ai fini quand…

- [ ] stratégie justifiée et critère de retour arrière chiffré ;
- [ ] chaque public de C1 a une action d'accompagnement ;
- [ ] la maintenance après le projet a un responsable nommé.

---
[← Étape 17](E17-plan-projet-raci.md) · [Parcours](../METHODE.md) · [Étape 19 — Cahier de recette →](E19-recette.md)
