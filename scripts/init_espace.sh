#!/usr/bin/env bash
# Crée (ou complète) un espace de travail formateur à partir du plugin.
# N'écrase jamais un fichier existant.
# Usage : bash init_espace.sh <dossier_du_plugin> <dossier_espace>
set -euo pipefail
src="$1"; dst="$2"
mkdir -p "$dst"
copie() {  # copie récursive sans écraser
  local s="$src/$1" d="$dst/$1"
  [ -e "$s" ] || { echo "absent dans le plugin : $1"; return; }
  if [ -d "$s" ]; then mkdir -p "$d"; cp -Rn "$s/." "$d/"; else mkdir -p "$(dirname "$d")"; cp -n "$s" "$d"; fi
  echo "✔ $1"
}
for e in CLAUDE.md templates profils methodologie config \
         bibliotheque/README.md bibliotheque/index.md bibliotheque/sources-officielles.md \
         formateurs/README.md formateurs/_modele chartes/README.md chartes/_modele; do
  copie "$e"
done
mkdir -p "$dst/bibliotheque/sujets" "$dst/cours"
[ -e "$dst/.gitignore" ] || cp "$src/.gitignore" "$dst/.gitignore"
echo "Espace prêt : $dst"
