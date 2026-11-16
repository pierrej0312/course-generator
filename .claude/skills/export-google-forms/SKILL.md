---
name: export-google-forms
description: Transforme l'évaluation (quiz) et le questionnaire de feedback d'un cours en Google Forms en ligne, via un script Apps Script généré que le formateur exécute dans son compte Google.
---
# Export vers Google Forms

Pourquoi Apps Script : le script s'exécute dans le compte Google du formateur, sans projet Google Cloud ni clé d'API à configurer. Chaque formateur crée les formulaires dans son propre Drive.

## Étapes
1. À partir de `06-evaluations/evaluation.md` (validée par le formateur), écrire `06-evaluations/evaluation.forms.json` au format de `templates/evaluation-forms.json` :
   - `quiz: true`, points, bonnes réponses, feedback correct/incorrect renvoyant à la séquence du cours ;
   - types disponibles : `choix_unique`, `choix_multiple`, `texte_long`, `echelle`.
2. Idem pour le feedback : `06-evaluations/feedback.forms.json` (base : `templates/feedback-forms.json`, `quiz: false`).
3. Générer les scripts :
   ```bash
   python3 scripts/forms/genere_apps_script.py 06-evaluations/evaluation.forms.json > 06-evaluations/evaluation.gs
   python3 scripts/forms/genere_apps_script.py 06-evaluations/feedback.forms.json  > 06-evaluations/feedback.gs
   ```
   Le générateur refuse un quiz incohérent (choix unique sans exactement une bonne réponse, etc.) : corriger le JSON, ne pas contourner.
4. Donner au formateur la marche à suivre :
   1. ouvrir https://script.google.com → **Nouveau projet** ;
   2. remplacer le contenu par celui du fichier `.gs` ;
   3. exécuter la fonction `creerFormulaire` et accepter l'autorisation demandée par Google ;
   4. le **journal d'exécution** affiche le lien apprenants et le lien d'édition.
5. Noter les deux liens dans `06-evaluations/liens-forms.md` et dans le cahier formateur, et journaliser.
6. Rappeler au formateur de vérifier le formulaire dans l'éditeur Google Forms avant de l'envoyer (paramètres de collecte des e-mails, publication des notes).

## Après la formation
Les réponses se consultent dans l'onglet Réponses du formulaire (export Google Sheets possible). Pour l'analyse et l'amélioration du cours, exporter en CSV et le déposer dans `06-evaluations/resultats/`.
