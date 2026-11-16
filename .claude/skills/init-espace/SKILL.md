---
name: init-espace
description: Crée l'espace de travail du formateur dans le projet courant (règles CLAUDE.md, templates, profils, méthodologie, modèles de profil et de charte, dossiers cours et bibliothèque). À lancer une fois après l'installation du plugin, avant /premiere-utilisation.
---
# Initialiser l'espace de travail

Le plugin contient la méthode (agents, skills, scripts). Les données du formateur (profil, chartes, cours, bibliothèque) vivent dans **son** projet : c'est l'espace de travail.

1. Vérifier si le projet courant contient déjà `CLAUDE.md` et `templates/`. Si oui : espace déjà initialisé, proposer seulement de le compléter (rien n'est écrasé).
2. Montrer au formateur le dossier cible (le projet courant) et attendre son accord.
3. Lancer :
   ```bash
   bash "${CLAUDE_PLUGIN_ROOT}/scripts/init_espace.sh" "${CLAUDE_PLUGIN_ROOT}" "$(pwd)"
   ```
4. Expliquer que `CLAUDE.md` contient les règles communes (sources, voix, charte, classement) et qu'il est chargé automatiquement dans ce projet. Il peut l'adapter, mais les règles sur les sources ne doivent pas être affaiblies.
5. Conseiller d'en faire un dépôt Git **privé** (les cours clients ne doivent pas être publics).
6. Enchaîner sur `/premiere-utilisation`.

Si `${CLAUDE_PLUGIN_ROOT}` n'est pas remplacé par un chemin (dépôt utilisé directement, sans plugin), l'espace de travail est le dépôt lui-même : rien à copier.
