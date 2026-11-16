# Connecteurs et outils externes

Les connecteurs sont **personnels** : chaque formateur les connecte avec son propre compte
(sur claude.ai → Paramètres → Connecteurs ; ils sont ensuite utilisables dans Claude Code avec le même compte).
Ils ne peuvent pas être livrés « préconnectés » dans le dépôt.

**Règle pour les agents : un connecteur absent ne bloque jamais la chaîne.** On utilise la solution de repli et on le signale.

| Service | Sert à | Statut | Comment l'obtenir | Repli si absent |
|---|---|---|---|---|
| Google Drive | Récupérer d'anciens supports, déposer les livrables finaux, partager avec le client | Recommandé | Connecteur Google Drive | Fichiers locaux, dépôt manuel |
| Google Agenda | Créer les sessions de formation et les rappels de préparation (J-7, J-1) | Optionnel | Connecteur Google Calendar | Fichier `.ics` ou rappel manuel |
| Google Forms | Évaluations et feedback en ligne | Requis pour l'export Forms | **Pas de connecteur trouvé** au 16/11/2026 → script Apps Script exécuté dans le compte Google du formateur (skill `export-google-forms`) | Évaluation papier (docx/pdf) |
| Google Sheets | Analyser les réponses des formulaires | Optionnel | Connecteur Google Sheets | Export CSV déposé dans `06-evaluations/resultats/` |
| Google Slides | Si le formateur présente avec Google Slides plutôt que PowerPoint | Optionnel | Connecteur Google Slides | Import manuel du .pptx dans Google Slides |
| YouTube (transcriptions) | Veille vidéo | — | Pas de connecteur : navigateur (générateur de transcription vidIQ) ou sous-titres de la vidéo | Transcription collée par le formateur |
| Recherche web | Documentation officielle | Requis | Outils WebSearch / WebFetch intégrés | — |

## Outils locaux (production des documents)
`pip install -r scripts/requirements.txt` + LibreOffice (`soffice`), Poppler (`pdftoppm`), ImageMagick (`montage`).
Vérification : `bash scripts/verifie_installation.sh`.
