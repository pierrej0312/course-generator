---
name: recherche-sources
description: Recherche documentaire sur un thème de cours en priorité dans la documentation officielle, avec traçabilité complète et sans aucune source inventée.
---
# Recherche de sources

Entrée : un thème + le cours concerné.

1. Lire `bibliotheque/sources-officielles.md` pour la technologie concernée.
2. Rechercher (WebSearch) en restreignant d'abord aux domaines officiels.
3. Ouvrir chaque page retenue (WebFetch). Une page non ouverte ne peut pas être citée.
4. Remplir `cours/<cours>/01-notes/sources.md` : titre exact, URL, type, version, date, usage.
5. Résumer dans `01-notes/recherche-<theme>.md` en renvoyant aux numéros de sources.
6. Tout point non confirmé → `[À VÉRIFIER]` + liste en bas de `sources.md`.
7. Rapporter au formateur : ce qui est confirmé, ce qui ne l'est pas, les écarts de version.
