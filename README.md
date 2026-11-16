# Course Generator

Base réutilisable pour concevoir des formations : du cadrage jusqu'aux supports, ateliers, évaluations et feedback.
À cloner (ou utiliser comme template GitHub) pour chaque nouveau cours.

## Installation comme plugin Claude Code

Dans une session Claude Code (terminal), ouverte dans le dossier qui servira d'espace de travail :

```text
/plugin marketplace add pierrej0312/course-generator
/plugin install course-generator@course-generator-marketplace
```

Depuis le shell : `claude plugin marketplace add pierrej0312/course-generator` puis `claude plugin install course-generator@course-generator-marketplace`.

Les skills apparaissent sous la forme `/course-generator:<skill>` (ex. `/course-generator:nouveau-cours`).
Ensuite : `/course-generator:init-espace` crée l'espace de travail, puis `/course-generator:premiere-utilisation`.

Pour tester une copie locale sans installer : `claude --plugin-dir <chemin-du-dépôt>`.
Vérifier le manifeste : `claude plugin validate <chemin-du-dépôt>`.

> Ne pas installer le plugin en ouvrant ce dépôt lui-même comme projet : ses skills `.claude/` seraient chargées deux fois.

## Utilisation directe du dépôt (sans plugin)

Cloner le dépôt et l'ouvrir dans Claude Code : les skills et agents de `.claude/` sont chargés tels quels.

## Première utilisation (chaque nouveau formateur)

1. Ouvrir le dépôt dans Claude Code.
2. Lancer `/premiere-utilisation`. Elle vérifie les outils locaux et les connecteurs (Google Drive, Agenda, Sheets, Slides — voir `config/connecteurs.md`), teste l'export Google Forms, puis enchaîne sur `/profil-formateur` (ton, vocabulaire, personnalité) et `/preparation-charte`.
   Chaque connecteur se connecte avec ton propre compte ; s'il manque, la chaîne fonctionne en mode repli.

## Démarrer un nouveau cours

1. Ouvrir le dépôt dans Claude Code.
2. Lancer la skill `/nouveau-cours` : elle crée `cours/<nom-du-cours>/` à partir des templates et pose les questions de cadrage.
3. Suivre la chaîne décrite dans `methodologie/chaine-de-production.md`.

## Arborescence

| Dossier | Contenu |
|---|---|
| `CLAUDE.md` | Règles globales lues par tous les agents (sources, ton, classement) |
| `.claude/agents/` | Un agent par rôle (documentaliste, planificateur, relecteur…) |
| `.claude/skills/` | Les méthodologies automatisées (nouveau cours, recherche, simulation…) |
| `formateurs/` | Un profil par formateur : personnalité, voix, lexique, anciens supports |
| `chartes/` | Une charte graphique par organisation / client (templates Office, couleurs, polices) |
| `profils/` | Niveaux d'apprenants, formats horaires, modalités |
| `config/` | Connecteurs et outils externes : à quoi ils servent, replis |
| `methodologie/` | Les méthodes de conception, écrites noir sur blanc |
| `bibliotheque/` | Sujets mis de côté, réutilisables entre cours + sources officielles |
| `templates/` | Squelettes markdown de chaque livrable (+ JSON Google Forms) |
| `scripts/` | Production des documents (pptx, docx, pdf, contrôle visuel) et export Google Forms |
| `cours/` | Un dossier par cours |

## À compléter avant le premier cours

- [ ] Ton profil dans `formateurs/<identifiant>/` (via `/profil-formateur`)
- [ ] Ta charte dans `chartes/<nom>/`
- [ ] `bibliotheque/sources-officielles.md` — domaines officiels par techno
