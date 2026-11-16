---
name: partage-drive
description: Dépose les livrables finaux d'un cours (pdf, pptx, docx, fichiers d'atelier) dans Google Drive, dans une arborescence propre, et récupère depuis Drive d'anciens supports à importer.
---
# Partage via Google Drive

Prérequis : connecteur Google Drive disponible (sinon repli : indiquer au formateur les fichiers à déposer lui-même).

## Déposer les livrables
1. Vérifier que la relecture finale (`07-relecture.md`) est « prêt ». Sinon, demander confirmation avant de déposer.
2. Dossier racine : celui de `formateurs/<identifiant>/configuration.md` (le demander s'il est vide).
3. Arborescence proposée : `<racine>/<cours>/Apprenants/` (pdf des supports, cheatsheet, énoncés, fichiers d'atelier) et `<racine>/<cours>/Formateur/` (pptx, cahier, corrigés, évaluations). Ne jamais mettre les corrigés ou le cahier dans le dossier apprenants.
4. Montrer la liste des fichiers et leur destination, déposer après validation.
5. Ne modifier aucun droit de partage sans demande explicite. Noter les liens dans `journal.md`.

## Récupérer d'anciens supports
Chercher dans Drive les fichiers indiqués par le formateur, les télécharger dans `cours/<cours>/01-notes/anciens-supports/` (ou `formateurs/<identifiant>/exemples/` pour le profil), sans les modifier sur Drive.
