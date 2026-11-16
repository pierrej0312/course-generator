# Règles du dépôt Course Generator

> Ce fichier est copié dans chaque espace de travail par `/init-espace` (un plugin ne charge pas de CLAUDE.md lui-même).
> Dans les skills et agents, `${CLAUDE_PLUGIN_ROOT}` désigne le dossier du plugin installé. S'il apparaît tel quel (non remplacé), le dépôt est utilisé directement : remplace-le par la racine du dépôt.

Ce dépôt sert à concevoir des formations. Tout agent qui travaille ici respecte les règles ci-dessous.

## 1. Sources : ne jamais inventer

- Aucune affirmation technique (commande, option, version, comportement, chiffre) sans **URL réellement consultée** pendant la session.
- Toute source utilisée est consignée dans `cours/<cours>/01-notes/sources.md` (URL, date de consultation, version documentée, où elle sert).
- Priorité aux domaines listés dans `bibliotheque/sources-officielles.md`. Blogs, forums et vidéos = compléments, toujours signalés comme tels.
- Ce qui n'est pas sourcé est marqué `[À VÉRIFIER]`. Aucun support final ne sort tant qu'il en reste un.
- Ne jamais fabriquer une URL, un titre de page, une citation ou un numéro de version. En cas de doute : le dire.

## 2. Vidéos de vulgarisation

- Une vidéo est une **source d'inspiration** (analogies, ordre des idées, façon d'expliquer), **pas une source factuelle**.
- Transcription rangée dans `cours/<cours>/01-notes/videos/` avec URL, chaîne, date.
- Tout fait repris d'une vidéo est confirmé par la documentation officielle avant d'entrer dans le cours.

## 3. Ton et style : la voix du formateur du cours

Ce dépôt est partagé par plusieurs formateurs. Il n'existe **pas de voix par défaut**.

- Le formateur d'un cours est indiqué dans `cours/<cours>/00-brief.md` (champ « Formateur »).
- Avant de rédiger quoi que ce soit destiné aux apprenants, lire `formateurs/<identifiant>/profil.md`, `voix.md` et `lexique.md`.
- Si le profil n'existe pas ou est vide : s'arrêter et proposer la skill `/profil-formateur`. Ne jamais rédiger dans une voix générique ni emprunter le profil d'un autre formateur.
- `formateurs/_modele/` est un squelette vierge, jamais une source de style.
- Interdits : formules creuses (« dans le monde en constante évolution », « plongeons dans », « il est important de noter »), listes génériques sans exemple concret, énoncés d'exercice interchangeables d'un cours à l'autre.
- Chaque notion s'appuie sur un exemple concret lié au fil rouge du cours.
- Adapter la profondeur au niveau défini dans `profils/niveaux.md` (ingénieurs = explications internes, compromis, cas limites).

## 4. Contraintes du cours

Toujours lire `cours/<cours>/00-brief.md` avant de produire : durée (demi-jour / jour / multi-jours), niveau, modalité (présentiel / distanciel), matériel des apprenants. Le temps disponible prime : ce qui ne tient pas va dans la bibliothèque.

## 5. Classement des notes

- Notes brutes, discussions, anciens supports → `cours/<cours>/01-notes/`.
- Sujet pertinent mais hors périmètre ou trop poussé pour ce cours → `bibliotheque/sujets/<sujet>.md` (template `templates/sujet-bibliotheque.md`), avec un lien depuis le cours d'origine et l'inverse.
- Avant de rédiger un nouveau cours, chercher dans `bibliotheque/sujets/` ce qui peut être réutilisé.

## 6. Traçabilité

Chaque décision (coupe, ajout, choix pédagogique, retour de simulation retenu ou rejeté) est ajoutée dans `cours/<cours>/journal.md`, datée, avec sa raison.

## 7. Charte graphique

- Charte du cours = champ « Charte » du brief ; à défaut, la charte par défaut du profil formateur.
- Tous les supports (pptx, pdf, docx, cheatsheet) utilisent exclusivement les templates de `chartes/<charte>/`.
- Charte absente ou incomplète : s'arrêter et le signaler. Ne jamais inventer de couleurs ou polices.
