---
name: transcription-video
description: Récupère la transcription d'une vidéo YouTube de vulgarisation et en extrait idées pédagogiques et faits à vérifier.
---
# Transcription vidéo

Entrée : URL YouTube + cours concerné.

1. Obtenir la transcription, au choix :
   - générateur de transcription YouTube de vidIQ (gratuit, sans inscription) via le navigateur ;
   - extraction des sous-titres de la vidéo ;
   - transcription collée par le formateur.
   Si la vidéo n'a pas de sous-titres et qu'aucune transcription n'est fournie : le signaler, ne rien résumer.
2. Créer `cours/<cours>/01-notes/videos/<chaine>-<titre-court>.md` (template `templates/video.md`).
3. Extraire analogies, ordre des idées, exemples.
4. Lister les faits techniques affirmés → à vérifier avec la skill `recherche-sources`.
