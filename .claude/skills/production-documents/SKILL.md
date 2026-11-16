---
name: production-documents
description: Produit les fichiers finaux d'un cours (diapositives pptx + pdf, cheatsheet, cahier formateur, énoncés d'atelier, évaluation papier en docx + pdf) à partir des markdown, en respectant strictement la charte, puis lance le contrôle visuel.
---
# Production des documents

Principe : **le markdown est la source, le fichier Office est un produit.** Toute correction se fait dans le markdown ou dans la charte, puis on régénère. On ne retouche jamais un .pptx/.docx généré pour « arranger » un détail.

## Prérequis
- Charte du cours (brief) préparée : `chartes/<charte>/charte-technique.json` présent. Sinon → skill `preparation-charte`.
- Dépendances : `scripts/requirements.txt` + LibreOffice, pdftoppm, ImageMagick.

## Formats source
- Diapositives : `03-supports/slides.md` — format décrit en tête de `scripts/docs/genere_pptx.py` (exemple : `scripts/docs/exemple/slides.md`). Une diapo = une idée ; préciser la mise en page logique ; notes orateur obligatoires sur les diapos de contenu.
- Documents : markdown simple — format décrit en tête de `scripts/docs/genere_docx.py` (exemple : `scripts/docs/exemple/cahier.md`).

## Commandes
```bash
C=chartes/<charte>
# Diapositives
python3 scripts/docs/genere_pptx.py 03-supports/slides.md --charte $C --out 03-supports/<cours>.pptx
# Documents
python3 scripts/docs/genere_docx.py 03-supports/cheatsheet.md        --charte $C --out 03-supports/cheatsheet.docx
python3 scripts/docs/genere_docx.py 05-formateur/cahier.md           --charte $C --out 05-formateur/cahier.docx
python3 scripts/docs/genere_docx.py 04-ateliers/<atelier>/enonce.md  --charte $C --out 04-ateliers/<atelier>/enonce.docx
# Vérification charte (polices / couleurs hors charte)
python3 scripts/docs/verifie_charte.py <fichier> --charte $C
# PDF + images pour contrôle visuel
bash scripts/docs/apercu.sh <fichier> <dossier>/apercu
```
Les chemins sont relatifs au dossier du cours pour les sources, à la racine du dépôt pour `scripts/` et `chartes/`.

## Alertes
Code retour 2 = fichier produit **avec alertes** (densité dépassée, `[À VÉRIFIER]`, notes manquantes, style absent…). Chaque alerte se corrige dans la source : découper la diapo, raccourcir, déplacer le détail en notes orateur ou dans la cheatsheet. Ne pas augmenter les limites de la charte pour faire taire une alerte sans l'accord du formateur.

## Ensuite
Toujours enchaîner sur la skill `controle-visuel`. Le PDF livré est celui produit par `apercu.sh` une fois le contrôle visuel validé.
