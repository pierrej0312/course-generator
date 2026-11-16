#!/usr/bin/env python3
"""Vérifie qu'un .pptx ou .docx final respecte la charte : aucune police ni couleur posée
en dur en dehors de celles de la charte (utile si le fichier a été retouché à la main).

Usage : python3 verifie_charte.py fichier.pptx|fichier.docx --charte chartes/<nom>
"""
import argparse, os, re, sys, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import charge_charte

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("fichier"); ap.add_argument("--charte", required=True)
    a = ap.parse_args()
    c = charge_charte(a.charte)
    polices = {v for v in c.get("polices", {}).values() if v}
    for sec in ("pptx", "docx"):
        if c.get(sec) and c[sec].get("police_code"):
            polices.add(c[sec]["police_code"])
    polices |= set(c.get("polices_autorisees", []))
    couleurs = {v.upper().lstrip("#") for v in c.get("palette", {}).values()}
    couleurs |= {v.upper().lstrip("#") for v in c.get("couleurs_autorisees", [])}
    pb = {}
    with zipfile.ZipFile(a.fichier) as z:
        for n in z.namelist():
            if not re.match(r"(ppt/slides/slide\d+|word/document)\.xml$", n):
                continue
            x = z.read(n).decode("utf-8", "ignore")
            for f in set(re.findall(r'<a:latin typeface="([^"+][^"]*)"', x)) | set(re.findall(r'w:ascii="([^"]+)"', x)):
                if f not in polices:
                    pb.setdefault(n, []).append(f"police hors charte : {f}")
            for col in set(re.findall(r'<a:srgbClr val="([0-9A-Fa-f]{6})"', x)) | set(re.findall(r'<w:color w:val="([0-9A-Fa-f]{6})"', x)):
                if col.upper() not in couleurs:
                    pb.setdefault(n, []).append(f"couleur hors charte : #{col}")
    if not pb:
        print("✔ Charte respectée (polices et couleurs)."); return
    for n, l in sorted(pb.items()):
        print(f"{n} :"); [print(f"  - {e}") for e in sorted(set(l))]
    sys.exit(2)

if __name__ == "__main__":
    main()
