"""Fonctions partagées : lecture de la charte technique et du markdown inline."""
import json, os, re, sys

def charge_charte(dossier):
    p = os.path.join(dossier, "charte-technique.json")
    if not os.path.exists(p):
        sys.exit(f"Erreur : {p} introuvable. Lancer d'abord la skill preparation-charte.")
    c = json.load(open(p, encoding="utf-8"))
    c["_dossier"] = dossier
    return c

INLINE = re.compile(r"(\*\*[^*]+\*\*|`[^`]+`|\*[^*]+\*)")

def segments_inline(texte):
    """Découpe 'du **gras**, du `code` et de l'*italique*' en [(texte, style)]."""
    out = []
    for morceau in INLINE.split(texte):
        if not morceau:
            continue
        if morceau.startswith("**") and morceau.endswith("**"):
            out.append((morceau[2:-2], "gras"))
        elif morceau.startswith("`") and morceau.endswith("`"):
            out.append((morceau[1:-1], "code"))
        elif morceau.startswith("*") and morceau.endswith("*") and len(morceau) > 2:
            out.append((morceau[1:-1], "italique"))
        else:
            out.append((morceau, None))
    return out
