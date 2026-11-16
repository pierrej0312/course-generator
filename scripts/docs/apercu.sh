#!/usr/bin/env bash
# Rend un .pptx/.docx/.pdf en images pour le contrôle visuel.
# Usage : bash apercu.sh fichier.(pptx|docx|pdf) [dossier_sortie]
# Produit : <sortie>/<nom>.pdf, <sortie>/pages/page-NN.png, <sortie>/planche.png
# Attention : rendu LibreOffice. Si une police de la charte n'est pas installée sur la
# machine, elle est remplacée : le rendu final se vérifie aussi dans PowerPoint/Word.
set -euo pipefail
f="$1"; out="${2:-$(dirname "$f")/apercu}"
mkdir -p "$out/pages"
nom="$(basename "${f%.*}")"
case "$f" in
  *.pdf) cp "$f" "$out/$nom.pdf" ;;
  *) soffice --headless --convert-to pdf --outdir "$out" "$f" >/dev/null 2>&1 ;;
esac
pdftoppm -r 60 -png "$out/$nom.pdf" "$out/pages/page"
montage "$out"/pages/page-*.png -tile 4x -geometry +6+6 -background '#888888' "$out/planche.png" 2>/dev/null || true
echo "PDF : $out/$nom.pdf"
echo "Pages : $(ls "$out/pages" | wc -l) images dans $out/pages"
echo "Planche : $out/planche.png"
fc-list : family | sort -u > "$out/polices-installees.txt"
