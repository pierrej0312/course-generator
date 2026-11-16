# Chaîne de production d'un cours

| # | Étape | Agent | Livrable |
|---|---|---|---|
| 1 | Cadrage | `cadrage` | `00-brief.md` |
| 2 | Recherche documentaire | `documentaliste` | `01-notes/sources.md`, notes |
| 3 | Veille vidéo | `veille-video` | `01-notes/videos/*.md` |
| 4 | Tri des notes | `trieur-notes` | notes classées, sujets envoyés en `bibliotheque/` |
| 5 | Plan | `planificateur` | `02-plan.md` |
| 6 | Simulation (plan) | `avocat-du-diable`, `apprenant-simule` | `simulations/plan-*.md` |
| 7 | Ateliers | `concepteur-ateliers` | `04-ateliers/` |
| 8 | Supports | `redacteur-supports` | `03-supports/` (pptx, pdf, cheatsheet) |
| 9 | Cahier formateur | `cahier-formateur` | `05-formateur/cahier.md` |
| 10 | Évaluations & feedback | `evaluations` (+ skill `export-google-forms`) | `06-evaluations/`, Google Forms en ligne |
| 11 | Simulation (ateliers) | `apprenant-simule` | `simulations/ateliers-*.md` |
| 12 | Validation des supports | `apprenant-difficile`, `apprenant-expert`, `apprenant-mefoutiste` (skill `validation-supports`) | `simulations/supports-*.md` |
| 13 | Relecture finale | `relecteur` | `07-relecture.md` |

Étapes 8 à 10 : les fichiers Office/PDF sont produits par la skill `production-documents` puis vérifiés par `controle-visuel` (le markdown reste la source).

Chaque étape ajoute ses décisions dans `journal.md`.
Tu valides à la fin des étapes 1, 5, 6, 12 et 13 avant de continuer.
