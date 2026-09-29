# Étape 0 — Installer l'équipe et le dépôt

> Phase 0 · Démarrer · **Piloter** · Artefact : [P3 Journal de bord](../modeles/P3-journal-de-bord.md) · Jalon **J0** · ⏱ 1 h

## Pourquoi cette étape ?

Pendant 7 séances, vous allez produire une quinzaine de documents à plusieurs. Sans rôles clairs ni endroit unique où tout est rangé, vous perdrez du temps à vous demander « qui fait quoi » et « où est la dernière version ». Le dépôt GitHub **est** votre dossier de projet : l'enseignant évalue ce qui y est commité.

## Ce dont vous avez besoin

- Un compte GitHub par membre.
- Le dépôt modèle [`BTS2-Besoins-CPMS`](../README.md).

## Comment faire, pas à pas

1. **Formez l'équipe** (3 ou 4) et répartissez les rôles. Ils **tournent à chaque jalon** pour que chacun touche à tout.

   | Rôle | Ce qu'il fait |
   |---|---|
   | Animateur·rice | Ouvre la séance (« où en est-on ? »), distribue le travail, surveille l'heure |
   | Secrétaire | Tient le journal de bord (P3), prend les notes en entretien |
   | Responsable qualité | Vérifie les critères de qualité avant chaque commit d'artefact, lance `outils/verifier.py` |
   | Responsable sécurité | Relit chaque document avec la question « quelles données, quel risque ? » (S1, S2, S3) |

2. **Créez le dépôt de l'équipe** : sur la page du dépôt modèle, bouton vert **Use this template → Create a new repository**. Propriétaire : l'un de vous ; nom : `cpms-<cas>-<equipe>` ; visibilité : **Private**.
3. **Invitez** les coéquipiers et l'enseignant : *Settings → Collaborators → Add people*.
4. **Créez les jalons** : *Issues → Milestones → New milestone* : `J1 Besoin validé`, `J2 Go-No-go`, `J3 Plan validé`, `J4 Bilan`, avec les dates données par l'enseignant.
5. **Créez les étiquettes** : *Issues → Labels → New label* : `concevoir`, `piloter`, `mesurer`, `securiser`, `recit`, `risque`.
6. **Créez le tableau** : onglet *Projects → Link a project → New project → Board*. Colonnes : *À faire, En cours, À relire, Fait*.
7. **Ouvrez un ticket par artefact de la phase 1** (C1, C2, C3, M1, S1) avec le bon jalon et la bonne étiquette, et assignez-le à quelqu'un.
8. **Ouvrez le journal de bord** : copiez [`modeles/P3-journal-de-bord.md`](../modeles/P3-journal-de-bord.md) dans `livrables/`, remplissez le tableau de l'équipe et la première entrée.
9. **Clonez** le dépôt (ou ouvrez-le dans un Codespace) pour pouvoir lancer `python3 outils/verifier.py`.

### Travailler avec Git au quotidien

```bash
git pull                          # toujours commencer par récupérer le travail des autres
cp modeles/C1-parties-prenantes.md livrables/
# … éditer livrables/C1-parties-prenantes.md …
git add livrables/C1-parties-prenantes.md
git commit -m "C1 : parties prenantes, v1 (closes #2)"
git push
```

Le message `closes #2` ferme automatiquement le ticket n° 2. Un commit par artefact (au moins), avec un message qui dit **ce qui a changé**.

## Exemple

[Journal de bord du club de handball](../exemples/hbc-val-de-furan/P3-journal-de-bord.md) — voir l'entrée « Séance 1 ».

## Pièges à éviter

- Travailler chacun sur un document partagé hors du dépôt, et tout copier la veille du jalon : l'historique ne montre alors pas qui a fait quoi.
- Garder les mêmes rôles tout le projet : à l'oral, chacun doit maîtriser l'ensemble.

## J'ai fini quand…

- [ ] le dépôt d'équipe existe, privé, avec l'enseignant invité ;
- [ ] les 4 jalons, les 6 étiquettes et le tableau existent ;
- [ ] les tickets de la phase 1 sont ouverts et assignés ;
- [ ] `livrables/P3-journal-de-bord.md` est commité avec l'entrée de la séance 1.

---
[Parcours](../METHODE.md) · [Étape suivante : 1 — Lire le besoin exprimé →](E01-lire-le-besoin-exprime.md)
