<!-- layout: titre -->
# Git au quotidien
Formation technicien — 1 journée
---
<!-- layout: section -->
# 1. Pourquoi versionner ?
---
# Ce que Git enregistre
- Un **commit** = un instantané du projet
- Chaque commit pointe vers son parent
  - sauf le premier
- Les branches sont de simples *pointeurs* vers un commit
Notes:
Partir de l'exemple du fil rouge : le site de la boulangerie.
---
<!-- layout: code -->
# Créer une branche
```bash
git switch -c feature/menu
git add menu.html
git commit -m "Ajoute le menu"
```
Notes:
Montrer git log --oneline après.
---
<!-- layout: deux-colonnes -->
# merge ou rebase ?
- merge garde l'historique réel
- crée un commit de fusion
|||
- rebase réécrit l'historique
- à éviter sur une branche partagée [À VÉRIFIER]
Notes:
Question piège classique.
---
<!-- layout: image -->
# Schéma du flux
![Flux des branches](schema.png)
Notes:
Schéma.
---
# Trop chargée
- point 1 avec un texte très long qui dépasse largement la limite de caractères prévue par la charte pour une puce
- point 2
- point 3
- point 4
- point 5
- point 6
- point 7
Notes:
test
