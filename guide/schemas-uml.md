# La méthode en diagrammes UML

> Ces diagrammes décrivent **la méthode elle-même** : qui fait quoi, dans quel ordre, comment un document évolue, comment les artefacts sont reliés.
> Pour dessiner **vos propres** diagrammes (processus de votre organisation, cas d'utilisation, séquences), voir l'[aide-mémoire UML en Mermaid](aide-memoire-uml-mermaid.md).
> Pour les choix à faire en cours de route : les [arbres de décision](arbres-de-decision.md).

| Diagramme | Ce qu'il montre | Où il sert |
|---|---|---|
| Diagramme d'activité | la méthode complète, par acteur | [METHODE.md](../METHODE.md) |
| Diagramme de cas d'utilisation | qui fait quoi dans le module | [METHODE.md](../METHODE.md) |
| Diagramme de séquence | de l'entretien au compte rendu validé (étapes 3-4) | [étape 4](E04-mener-entretien-compte-rendu.md) |
| Diagramme de séquence | le passage d'un jalon avec oral (J2) | [étape 15](E15-presenter-go-no-go.md) |
| Diagramme de séquence | l'exécution de la recette (étape 19) | [étape 19](E19-recette.md) |
| Diagramme d'états-transitions | la vie d'un artefact | [étape 0](E00-installer-equipe-et-depot.md) |
| Diagramme d'états-transitions | d'une phrase du client à un test réussi | [étape 8](E08-recits-gherkin-moscow.md) |
| Diagramme d'états-transitions | la vie d'un risque (P2) | [étape 14](E14-risques-projet.md) |
| Diagramme de classes | comment les artefacts s'enchaînent (traçabilité) | [étape 7](E07-reformuler-le-besoin.md), [METHODE §4](../METHODE.md#4-carte-des-16-artefacts) |

---

## Le processus global

### Diagramme d'activité — la méthode complète, par acteur

```mermaid
flowchart TB
    subgraph EQ["🧑‍💻 Équipe"]
        direction TB
        d(("Début")) --> e0["0 · Installer l'équipe et le dépôt"]
        e0 --> e1["1-3 · Lire le besoin · C1 · C2"]
        e1 --> e4["4 · Mener l'entretien · rédiger C3"]
        e5["5-6 · Chiffrer M1 §1 · inventorier S1 §1"]
        e7["7-10 · C4 · M1 §2 · S1 §2"]
        e11["11-14 · Solutions · C5 · S2 · P2"]
        e15["15 · Présenter la recommandation"]
        e16["16-20 · C6 · P1 · P4 · M2 · S3"]
        e21["21-22 · Preuve de concept · M3 · clôture"]
        f(("Fin"))
    end
    subgraph CL["🧑‍🏫 Client (joué par l'enseignant)"]
        direction TB
        c1["Répond dans son rôle"]
        c2{"Compte rendu fidèle ?"}
        c3{"J1 · besoin validé ?"}
        c4{"J2 · décision"}
        c5{"J3 · plan validé ?"}
        c6["J4 · évalue le bilan"]
    end
    e4 --> c1 --> c2
    c2 -- "non : corrections" --> e4
    c2 -- "oui" --> e5
    e5 --> c3
    c3 -- "non : entretien complémentaire" --> e1
    c3 -- "oui" --> e7 --> e11 --> e15 --> c4
    c4 -- "Go" --> e16
    c4 -- "No-go : on prépare l'alternative" --> e16
    c4 -- "À retravailler" --> e11
    e16 --> c5
    c5 -- "non" --> e16
    c5 -- "oui" --> e21 --> c6 --> f
```

Chaque rectangle est une activité de l'équipe, chaque losange une décision du client. Les flèches qui remontent montrent qu'on **revient en arrière** quand le client n'est pas d'accord : c'est normal, c'est prévu.

*Utilisé à : [METHODE.md](../METHODE.md).*


---

## Les acteurs et leurs usages (diagramme de cas d'utilisation)

### Diagramme de cas d'utilisation — qui fait quoi dans le module

```mermaid
flowchart LR
    eq(("🧑‍💻 Équipe"))
    cl(("🧑‍🏫 Client<br/>(enseignant dans son rôle)"))
    ev(("🧑‍🏫 Enseignant<br/>évaluateur"))
    gh(("🗄️ GitHub"))
    subgraph MOD["Module « Du besoin exprimé à la mise en place »"]
        u1(["Préparer un entretien"])
        u2(["Mener un entretien"])
        u3(["Faire valider un compte rendu"])
        u4(["Chiffrer la situation de départ"])
        u5(["Comparer des scénarios"])
        u6(["Présenter la recommandation"])
        u7(["Décider Go / No-go"])
        u8(["Préparer la mise en place"])
        u9(["Exécuter la recette"])
        u10(["Vérifier la complétude d'un jalon"])
        u11(["Évaluer un jalon"])
        u12(["Tracer le travail : commit, ticket"])
    end
    eq --- u1
    eq --- u2
    eq --- u4
    eq --- u5
    eq --- u6
    eq --- u8
    eq --- u10
    cl --- u2
    cl --- u3
    cl --- u7
    cl --- u9
    ev --- u11
    u12 --- gh
    u2 -. "«include»" .-> u1
    u3 -. "«include»" .-> u12
    u6 -. "«include»" .-> u5
    u11 -. "«include»" .-> u10
```

Un bonhomme (cercle) est un **acteur** : une personne ou un système extérieur. Un ovale est un **cas d'utilisation** : un service rendu, formulé par un verbe. La flèche pointillée `«include»` signifie « contient toujours » : on ne mène pas d'entretien sans l'avoir préparé.

*Utilisé à : [METHODE.md](../METHODE.md). Pour dessiner les cas d'utilisation de votre organisation : [aide-mémoire §2 et §2 bis](aide-memoire-uml-mermaid.md#2-diagramme-de-cas-dutilisation).*

---

## Les interactions (diagrammes de séquence)

### Diagramme de séquence — de l'entretien au compte rendu validé (étapes 3-4)

```mermaid
sequenceDiagram
    autonumber
    participant Eq as Équipe
    participant GH as GitHub
    participant Cl as Client (enseignant)
    Eq->>GH: commit du guide d'entretien C2
    Eq->>Cl: demande un créneau
    Cl->>GH: vérifie que C2 est commité
    alt C2 absent
        Cl-->>Eq: créneau refusé
    else C2 présent
        Cl-->>Eq: créneau de 12 minutes
        loop pour chaque thème du guide
            Eq->>Cl: question ouverte puis relances
            Cl-->>Eq: réponse dans le rôle
        end
        Note over Eq: le preneur de notes écrit mot pour mot
        Eq->>GH: commit C3 et ticket « Validation C3 »
        Cl->>GH: commente le ticket (corrections)
        Eq->>GH: C3 corrigé, §6 rempli, ticket fermé
    end
```

Lisez de haut en bas : chaque flèche est un message, dans l'ordre (numéros). Le bloc `alt` montre deux cas possibles, le bloc `loop` une répétition.

*Utilisé à : [étape 4](E04-mener-entretien-compte-rendu.md).*

### Diagramme de séquence — le passage d'un jalon avec oral (J2)

```mermaid
sequenceDiagram
    autonumber
    participant Eq as Équipe
    participant V as verifier.py
    participant GH as GitHub
    participant Cl as Client (enseignant)
    Eq->>V: python3 outils/verifier.py --jalon J2
    V-->>Eq: liste des ✓ ◐ ✗
    opt il reste des ◐ ou des ✗
        Eq->>GH: compléter les artefacts, commit, push
    end
    Eq->>Cl: oral de 10 minutes
    Cl-->>Eq: objections
    Eq->>Cl: réponses appuyées sur des chiffres (M1) et la grille (C5)
    Cl-->>Eq: décision Go, No-go ou à retravailler
    Eq->>GH: C5 §6 (décision), P3 (journal), P2 (nouveaux risques)
```

Le bloc `opt` est facultatif : il n'a lieu que si la condition est vraie.

*Utilisé à : [étape 15](E15-presenter-go-no-go.md).*

### Diagramme de séquence — l'exécution de la recette (étape 19)

```mermaid
sequenceDiagram
    autonumber
    participant Eq as Équipe
    participant Ut as Utilisateur réel
    participant So as Solution (compte de test)
    participant GH as GitHub
    Eq->>So: prépare des données fictives
    Eq->>Ut: remet le cahier de recette M2
    loop pour chaque test
        Ut->>So: exécute les étapes
        So-->>Ut: résultat observé
        Ut->>Ut: compare au résultat attendu
        alt KO
            Ut->>GH: ouvre un ticket d'anomalie
            Eq->>So: corrige ou reparamètre
            Ut->>So: rejoue le test
        end
    end
    Ut->>Eq: signe le procès-verbal (avec ou sans réserves)
```

C'est l'**utilisateur réel** qui exécute, pas l'équipe : c'est tout l'intérêt de la recette.

*Utilisé à : [étape 19](E19-recette.md).*


---

## Les cycles de vie (diagrammes d'états-transitions)

### Diagramme d'états-transitions — la vie d'un artefact

```mermaid
stateDiagram-v2
    state "Copié depuis le modèle" as Copie
    state "En rédaction" as Redac
    state "À relire" as Relire
    state "Commité" as Commit
    state "Soumis au client" as Soumis
    state "Validé" as Valide
    [*] --> Copie : cp modeles/… livrables/
    Copie --> Redac
    Redac --> Relire : plus aucun marqueur ⟪…⟫
    Relire --> Redac : critère de qualité non rempli
    Relire --> Commit : relu par le responsable qualité
    Commit --> Soumis : C3, C4 §2, C5 (soumis au client)
    Commit --> Valide : autres artefacts, au jalon
    Soumis --> Redac : corrections demandées
    Soumis --> Valide : accord du client
    Valide --> Redac : nouvelle information
    Valide --> [*] : jalon passé
```

Un rectangle arrondi est un **état**, une flèche une **transition**, le texte après « : » l'événement qui la déclenche. Un artefact peut revenir en rédaction à tout moment si une information nouvelle arrive.

*Utilisé à : [étape 0](E00-installer-equipe-et-depot.md).*

### Diagramme d'états-transitions — d'une phrase du client à un test réussi

```mermaid
stateDiagram-v2
    state "Demande brute (verbatim C3)" as V
    state "Récit rédigé (C4)" as R
    state "Priorisé (MoSCoW)" as P
    state "Critère Gherkin écrit" as G
    state "Couvert par le scénario retenu (C5)" as S
    state "Test écrit (M2)" as T
    state "Test réussi" as OK
    state "Écarté (Won't)" as W
    [*] --> V
    V --> R : reformulation
    R --> P
    P --> W : Won't
    P --> G : Must ou Should
    G --> S
    S --> T
    T --> OK : exécuté par le client
    T --> G : KO, critère ambigu
    OK --> [*]
    W --> [*]
```

Ce diagramme montre la **traçabilité** : chaque test de recette doit pouvoir remonter jusqu'à une phrase prononcée par le client.

*Utilisé à : [étape 8](E08-recits-gherkin-moscow.md).*

### Diagramme d'états-transitions — la vie d'un risque (P2)

```mermaid
stateDiagram-v2
    state "Identifié" as I
    state "Coté (probabilité × impact)" as C
    state "Suivi (parade, responsable, ticket)" as S
    state "Surveillé" as W
    state "Survenu" as X
    state "Clos" as F
    [*] --> I
    I --> C
    C --> S : criticité > 8
    C --> W : criticité ≤ 8
    W --> S : probabilité ou impact en hausse
    S --> W : parade efficace
    S --> X : l'événement se produit
    W --> X : l'événement se produit
    X --> F : réaction appliquée, leçon notée dans M3
    S --> F : la cause a disparu
    F --> [*]
```

*Utilisé à : [étape 14](E14-risques-projet.md).*


---

## Les liens entre artefacts (diagramme de classes)

### Diagramme de classes — comment les artefacts s'enchaînent (traçabilité)

```mermaid
classDiagram
    direction LR
    class PartiePrenante {
        <<C1>>
        nom
        role
        influence
        interet
    }
    class Entretien {
        <<C2 C3>>
        date
        objectifs
    }
    class Verbatim {
        <<C3>>
        numero
        texte
    }
    class Constat {
        <<C3>>
        texte
        certitude
    }
    class Besoin {
        <<C4>>
        enonce
        perimetre
    }
    class RecitUtilisateur {
        <<C4>>
        id
        moscow
    }
    class CritereAcceptation {
        <<C4>>
        etantDonne
        quand
        alors
    }
    class Indicateur {
        <<M1>>
        depart
        cible
        echeance
    }
    class Scenario {
        <<C5>>
        noteTELOS
        cout3ans
    }
    class Donnee {
        <<S1>>
        sensible
        D I C P
    }
    class Menace {
        <<S3>>
        source
        gravite
    }
    class Mesure {
        <<S3>>
        type
        responsable
    }
    class Risque {
        <<P2>>
        criticite
        parade
    }
    class TestRecette {
        <<M2>>
        attendu
        obtenu
    }
    PartiePrenante "1" -- "0..*" Entretien : est interrogée
    Entretien "1" *-- "1..*" Verbatim : contient
    Constat "0..*" --> "1..*" Verbatim : s'appuie sur
    Besoin "1" --> "1..*" Constat : reformule
    Besoin "1" *-- "1..*" RecitUtilisateur : se découpe en
    RecitUtilisateur "1" *-- "0..*" CritereAcceptation : vérifié par
    CritereAcceptation "1" --> "1..*" TestRecette : devient
    Besoin "1" --> "1..*" Indicateur : mesuré par
    Scenario "0..*" --> "0..*" RecitUtilisateur : couvre
    Menace "0..*" --> "1..*" Donnee : vise
    Mesure "1..*" --> "1..*" Menace : réduit
    Mesure "0..*" --> "0..1" TestRecette : vérifiée par
    Risque "0..*" --> "1" Scenario : concerne
```

Chaque classe est une notion de la méthode ; l'étiquette `<<C3>>` indique dans quel artefact on la trouve. Les multiplicités (`1`, `0..*`, `1..*`) se lisent : « un besoin se découpe en **un ou plusieurs** récits ». Le losange plein (composition) signifie que l'élément n'existe pas sans son parent.

*Utilisé à : [étape 7](E07-reformuler-le-besoin.md), [METHODE §4](../METHODE.md#4-carte-des-16-artefacts).*


---
[Parcours](../METHODE.md) · [Arbres de décision](arbres-de-decision.md) · [Aide-mémoire UML](aide-memoire-uml-mermaid.md)
