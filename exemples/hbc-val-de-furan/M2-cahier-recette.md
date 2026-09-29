# M2 — Cahier de recette · *exemple rédigé*

> **Mesurer** · rédigé en Phase 4 (**J3**), exécuté en Phase 5 (**J4**)

## 1. Stratégie

- Exécute la recette : **Sébastien** (coach U13) et **3 parents volontaires**, pas l'équipe projet.
- Environnement : l'application A configurée, équipe U13 importée ; un match fictif « Match de recette » créé le 01/12.

## 2. Cas de test

| ID | Récit / ENF | Préconditions | Étapes | Résultat attendu | Obtenu | OK / KO | Anomalie |
|---|---|---|---|---|---|---|---|
| T-01 | US-01 | coach connecté | créer un match avec lieu, heure, adresse, départ du parking ; chronométrer | envoyé en moins de 5 min | 3 min 40 | OK | |
| T-02 | US-02 | parent 1 invité | ouvrir la notification, répondre « présent » + 3 places | réponse enregistrée, aucun texte saisi | conforme, 20 s | OK | |
| T-03 | US-03 | 14 convoqués, 3 réponses | coach ouvre le match | 11 « sans réponse » en tête, 3 places affichées | liste triée par nom, pas par statut | **KO** | #21 : tri manuel possible, réglage trouvé → OK au 2e passage |
| T-04 | US-04 | parent 2 sans réponse | attendre mardi 21 h | rappel reçu | reçu 21 h 02 | OK | |
| T-05 | US-05 | match à l'extérieur | parent 3 ouvre le match | mention « extérieur » + adresse cliquable | conforme | OK | |
| T-S1 | ENF-03 | parent 1 connecté | chercher le téléphone d'une autre famille | **aucune coordonnée visible** | seuls les prénoms visibles | OK | |
| T-S2 | S3 droits | coach U13 connecté | ouvrir l'équipe U15 | accès refusé | refusé | OK | |
| T-S3 | S3 départ | compte coach test désactivé par Nadège | se reconnecter | accès refusé | refusé | OK | |
| T-R1 | ENF-05 | Nadège administratrice | exporter la liste U13 en CSV | fichier avec 14 joueurs et contacts | conforme | OK | |

> 💡 **Pourquoi ?** Chaque test a un **résultat attendu observable** écrit **avant** l'exécution. Le KO de T-03 n'est pas un échec de la recette : c'est exactement ce que la recette sert à trouver.

## 3. Procès-verbal de recette

- Tests exécutés : 9 · réussis : 9 (dont 1 après correction) · anomalies bloquantes : 0
- Décision : [ ] Recette prononcée · [x] **Prononcée avec réserves** : ENF-02 (familles sans smartphone) couverte par saisie manuelle du coach, à réévaluer en février · [ ] Refusée
- Date et signataire côté client : 01/12, Nadège Roche, secrétaire

---
**Critères de qualité** — [x] 100 % des Must couverts · [x] tests exécutables par quelqu'un qui n'a pas construit la solution · [x] tests de sécurité présents
