# S3 — Plan de sécurisation · *exemple rédigé*

> **Sécuriser** · Phase 4 (**J3**), mesures vérifiées en Phase 5 (**J4**)

## 1. Scénarios de menace

| ID | Source de risque | Scénario | Donnée(s) (S1) | DICP | Vraisemblance | Gravité |
|---|---|---|---|---|---|---|
| M-01 | Entraîneur ayant quitté le club | garde l'accès et voit les lieux et horaires des matchs des enfants | identité des joueurs | C | 3 | 3 |
| M-02 | Parent malveillant ou curieux | récupère les numéros des autres familles | coordonnées parents | C | 2 | 2 |
| M-03 | Compte administrateur piraté (mot de passe réutilisé) | export de toute la base, envoi de faux messages | toutes | C, I | 2 | 4 |
| M-04 | Éditeur de l'application | ferme ou change son offre ; données inaccessibles | toutes | D | 1 | 3 |
| M-05 | Habitude existante | certificats médicaux envoyés dans l'outil « parce que c'est pratique » | données de santé | C | 3 | 4 |

## 2. Mesures

| Mesure | Contre | Type | Coût / effort | Responsable | Vérifiée en recette ? |
|---|---|---|---|---|---|
| Comptes nominatifs ; **désactivation du compte d'un entraîneur le jour de son départ** (procédure d'une page) | M-01 | organisationnelle + technique | 5 min par départ | Nadège | T-S3 |
| Coordonnées des parents masquées entre familles (réglage) | M-02 | technique | nul | équipe projet | T-S1 |
| Double authentification obligatoire pour les 2 administrateurs | M-03 | technique | 10 min | Nadège | à vérifier au lancement |
| Export CSV mensuel stocké dans le drive du bureau | M-04 | organisationnelle | 5 min/mois | Nadège | T-R1 |
| Règle écrite « aucune pièce médicale dans l'outil ni sur WhatsApp » : elles se déposent sur la plateforme fédérale de licence | M-05 | organisationnelle | réunion coachs | président | — |
| Entraîneur limité à **son** équipe | M-01, M-02 | technique | nul | équipe projet | T-S2 |

> 💡 **Pourquoi ?** La moitié des mesures sont **organisationnelles** (une procédure, une règle). En sécurité, ce n'est pas un aveu de faiblesse : c'est souvent là que se trouvent les risques réels d'une petite organisation.

## 3. Comptes et droits

| Profil | Peut consulter | Peut modifier | Ne doit pas voir | Authentification |
|---|---|---|---|---|
| Administrateur (2) | tout | tout | — | mot de passe + double authentification |
| Entraîneur | son équipe | matchs et réponses de son équipe | autres équipes, coordonnées hors de son équipe | mot de passe |
| Parent | matchs de l'équipe de son enfant, prénoms des coéquipiers, places de voiture | sa réponse, ses places | coordonnées des autres familles | lien personnel ou mot de passe |

## 4. Sauvegarde et restauration

- Export CSV le 1er lundi du mois → drive du bureau (1 copie) + clé USB du trésorier (2e support) ; l'application elle-même est la 3e copie hors site.
- Test de restauration : import de l'export de décembre dans un compte de test, prévu le 06/01 par l'équipe projet.

## 5. Continuité et réversibilité

- Indisponibilité d'une semaine : retour à la règle S0 (message type du mardi + sondage) — le modèle de message est dans la fiche des coachs.
- Changement d'outil : export CSV complet (joueurs, équipes, contacts) ; aucune donnée propriétaire indispensable.

## 6. Risques résiduels acceptés

Un parent peut faire une capture d'écran de la liste des prénoms de l'équipe et la diffuser. Risque accepté par le président le 20/11 (les prénoms sont déjà connus des familles de l'équipe).

---
**Critères de qualité** — [x] chaque scénario a au moins une mesure · [x] au moins une mesure organisationnelle · [x] test de restauration planifié · [x] risques résiduels acceptés par le client
**Usage de l'IA** : nous avons demandé des menaces « pour une application de club sportif » ; la liste était générique (rançongiciel, DDoS). Nous avons gardé l'idée du compte administrateur piraté (M-03) et écrit les autres à partir de nos entretiens.
