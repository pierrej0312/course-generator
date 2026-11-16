---
name: agenda-formation
description: Crée dans Google Agenda les sessions d'une formation et les rappels de préparation issus du cahier formateur (J-7, J-1, vérifications matérielles).
---
# Agenda de la formation

Prérequis : connecteur Google Agenda disponible (sinon repli : générer un fichier `05-formateur/formation.ics` et le signaler).

1. Lire `00-brief.md` (dates, horaires, modalité, lieu ou lien visio) et `05-formateur/cahier.md` (préparations).
   Si les dates ne sont pas dans le brief, les demander — ne jamais les supposer.
2. Lire dans `formateurs/<identifiant>/configuration.md` l'agenda à utiliser.
3. Proposer au formateur la liste des événements avant toute création :
   - une session par jour (demi-journée) de formation, avec le lien visio ou l'adresse ;
   - rappels de préparation : J-7 (installations, tests de l'environnement), J-1 (vérifications), avec la checklist du cahier dans la description.
4. Créer les événements validés, puis noter leurs liens dans `05-formateur/cahier.md` et dans `journal.md`.
5. Ne jamais inviter des apprenants ou des tiers sans demande explicite du formateur.
