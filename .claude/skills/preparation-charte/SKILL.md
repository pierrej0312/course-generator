---
name: preparation-charte
description: Prépare une charte graphique pour la production automatique (analyse des templates pptx/docx, correspondance des mises en page et styles, limites de densité). À lancer pour chaque nouvelle charte ou après modification d'un template.
---
# Préparation d'une charte

Une charte = `chartes/<nom>/` avec `template.pptx`, `template.docx`, logo, et `charte-technique.json` (lu par les scripts).

## Étapes
1. Vérifier la présence de `template.pptx` et `template.docx`. S'ils manquent, les demander au formateur (modèle de son organisation ou créé dans PowerPoint/Word). **Ne jamais fabriquer une charte** à partir de couleurs supposées.
2. Vérifier les dépendances : `pip install -r "${CLAUDE_PLUGIN_ROOT}/scripts/requirements.txt"`, puis `which soffice pdftoppm montage`.
3. Lancer `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/docs/analyse_charte.py" chartes/<nom>` → produit `analyse.md` et `charte-technique.brouillon.json` (mises en page, zones, couleurs et polices du thème, styles Word — tout est lu dans les fichiers).
4. Présenter au formateur la correspondance proposée et la faire valider/corriger :
   - mises en page logiques : `titre`, `section`, `contenu`, `deux-colonnes`, `image`, `code`, `fin` ;
   - styles Word : `titre1-3`, `paragraphe`, `puce`, `puce2`, `numero`, `citation`, `code`, `tableau`, `legende` ;
   - police des blocs de code (doit être installée chez lui) ;
   - limites de densité (`puces_max`, `caracteres_par_puce`, `lignes_code_max`, `mots_max`) ;
   - si la charte autorise d'autres couleurs/polices que celles du thème : `couleurs_autorisees`, `polices_autorisees`.
   Si une mise en page manque dans le template (ex. pas de mise en page « code »), le signaler : le formateur l'ajoute dans PowerPoint ou choisit une mise en page existante.
5. Enregistrer la version validée dans `chartes/<nom>/charte-technique.json`.
6. Rédiger `chartes/<nom>/charte.md` (lisible par les humains) à partir de `analyse.md` : couleurs, polices, mises en page, règles d'usage données par le formateur.
7. Test : produire les exemples de `${CLAUDE_PLUGIN_ROOT}/scripts/docs/exemple/` avec cette charte (skill `production-documents`) et faire le contrôle visuel avec le formateur.
