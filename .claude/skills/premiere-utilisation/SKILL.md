---
name: premiere-utilisation
description: Configuration de la première utilisation pour un nouveau formateur — outils locaux, connecteurs (Google Drive, Agenda, Sheets, Slides), test Google Forms, profil formateur et charte. À relancer pour revérifier la configuration.
---
# Première utilisation

Objectif : un formateur prêt à produire un cours, avec un état clair de ce qui marche et des replis pour le reste. Avancer étape par étape, en expliquant chaque étape en une phrase.

1. **Identité** — demander nom et identifiant. Créer `formateurs/<identifiant>/` depuis `formateurs/_modele/` s'il n'existe pas.
2. **Outils locaux** — lancer `bash scripts/verifie_installation.sh`. Pour chaque manque, donner la commande d'installation adaptée à son système (demander lequel) ; ne pas installer sans son accord.
3. **Connecteurs** — lire `config/connecteurs.md`. Pour chaque service :
   - vérifier s'il est disponible dans la session (outils dont le nom contient `Google_Drive`, `Google_Calendar`, `Google_Sheets`, `Google_Slides`, ou équivalent) ;
   - s'il est disponible : faire un appel de lecture inoffensif (ex. lister les fichiers récents, lister les agendas) pour confirmer qu'il répond ;
   - s'il manque : expliquer à quoi il sert dans la chaîne, et que le formateur peut le connecter avec son compte dans les paramètres de connecteurs de claude.ai, puis relancer la skill ; ou le refuser (repli noté).
   Ne jamais présenter un connecteur comme obligatoire s'il a un repli.
4. **Préférences liées aux connecteurs** (si connectés) : dossier Drive racine pour les livrables, agenda à utiliser pour les formations.
5. **Google Forms** — proposer un test : générer le script d'exemple (`templates/feedback-forms.json`) avec la skill `export-google-forms`, le formateur l'exécute sur script.google.com et confirme que le formulaire est créé. Il peut le supprimer ensuite.
6. **Profil formateur** — lancer `/profil-formateur`.
7. **Charte** — demander quelle(s) charte(s) il utilise ; pour chacune absente ou non préparée, lancer `/preparation-charte`.
8. **Récapitulatif** — remplir `formateurs/<identifiant>/configuration.md` (états réels constatés, rien de supposé) et afficher : ce qui est prêt, ce qui fonctionne en mode repli, ce qui reste à faire. Proposer ensuite `/nouveau-cours`.
