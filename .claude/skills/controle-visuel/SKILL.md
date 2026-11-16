---
name: controle-visuel
description: Contrôle visuel des documents produits (pptx, docx, pdf) en les rendant en images et en vérifiant mise en page, débordements, lisibilité et cohérence avec la charte. À utiliser après chaque génération de document.
---
# Contrôle visuel

1. Rendre le fichier : `bash scripts/docs/apercu.sh <fichier> <dossier>/apercu` → PDF, une image par page, planche contact.
2. Regarder **la planche** pour la cohérence d'ensemble, puis **chaque page** concernée en détail.
3. Vérifier, page par page :
   - **Débordements** : texte qui sort de sa zone ou passe sous un autre élément, code coupé, tableau qui déborde de la page.
   - **Densité** : diapo lisible en 5 secondes ? texte trop petit (réduction automatique) ? plus de 6 lignes serrées ?
   - **Alignements** : titres à la même position d'une diapo à l'autre, images centrées, rien de collé au bord.
   - **Cohérence** : mêmes mises en page pour les mêmes types de contenu, numérotation des sections, pas de zone vide « Cliquez pour ajouter… ».
   - **Charte** : couleurs, polices, logo, pied de page conformes ; `verifie_charte.py` sans alerte.
   - **Images** : nettes, non déformées, lisibles en projection (et en partage d'écran si distanciel).
   - **Documents Word** : sauts de page placés aux bons endroits, pas de titre orphelin en bas de page, cases à cocher et tableaux lisibles à l'impression.
4. Consigner les constats dans `<dossier>/apercu/controle.md` : page, problème, correction prévue (dans la source markdown ou la charte).
5. Corriger les sources, régénérer (skill `production-documents`), recontrôler jusqu'à zéro constat bloquant.

## Limite à connaître
Le rendu est fait par LibreOffice. Si une police de la charte n'est pas installée sur la machine (voir `apercu/polices-installees.txt`), elle est remplacée et la mise en page peut différer légèrement. Le signaler au formateur et lui demander une vérification finale dans PowerPoint/Word.
