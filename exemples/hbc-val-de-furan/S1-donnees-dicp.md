# S1 — Données et besoins DICP · *exemple rédigé*

> **Sécuriser** · §1 en Phase 1 (**J1**), §2 en Phase 2 (**J2**)

## 1. Inventaire des données

| Donnée / ensemble de données | Concerne qui | Personnelle ? | Sensible au sens du RGPD ? | Où elle est aujourd'hui | Qui y accède aujourd'hui | Volume |
|---|---|---|---|---|---|---|
| Prénom, nom, équipe des joueurs | joueurs mineurs | oui | non (mais **mineurs**) | logiciel fédéral de licences + groupes WhatsApp | bureau, entraîneurs, tous les parents du groupe | 112 |
| Téléphone et e-mail des parents | parents | oui | non | logiciel de licences, téléphones personnels des entraîneurs | bureau, entraîneurs, **tous les membres du groupe** | ≈ 170 |
| Réponses aux convocations (présent / absent) | joueurs | oui | non | messages WhatsApp | groupe | ≈ 20 / semaine / équipe |
| Disponibilités de conducteurs | parents | oui | non | messages WhatsApp | groupe | — |
| Questionnaires de santé, certificats médicaux | joueurs mineurs | oui | **oui (santé)** | photos sur les téléphones des entraîneurs | entraîneur, parfois le groupe | ≈ 30 / saison |

## 2. Besoins de sécurité (DICP)

| Donnée | D | I | C | P | Justification |
|---|---|---|---|---|---|
| Identité et équipe des joueurs | 2 | 3 | 3 | 1 | **C=3** : ce sont des mineurs ; leur nom associé à un lieu et un horaire de match permet de les retrouver. **I=3** : une erreur d'équipe = enfant non convoqué. |
| Coordonnées des parents | 2 | 2 | 2 | 1 | C=2 : visibles de tout le groupe aujourd'hui, risque de démarchage ou de harcèlement modéré. |
| Réponses aux convocations | **3** | 3 | 1 | 2 | **D=3** : si l'information n'est pas disponible le mercredi soir, l'entraîneur ne peut pas organiser le match (→ forfait). P=2 : utile en cas de contestation d'un forfait. |
| Données de santé | 1 | 3 | **4** | 2 | **C=4** : donnée de santé d'un mineur. Elle n'a **rien à faire** dans l'outil de convocation → hors périmètre, mesure dans S3. |

> 💡 **Pourquoi ?** Chaque note est justifiée par une **conséquence concrète** (« l'entraîneur ne peut pas organiser le match »), pas par une formule vague (« c'est important »). La donnée de santé est notée pour décider de **l'exclure**, pas pour la gérer.

## 3. Ce que révèle l'existant

- Les numéros de tous les parents sont visibles par tous les membres des groupes, y compris des parents d'anciens joueurs jamais retirés.
- Des données de santé de mineurs sont stockées sur des téléphones personnels, sans règle.
- Un entraîneur qui quitte le club garde tout l'historique.

---
**Critères de qualité** — [x] toutes les données citées dans les C3 sont inventoriées · [x] chaque note DICP est justifiée par une conséquence · [x] les failles de l'existant sont relevées sans jugement
**Usage de l'IA** : aucun.
