# Arbres de décision

> Un arbre de décision se lit **de haut en bas** : on répond à la question du losange, on suit la flèche « oui » ou « non », jusqu'à une case qui dit quoi faire.
> Ils ne remplacent pas votre réflexion : ils vous évitent d'oublier une question. **Notez dans l'artefact la réponse à chaque question**, c'est ce qui justifie votre choix.

| Arbre | Quand l'utiliser | Fiche |
|---|---|---|
| [Où en sommes-nous ? Quelle étape maintenant ?](#orientation) | Se repérer | [METHODE](../METHODE.md) |
| [Classer une phrase du besoin exprimé](#classer_phrase) | Phase 1 — Recueillir | [E01-lire-le-besoin-exprime](E01-lire-le-besoin-exprime.md) |
| [Ma question d'entretien est-elle bonne ?](#question_entretien) | Phase 1 — Recueillir | [E03-preparer-entretien](E03-preparer-entretien.md) |
| [Quel niveau de certitude pour un constat (C3 §2) ?](#certitude) | Phase 1 — Recueillir | [E04-mener-entretien-compte-rendu](E04-mener-entretien-compte-rendu.md) |
| [Cette donnée est-elle personnelle ? sensible ?](#donnee) | Phase 1 — Recueillir | [E06-donnees-et-dicp](E06-donnees-et-dicp.md) |
| [Must, Should, Could ou Won't ?](#moscow) | Phase 2 — Analyser | [E08-recits-gherkin-moscow](E08-recits-gherkin-moscow.md) |
| [Mon indicateur est-il SMART ?](#smart) | Phase 2 — Analyser | [E09-indicateurs](E09-indicateurs.md) |
| [Une IA est-elle la bonne réponse ?](#ia) | Phase 3 — Faisabilité | [E11-rechercher-solutions](E11-rechercher-solutions.md) |
| [Quel scénario recommander ? GO ou NO-GO ?](#scenario) | Phase 3 — Faisabilité | [E12-faisabilite-telos-couts](E12-faisabilite-telos-couts.md) |
| [Quelle base légale pour le traitement ?](#base_legale) | Phase 3 — Faisabilité | [E13-rgpd](E13-rgpd.md) |
| [Faut-il une analyse d'impact (AIPD) ?](#aipd) | Phase 3 — Faisabilité | [E13-rgpd](E13-rgpd.md) |
| [Risque projet (P2) ou menace de sécurité (S3) ?](#p2_s3) | Phase 3 — Faisabilité | [E14-risques-projet](E14-risques-projet.md) |
| [Quelle stratégie de bascule ?](#bascule) | Phase 4 — Préparer la mise en place | [E18-deploiement](E18-deploiement.md) |

---

## Se repérer

<a id="orientation"></a>

### Où en sommes-nous ? Quelle étape maintenant ?

```mermaid
flowchart TD
    Q1{"Le dépôt d'équipe existe-t-il ?"} -- "non" --> A0["Étape 0"]
    Q1 -- "oui" --> Q2{"Avons-nous au moins 3 comptes rendus C3 validés ?"}
    Q2 -- "non" --> Q3{"Nos guides d'entretien C2 sont-ils prêts ?"}
    Q3 -- "non" --> A1["Étapes 1 à 3"]
    Q3 -- "oui" --> A4["Étape 4 : demander un entretien"]
    Q2 -- "oui" --> Q4{"M1 §1 et S1 §1 sont-ils remplis ?"}
    Q4 -- "non" --> A5["Étapes 5 et 6, puis jalon J1"]
    Q4 -- "oui" --> Q5{"Le client a-t-il pris sa décision au J2 ?"}
    Q5 -- "non" --> Q6{"C4 est-il complet : récits, Gherkin, MoSCoW, ENF ?"}
    Q6 -- "non" --> A7["Étapes 7 à 10"]
    Q6 -- "oui" --> A11["Étapes 11 à 15, puis jalon J2"]
    Q5 -- "oui" --> Q7{"C6, P1, P4, M2 et S3 sont-ils commités ?"}
    Q7 -- "non" --> A16["Étapes 16 à 20, puis jalon J3"]
    Q7 -- "oui" --> A21["Étapes 21 et 22, puis jalon J4"]
```

À relire au début de chaque séance.

*Fiche associée : [METHODE](../METHODE.md).*


---

## Phase 1 — Recueillir

<a id="classer_phrase"></a>

### Classer une phrase du besoin exprimé

```mermaid
flowchart TD
    A{"La phrase nomme-t-elle un outil, une technologie ou une fonctionnalité ?"} -- "oui" --> SOL["🟦 SOLUTION IMAGINÉE<br/>→ question d'entretien :<br/>« Qu'est-ce qui vous fait dire ça ? »"]
    A -- "non" --> B{"Décrit-elle une limite : budget, date, règle, personne, matériel ?"}
    B -- "oui" --> CON["🟩 CONTRAINTE<br/>→ C4 §3 périmètre, C5 grille TELOS"]
    B -- "non" --> C{"Décrit-elle un fait qui gêne quelqu'un ?"}
    C -- "oui" --> PB["🟥 PROBLÈME<br/>→ à chiffrer (M1) et à vérifier en entretien"]
    C -- "non" --> CTX["Contexte<br/>→ utile pour C1"]
```

*Fiche associée : [E01-lire-le-besoin-exprime](E01-lire-le-besoin-exprime.md).*

<a id="question_entretien"></a>

### Ma question d'entretien est-elle bonne ?

```mermaid
flowchart TD
    A{"Contient-elle une solution ou une technologie ?"} -- "oui" --> R1["Reformuler vers le problème :<br/>« Qu'est-ce qui vous fait perdre du temps ? »"]
    A -- "non" --> B{"Peut-on y répondre par oui ou non ?"}
    B -- "oui" --> C{"Est-ce une relance pour préciser un point déjà évoqué ?"}
    C -- "oui" --> OK1["✔ À garder"]
    C -- "non" --> R2["Transformer en « Racontez-moi… »<br/>ou « Comment… »"]
    B -- "non" --> D{"Contient-elle du jargon : base de données, RGPD, cahier des charges… ?"}
    D -- "oui" --> R3["Traduire en mots de tous les jours"]
    D -- "non" --> OK2["✔ Bonne question"]
```

*Fiche associée : [E03-preparer-entretien](E03-preparer-entretien.md).*

<a id="certitude"></a>

### Quel niveau de certitude pour un constat (C3 §2) ?

```mermaid
flowchart TD
    A{"Est-ce dit clairement dans un verbatim ?"} -- "non" --> V1["À VÉRIFIER<br/>c'est une déduction de l'équipe"]
    A -- "oui" --> B{"Une autre source le contredit-elle ?"}
    B -- "oui" --> V2["À VÉRIFIER<br/>→ question en C3 §5"]
    B -- "non" --> C{"Une deuxième source le confirme-t-elle : autre entretien, document, fichier ?"}
    C -- "oui" --> S["SÛR"]
    C -- "non" --> P["PROBABLE<br/>→ chercher une deuxième source"]
```

*Fiche associée : [E04-mener-entretien-compte-rendu](E04-mener-entretien-compte-rendu.md).*

<a id="donnee"></a>

### Cette donnée est-elle personnelle ? sensible ?

```mermaid
flowchart TD
    A{"Permet-elle d'identifier une personne, directement ou en la croisant avec autre chose ?"} -- "non" --> N["Donnée NON personnelle<br/>→ cotez quand même DICP si le service en dépend"]
    A -- "oui" --> B{"Révèle-t-elle la santé, l'origine, des opinions, une religion, l'orientation sexuelle, un syndicat, la biométrie, la génétique ?"}
    B -- "oui" --> S["Donnée SENSIBLE (article 9)<br/>interdite sauf exception<br/>→ la retirer si possible, sinon justifier l'exception<br/>→ AIPD probable"]
    B -- "non" --> C{"Concerne-t-elle un mineur, ou s'agit-il d'un n° de sécurité sociale, bancaire, d'un mot de passe ?"}
    C -- "oui" --> H["Donnée personnelle à VIGILANCE RENFORCÉE<br/>→ confidentialité ≥ 3 dans S1"]
    C -- "non" --> P["Donnée personnelle<br/>→ S1 et S2 normalement"]
```

*Fiche associée : [E06-donnees-et-dicp](E06-donnees-et-dicp.md).*


---

## Phase 2 — Analyser

<a id="moscow"></a>

### Must, Should, Could ou Won't ?

```mermaid
flowchart TD
    A{"Sans ce récit, le client a-t-il encore intérêt à changer ?"} -- "non" --> M["MUST"]
    A -- "oui" --> B{"Répond-il à un problème chiffré en M1, ou cité par plusieurs interlocuteurs ?"}
    B -- "oui" --> SH["SHOULD"]
    B -- "non" --> C{"Tient-il dans le budget et le délai ?"}
    C -- "oui" --> CO["COULD"]
    C -- "non" --> W["WON'T (this time)<br/>→ écrire pourquoi"]
    M --> V{"Plus de 40 % de Must au total ?"}
    V -- "oui" --> A
    V -- "non" --> OK["✔ Priorisation crédible"]
```

Si vous avez trop de Must, repassez chaque Must dans l'arbre en étant plus sévères.

*Fiche associée : [E08-recits-gherkin-moscow](E08-recits-gherkin-moscow.md).*

<a id="smart"></a>

### Mon indicateur est-il SMART ?

```mermaid
flowchart TD
    S{"Sait-on exactement ce qu'on compte ?"} -- "non" --> R1["Préciser l'objet compté"]
    S -- "oui" --> M{"Existe-t-il une source pour le mesurer ?"}
    M -- "non" --> R2["Trouver une source ou changer d'indicateur"]
    M -- "oui" --> D{"A-t-il une valeur de départ dans M1 §1 ?"}
    D -- "non" --> R3["Mesurer l'avant d'abord (étape 5)"]
    D -- "oui" --> A{"La cible est-elle crédible avec les moyens du client ?"}
    A -- "non" --> R4["Revoir la cible"]
    A -- "oui" --> P{"Est-il relié au « afin de » du besoin ou à un récit ?"}
    P -- "non" --> R5["L'abandonner"]
    P -- "oui" --> T{"A-t-il une échéance ?"}
    T -- "non" --> R6["Fixer une date"]
    T -- "oui" --> OK["✔ Indicateur SMART"]
```

*Fiche associée : [E09-indicateurs](E09-indicateurs.md).*


---

## Phase 3 — Faisabilité

<a id="ia"></a>

### Une IA est-elle la bonne réponse ?

```mermaid
flowchart TD
    A{"Les bonnes réponses sont-elles déjà écrites quelque part, à jour : FAQ, base, documents ?"} -- "non" --> A0["D'abord écrire et mettre à jour les sources.<br/>Une IA sans source fiable invente."]
    A -- "oui" --> B{"Une réponse fausse peut-elle nuire : santé, sécurité, argent, droits ?"}
    B -- "oui" --> C{"Peut-on exclure ces sujets et garantir le passage à un humain ?"}
    C -- "non" --> NO1["Pas d'IA en réponse directe au public.<br/>Éventuellement une aide pour le personnel."]
    C -- "oui" --> D
    B -- "non" --> D{"Des données personnelles ou sensibles transitent-elles ?"}
    D -- "oui" --> E{"L'hébergement est-il conforme : UE, pas de réutilisation pour l'entraînement, HDS si santé ?"}
    E -- "non" --> NO2["Écarter ce fournisseur"]
    E -- "oui" --> F
    D -- "non" --> F{"Peut-on mesurer la qualité avant la mise en service : jeu de questions, seuil fixé à l'avance ?"}
    F -- "non" --> NO3["Construire d'abord le jeu d'évaluation"]
    F -- "oui" --> OK["IA envisageable :<br/>un scénario à comparer comme les autres (TELOS)<br/>+ informer l'usager qu'il parle à une IA (AI Act)"]
```

*Fiche associée : [E11-rechercher-solutions](E11-rechercher-solutions.md).*

<a id="scenario"></a>

### Quel scénario recommander ? GO ou NO-GO ?

```mermaid
flowchart TD
    A{"S0, sans développement, couvre-t-il tous les Must ?"} -- "oui" --> B{"S0 a-t-il un 0 dans la grille TELOS ?"}
    B -- "non" --> R0["Recommander S0<br/>la solution la plus simple qui suffit"]
    B -- "oui" --> C
    A -- "non" --> C{"Une solution du marché S1 couvre-t-elle les Must, sans aucun 0 ?"}
    C -- "oui" --> R1["Recommander S1<br/>+ S0 en filet si utile"]
    C -- "non" --> D{"Le sur-mesure S2 a-t-il une maintenance assurée après votre départ, et aucun 0 ?"}
    D -- "oui" --> R2["Recommander S2<br/>avec ses conditions"]
    D -- "non" --> E{"Peut-on réduire le périmètre avec le client : Should → Could ?"}
    E -- "oui" --> F["Réduire le périmètre, puis reprendre l'arbre"]
    F --> A
    E -- "non" --> NG["NO-GO argumenté<br/>+ alternative : réorganisation, report, autre financement"]
```

Si plusieurs scénarios passent, départagez-les par : nombre de Must couverts, total TELOS, coût sur 3 ans, risques (P2).

*Fiche associée : [E12-faisabilite-telos-couts](E12-faisabilite-telos-couts.md).*

<a id="base_legale"></a>

### Quelle base légale pour le traitement ?

```mermaid
flowchart TD
    A{"Un texte (loi, règlement) oblige-t-il à traiter ces données ?"} -- "oui" --> OL["OBLIGATION LÉGALE"]
    A -- "non" --> B{"Est-ce un organisme public qui exerce sa mission ?"}
    B -- "oui" --> MIP["MISSION D'INTÉRÊT PUBLIC"]
    B -- "non" --> C{"Est-ce nécessaire pour exécuter un contrat avec la personne, ou le préparer à sa demande ?"}
    C -- "oui" --> CT["CONTRAT<br/>ou mesures précontractuelles"]
    C -- "non" --> D{"L'organisation a-t-elle un intérêt réel, que la personne peut raisonnablement attendre, sans atteinte disproportionnée à ses droits ?"}
    D -- "oui" --> IL["INTÉRÊT LÉGITIME<br/>→ écrire la mise en balance"]
    D -- "non" --> CS["CONSENTEMENT<br/>libre, éclairé, retirable<br/>→ prévoir comment le recueillir et le retirer"]
```

La sixième base, la sauvegarde des intérêts vitaux (urgence médicale…), est très rare dans nos cas.

*Fiche associée : [E13-rgpd](E13-rgpd.md).*

<a id="aipd"></a>

### Faut-il une analyse d'impact (AIPD) ?

```mermaid
flowchart TD
    A{"Le traitement figure-t-il dans la liste CNIL des traitements soumis à AIPD ?"} -- "oui" --> Y1["AIPD REQUISE"]
    A -- "non" --> B["Compter les critères européens remplis (sur 9) :<br/>données sensibles · personnes vulnérables · grande échelle ·<br/>croisement de données · usage innovant · surveillance systématique ·<br/>évaluation ou notation · décision automatique · exclusion d'un droit"]
    B --> C{"2 critères ou plus ?"}
    C -- "oui" --> Y2["AIPD EN PRINCIPE REQUISE"]
    C -- "non" --> N["AIPD NON REQUISE<br/>→ le justifier dans S2 §4<br/>→ revoir si le traitement change"]
```

*Fiche associée : [E13-rgpd](E13-rgpd.md).*

<a id="p2_s3"></a>

### Risque projet (P2) ou menace de sécurité (S3) ?

```mermaid
flowchart TD
    Z{"Est-ce un événement futur et incertain ?"} -- "non" --> K["Ce n'est pas un risque :<br/>c'est un constat (C3) ou une contrainte (C4)"]
    Z -- "oui" --> A{"Touche-t-il des données, des accès, une panne, une personne malveillante ?"}
    A -- "oui" --> S3["MENACE DE SÉCURITÉ → S3"]
    A -- "non" --> B{"Touche-t-il le délai, le budget, l'adoption, les compétences, une décision, un fournisseur ?"}
    B -- "oui" --> P2["RISQUE PROJET → P2"]
    B -- "non" --> K2["Reformuler en « cause → événement → conséquence »<br/>puis reprendre l'arbre"]
```

Un même problème peut avoir les deux faces (ex. « le seul administrateur part ») : une ligne dans P2 et une dans S3, avec un renvoi.

*Fiche associée : [E14-risques-projet](E14-risques-projet.md).*


---

## Phase 4 — Préparer la mise en place

<a id="bascule"></a>

### Quelle stratégie de bascule ?

```mermaid
flowchart TD
    A{"Peut-on garder l'ancien fonctionnement quelques semaines ?"} -- "non" --> B{"Peu d'utilisateurs et faible risque ?"}
    B -- "oui" --> BB1["BIG BANG<br/>sauvegarde avant, répétition"]
    B -- "non" --> BB2["BIG BANG très préparé<br/>répétition générale, support renforcé le jour J"]
    A -- "oui" --> C{"Beaucoup d'utilisateurs, ou adoption incertaine ?"}
    C -- "oui" --> PI["PILOTE sur un petit groupe<br/>puis généralisation"]
    C -- "non" --> D{"Perdre une information pendant la transition serait-il grave ?"}
    D -- "oui" --> DF["DOUBLE FONCTIONNEMENT<br/>avec une date de fin"]
    D -- "non" --> BB3["BIG BANG"]
```

Dans tous les cas : un critère de retour arrière chiffré (P4 §1).

*Fiche associée : [E18-deploiement](E18-deploiement.md).*


---
[Parcours](../METHODE.md) · [Diagrammes UML](schemas-uml.md) · [Aide-mémoire UML](aide-memoire-uml-mermaid.md)
