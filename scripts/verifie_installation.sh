#!/usr/bin/env bash
# Vérifie les outils locaux nécessaires à la production des documents.
ok=0
for b in python3 soffice pdftoppm montage; do
  if command -v "$b" >/dev/null 2>&1; then echo "✔ $b"; else echo "✘ $b manquant"; ok=1; fi
done
for m in pptx docx lxml PIL; do
  if python3 -c "import $m" 2>/dev/null; then echo "✔ python : $m"; else echo "✘ python : $m manquant (pip install -r scripts/requirements.txt)"; ok=1; fi
done
exit $ok
