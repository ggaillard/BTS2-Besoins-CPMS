# Étape 11 — Rechercher des solutions existantes

> Phase 3 Faisabilité · **Concevoir** · Alimente : [C5 Étude de faisabilité](../modeles/C5-etude-faisabilite.md) (annexe comparatif) · Jalon **J2** · ⏱ 1 h 30

## Pourquoi cette étape ?

Avant de proposer de développer quoi que ce soit, un professionnel vérifie ce qui existe déjà : un outil que l'organisation possède sans l'utiliser, un logiciel du marché, un service gratuit pour son secteur. C'est souvent moins cher, plus rapide et mieux maintenu qu'un développement sur mesure. C'est aussi ce qui rend votre scénario S2 (sur mesure) crédible : on ne peut dire « il faut développer » qu'après avoir montré que rien ne convient.

## Ce dont vous avez besoin

- [C4](../modeles/C4-fiche-besoins.md) : récits Must et exigences non fonctionnelles → ce seront vos **critères**.
- [S1](../modeles/S1-donnees-dicp.md) : les données sensibles → critères d'hébergement et de sécurité.
- Les indices laissés dans vos entretiens : « notre logiciel a peut-être une option », « le syndicat propose un module »… → **à vérifier en priorité**.

## Comment faire, pas à pas

1. **Écrivez vos critères avant de chercher** (sinon vous choisirez le plus joli) :
   - **éliminatoires** : couvre les Must, budget maximum, contrainte légale (hébergement de données de santé, argent public…), réversibilité ;
   - **de comparaison** : Should et Could, facilité, support en français, etc.
2. **Cherchez dans trois directions** :

   | Direction | Où chercher | Exemples de requêtes |
   |---|---|---|
   | **Ce que l'organisation a déjà** | entretiens, logiciels cités dans le README du cas, partenaires (fédération, syndicat, réseau) | « [nom du logiciel] + module réservation en ligne », documentation de l'éditeur |
   | **Les outils du secteur** | sites des fédérations et réseaux professionnels, comparateurs, retours d'expérience d'organisations similaires | « logiciel gestion bénévoles association », « prise de rendez-vous kiné hébergement données de santé » |
   | **Les outils génériques** | formulaires en ligne, agendas partagés, tableurs collaboratifs, messageries | « formulaire en ligne gratuit association RGPD » |

3. **Retenez 2 à 4 candidats** et, pour chacun, **allez sur son site** : page tarifs, page confidentialité / hébergement, documentation (import, export). **Notez l'adresse et la date de consultation** : les prix changent.
4. **Remplissez une grille** (`livrables/annexes/comparatif-solutions.md`) : une colonne par produit, une ligne par critère. Éliminez ceux qui échouent à un critère éliminatoire, en disant lequel.
5. **Vérifiez ce que l'IA vous dit** : si vous demandez « quels logiciels pour… », une partie des réponses peut être inventée ou périmée. Un produit n'entre dans le comparatif que si vous avez **ouvert son site**.
6. **Si vous posez une question à un éditeur** (chat, formulaire de contact), restez factuels et ne donnez aucune donnée personnelle du cas.

## Exemple

[Comparatif du club de handball](../exemples/hbc-val-de-furan/annexes/comparatif-applications.md) : 5 critères éliminatoires fixés avant, 3 applications, 1 retenue, 1 éliminée avec la raison.

## Pièges à éviter

- Ne chercher que des « applis » : un agenda partagé bien réglé ou une règle d'organisation peuvent suffire (scénario S0).
- Croire la page d'accueil : « conforme RGPD » ne suffit pas ; cherchez **où** sont hébergées les données et s'il existe un contrat de sous-traitance.
- Oublier le coût **humain** (paramétrage, administration, formation).

## J'ai fini quand…

- [ ] les critères éliminatoires sont écrits avant la recherche ;
- [ ] 2 à 4 solutions sont comparées, chacune avec adresse et date de consultation ;
- [ ] les pistes évoquées en entretien (« on a peut-être déjà… ») sont vérifiées.

---
[← Étape 10](E06-donnees-et-dicp.md#étape-10--cotation-dicp-2) · [Parcours](../METHODE.md) · [Étape 12 — Étude de faisabilité →](E12-faisabilite-telos-couts.md)
