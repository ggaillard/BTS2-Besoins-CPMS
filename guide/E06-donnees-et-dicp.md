# Étapes 6 et 10 — Inventorier les données, puis coter leurs besoins de sécurité (DICP)

> **Sécuriser** · Artefact : [S1 Données et besoins DICP](../modeles/S1-donnees-dicp.md)
> §1 Inventaire : Phase 1, jalon **J1** (étape 6, ⏱ 30 min) · §2 Cotation DICP : Phase 2, jalon **J2** (étape 10, ⏱ 45 min)

## Pourquoi ces étapes ?

On ne protège bien que ce qu'on connaît. Avant de choisir une solution, il faut savoir **quelles informations** elle va manipuler, **sur qui**, et **ce qui arriverait** si elles étaient perdues, fausses ou divulguées. C'est ce qui décidera plus tard de l'hébergement, des droits, des sauvegardes — et parfois qu'une solution est impossible (données de santé, par exemple).

## Ce dont vous avez besoin

- Vos [C3](../modeles/C3-compte-rendu-entretien.md), §4 « Données personnelles repérées ».
- Les documents du cas : les colonnes des CSV, les formulaires (ex. [formulaire d'adoption](../cas/01-spa-forez-pilat/documents/formulaire-adoption-actuel.md) de la SPA), les captures de messagerie.

## Étape 6 — Inventaire (§1)

1. **Copiez le modèle** : `cp modeles/S1-donnees-dicp.md livrables/`.
2. **Une ligne par ensemble de données** (ex. « fiches des adoptants », pas « nom », « prénom », « adresse » séparément).
3. Pour chacune : **qui** elle concerne, **personnelle ?** (permet-elle d'identifier quelqu'un, même indirectement ?), **sensible ?**, **où** elle est aujourd'hui, **qui** y accède, **combien**.
4. **Données sensibles au sens du RGPD** (article 9) : santé, opinions politiques, convictions religieuses, origine, orientation sexuelle, données biométriques ou génétiques, appartenance syndicale. Attention : « allergique aux fruits à coque » ou « problème de santé dans le foyer » **sont** des données de santé.
5. **Signalez aussi** : données de **mineurs**, numéro de sécurité sociale, coordonnées bancaires, mots de passe partagés — même si ce ne sont pas des « données sensibles » au sens strict.
6. **§3 Ce que révèle l'existant** : relevez les failles actuelles (mot de passe connu de tous, fichier sur un ordinateur personnel, adresses diffusées dans un groupe). Constatez **sans juger** : les gens se sont organisés avec ce qu'ils avaient.

## Étape 10 — Cotation DICP (§2)

Pour chaque ensemble de données, notez de **1 (faible) à 4 (vital)** :

| Critère | La question à se poser | Exemple de note 4 |
|---|---|---|
| **D**isponibilité | Que se passe-t-il si la donnée est **inaccessible** au moment où on en a besoin ? | La liste des réservations est illisible à l'ouverture : impossible de remettre les documents aux lecteurs qui se déplacent |
| **I**ntégrité | Que se passe-t-il si elle est **fausse** ou modifiée ? | Un document est marqué « rendu » alors qu'il ne l'a pas été : le lecteur suivant attend en vain, le précédent n'est jamais relancé |
| **C**onfidentialité | Que se passe-t-il si **quelqu'un qui ne devrait pas** la voit ? | La liste des emprunts d'un lecteur (qui révèle ses centres d'intérêt, sa santé, ses opinions) est vue par un autre lecteur |
| **P**reuve | A-t-on besoin de savoir **qui a fait quoi, quand** ? | Qui a effacé l'amende d'un lecteur ? (contrôle, contestation) |

**Chaque note se justifie par une conséquence concrète**, dans votre cas, pas par « c'est important ».

## Exemple

[S1 du club de handball](../exemples/hbc-val-de-furan/S1-donnees-dicp.md) : la donnée de santé est notée C=4… pour décider de l'**exclure** de l'outil.

## Pièges à éviter

- Tout noter 4 : si tout est vital, rien ne l'est. Les notes servent à **prioriser** les mesures de S3.
- Oublier les données « de travail » qui ne concernent pas des personnes mais dont dépend le service (plannings, fiches produits, disponibilités).
- Confondre « personnelle » et « sensible ».

## J'ai fini quand…

- [ ] toutes les données citées dans les C3 sont inventoriées (J1) ;
- [ ] chaque note DICP est justifiée par une conséquence (J2) ;
- [ ] les failles de l'existant sont listées.

---
[← Étape 5](E05-chiffrer-situation-depart.md) · [Parcours](../METHODE.md) · [Étape 7 — Reformuler le besoin →](E07-reformuler-le-besoin.md)
