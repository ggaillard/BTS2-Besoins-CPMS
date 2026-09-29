# C5 — Étude de faisabilité et scénarios · *exemple rédigé*

> **Concevoir** · Phase 3 Faisabilité · présentée au jalon **J2 — Go / No-go**

## 1. Les scénarios étudiés

| | S0 — Règle commune | S1 — Application de gestion d'équipe du marché | S2 — Application sur mesure |
|---|---|---|---|
| Description | Convocation le **mardi soir** avec un message type (lieu, heure, adresse) et un **sondage** intégré à la messagerie existante ; tableau des conducteurs épinglé | Application gratuite (offre associative) de gestion d'équipe sportive : convocations, réponses en un geste, rappels, covoiturage. Nous en avons comparé 3 (annexe) | Application web développée par des étudiants : convocations, réponses, covoiturage |
| Récits Must couverts (C4) | 2 / 3 (pas de vue synthétique fiable) | 3 / 3 | 3 / 3 |

> 💡 **Pourquoi ?** S0 n'est pas là « pour faire joli » : si la règle du mardi suffisait à supprimer les forfaits, ce serait la meilleure solution (gratuite, immédiate).

## 2. Grille TELOS

| Critère | S0 | S1 | S2 |
|---|---|---|---|
| **T**echnique | **3** — rien à installer | **2** — application à paramétrer ; import des familles par CSV possible (vérifié dans la documentation de l'éditeur, consultée le 12/10) | **1** — hébergement, notifications, maintenance : personne au club ne sait le faire, et l'équipe étudiante part en juin |
| **É**conomique | **3** — 0 € | **3** — offre gratuite pour les associations, 0 € ; option payante à 79 €/an non nécessaire (tarifs consultés le 12/10) | **1** — ≈ 60 €/an d'hébergement + nom de domaine, et surtout aucune maintenance financée |
| **L**égal | **1** — les numéros de tous les parents restent visibles de tous ; données de santé sur les téléphones | **2** — données hébergées dans l'UE selon l'éditeur ; comptes parents pour les moins de 15 ans ; contrat de sous-traitance à signer | **2** — à construire entièrement (information, droits, sécurité) |
| **O**pérationnel | **2** — dépend de la discipline de 12 entraîneurs | **2** — une application de plus pour les parents ; réponse par SMS possible pour les familles sans smartphone | **2** — même problème d'adoption que S1 |
| Calendaire (***S**chedule*) | **3** — applicable la semaine prochaine | **3** — pilote possible en novembre | **0** — impossible avant la fin de la phase aller |
| **Total** | 12 / 15 | **12 / 15** | 6 / 15 — **éliminé** (un 0) |

## 3. Coût total sur 3 ans

| Poste | S0 | S1 | S2 | Source / hypothèse |
|---|---|---|---|---|
| Acquisition / développement | 0 | 0 | 0 (étudiants) | — |
| Abonnements, hébergement, domaine | 0 | 0 | 180 € | 60 €/an, hébergeur mutualisé |
| Formation | 2 h | 6 h (réunion de lancement + tutoriel) | 6 h | estimation |
| Maintenance (heures bénévoles) | 0 | 10 h/an (Nadège : comptes, saisons) | **non assurée** | entretien Nadège |
| **Total 3 ans** | 0 € + 2 h | 0 € + 36 h | 180 € + ∞ | |

## 4. Risques majeurs par scénario (→ P2, S3)

- S0 : les entraîneurs n'appliquent pas la règle ; la fuite de numéros continue.
- S1 : les parents n'installent pas l'application ; l'éditeur change son offre gratuite.
- S2 : plus personne pour corriger un bug après juin.

## 5. Recommandation

> **Décision proposée : GO sur S1, en pilote sur 3 équipes (U11, U13, U15), avec S0 appliqué immédiatement à toutes les équipes.**
> Parce que (1) S1 est la seule solution qui couvre les 3 récits Must, (2) elle est gratuite, et (3) elle corrige la visibilité des numéros (L = 2 au lieu de 1). S0 à égalité de points mais ne règle ni la vue d'ensemble ni la confidentialité ; il sert de filet de sécurité.
> Conditions : 90 % des familles pilotes inscrites en 3 semaines (KPI-04) ; sinon, retour à S0 seul.

## 6. Décision du client au jalon J2

GO accepté par le bureau le 20/11, avec une réserve du président : « Je voulais une appli à notre nom. » Réponse apportée : le logo et les couleurs du club peuvent être ajoutés dans l'application choisie.

---
**Critères de qualité** — [x] 3 scénarios dont un sans développement · [x] chaque note justifiée et sourcée · [x] coûts sur 3 ans, temps humain compris · [x] recommandation cohérente avec la grille
**Usage de l'IA** : nous avons demandé une liste d'applications de gestion d'équipe ; sur 6 proposées, 2 n'existaient plus. Les 3 retenues ont été vérifiées sur leur site (annexe, dates de consultation).
