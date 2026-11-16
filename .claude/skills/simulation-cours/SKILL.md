---
name: simulation-cours
description: Challenge un plan ou des ateliers en lançant un avocat du diable et des apprenants simulés de plusieurs profils, puis synthétise les constats pour décision du formateur.
---
# Simulation

Entrée : document cible (plan ou atelier) + cours.

1. Lire le brief pour déterminer les profils pertinents (niveau, modalité, contraintes matérielles).
2. Lancer en parallèle, **sans leur transmettre l'historique de conception** :
   - `avocat-du-diable` sur le document ;
   - `apprenant-simule` pour 2 à 3 profils (ex. profil cible, profil plus faible, profil distanciel/contraint).
3. Synthétiser dans `simulations/<cible>-synthese.md` : constats dédoublonnés, triés par gravité.
4. Présenter la synthèse au formateur et lui demander pour chaque point bloquant/gênant : retenu ou rejeté.
5. Reporter les décisions dans `journal.md`. Ne modifier le document qu'après décision.
