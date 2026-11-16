---
name: validation-supports
description: Valide les supports et ateliers d'un cours en les faisant passer par trois apprenants simulés (difficile, expert, je-m'en-foutiste), puis synthétise leurs retours pour décision du formateur.
---
# Validation des supports

Entrée : le cours (`cours/<nom>/`). Prérequis : `03-supports/` et `04-ateliers/` rédigés.

1. Lancer **en parallèle**, sans leur transmettre l'historique de conception (seulement `00-brief.md`, `02-plan.md`, `03-supports/`, `04-ateliers/`, `01-notes/sources.md`) :
   - `apprenant-difficile`
   - `apprenant-expert`
   - `apprenant-mefoutiste`
2. Attendre les trois rapports dans `simulations/`.
3. Écrire `simulations/supports-synthese.md` :
   - **Erreurs confirmées** (expert, avec preuve) → à corriger en priorité.
   - **Doutes à vérifier** (expert) → passer à la skill `recherche-sources`.
   - **Questions à préparer** (difficile) → réponses à mettre en notes orateur ou dans le cahier formateur.
   - **Points de décrochage** (je-m'en-foutiste) → reformulation, découpage, interaction à ajouter.
   - Points soulevés par plusieurs profils en tête de liste.
4. Présenter la synthèse au formateur ; pour chaque point : retenu / rejeté.
5. Reporter les décisions dans `journal.md`. Ne modifier les supports qu'après décision.
6. Les réponses préparées retenues vont dans `05-formateur/cahier.md` (section « Questions probables »).
