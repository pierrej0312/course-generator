---
name: nouveau-cours
description: Crée le dossier d'un nouveau cours à partir des templates et orchestre la chaîne de production (cadrage → recherche → plan → simulation → ateliers → supports → relecture).
---
# Nouveau cours

0. Identifier le formateur. Si `formateurs/<identifiant>/` n'existe pas ou n'est pas configuré, lancer d'abord la skill `premiere-utilisation`. Lire `configuration.md` pour savoir quels connecteurs sont disponibles.
1. Demander le nom court du cours (kebab-case) → `cours/<nom>/`.
2. Créer l'arborescence :
   ```
   cours/<nom>/
   ├── 00-brief.md          (templates/brief.md)
   ├── 01-notes/
   │   ├── sources.md       (templates/sources.md)
   │   └── videos/
   ├── 02-plan.md           (templates/plan.md)
   ├── 03-supports/
   ├── 04-ateliers/
   ├── 05-formateur/
   ├── 06-evaluations/
   ├── simulations/
   └── journal.md           (templates/journal.md)
   ```
3. Lancer l'agent `cadrage`. **Pause : validation du brief par le formateur.**
4. Inviter le formateur à déposer ses anciens supports et ses explications dans `01-notes/`, et ses liens de vidéos.
5. Lancer `documentaliste` et `veille-video` (en parallèle si possible), puis `trieur-notes`.
6. Lancer `planificateur`. **Pause : validation du plan.**
7. Lancer la skill `simulation-cours` sur le plan. **Pause : le formateur retient/rejette les constats.**
8. Lancer `concepteur-ateliers`, puis `simulation-cours` sur les ateliers.
9. Vérifier que la charte du cours est préparée (sinon skill `preparation-charte`). Lancer `redacteur-supports`, `cahier-formateur`, `evaluations` ; produire les fichiers avec `production-documents` + `controle-visuel` ; créer les Google Forms avec `export-google-forms`.
10. Proposer `agenda-formation` (sessions + rappels de préparation) si l'agenda est connecté.
11. Lancer la skill `validation-supports` (apprenants difficile, expert, je-m'en-foutiste). **Pause : le formateur retient/rejette les constats.**
12. Lancer `relecteur`. **Pause : validation finale.**
13. Proposer `partage-drive` pour déposer les livrables.

Suivre `methodologie/chaine-de-production.md`. Journaliser chaque décision.
