#!/usr/bin/env python3
"""Génère un .docx (cahier formateur, énoncés, cheatsheet, évaluation papier…) à partir
d'un markdown et du template.docx de la charte. Seuls les styles du template sont utilisés.

Usage : python3 genere_docx.py document.md --charte chartes/<nom> --out document.docx

Markdown pris en charge : # ## ### titres, paragraphes, - puces (2 espaces = niveau 2),
1. listes numérotées, - [ ] cases à cocher, > citations, ```code```, tableaux | a | b |,
![légende](image.png), <!-- saut-de-page -->, **gras**, *italique*, `code`.
"""
import argparse, os, re, sys
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import charge_charte, segments_inline

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md"); ap.add_argument("--charte", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    charte = charge_charte(a.charte)
    cd = charte.get("docx") or sys.exit("Erreur : la charte n'a pas de section docx.")
    doc = Document(os.path.join(a.charte, cd["template"]))
    body = doc.element.body
    for el in list(body):                         # vide le contenu d'exemple, garde la mise en page
        if el.tag != qn("w:sectPr"):
            body.remove(el)
    noms = {s.name for s in doc.styles}
    alertes = set()
    pc = cd.get("police_code")
    base = os.path.dirname(os.path.abspath(a.md))

    def style(cle, defaut="paragraphe"):
        n = cd["styles"].get(cle) or cd["styles"].get(defaut)
        if n not in noms:
            alertes.add(f"style '{cle}' → '{n}' absent du template, remplacé par Normal")
            return "Normal"
        return n

    def para(texte, cle):
        p = doc.add_paragraph(style=style(cle))
        for t, st in segments_inline(texte):
            r = p.add_run(t)
            if st == "gras": r.bold = True
            elif st == "italique": r.italic = True
            elif st == "code" and pc: r.font.name = pc
        return p

    lignes = open(a.md, encoding="utf-8").read().splitlines()
    i = 0
    while i < len(lignes):
        l = lignes[i]
        if l.strip().startswith("```"):
            i += 1; bloc = []
            while i < len(lignes) and not lignes[i].strip().startswith("```"):
                bloc.append(lignes[i]); i += 1
            i += 1
            for b in bloc or [""]:
                p = doc.add_paragraph(style=style("code"))
                r = p.add_run(b)
                if pc: r.font.name = pc
                p.paragraph_format.space_after = Pt(0)
            continue
        if l.strip().startswith("|"):
            rangees = []
            while i < len(lignes) and lignes[i].strip().startswith("|"):
                cells = [c.strip() for c in lignes[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                    rangees.append(cells)
                i += 1
            if rangees:
                n = max(len(r) for r in rangees)
                t = doc.add_table(rows=len(rangees), cols=n)
                ts = cd["styles"].get("tableau")
                if ts in noms: t.style = ts
                elif ts: alertes.add(f"style de tableau '{ts}' absent du template")
                for ri, r in enumerate(rangees):
                    for ci in range(n):
                        cell = t.cell(ri, ci); cell.text = ""
                        p = cell.paragraphs[0]
                        for txt, st in segments_inline(r[ci] if ci < len(r) else ""):
                            run = p.add_run(txt)
                            run.bold = (ri == 0) or st == "gras"
                            if st == "code" and pc: run.font.name = pc
            continue
        m = re.match(r"^(#{1,3})\s+(.*)", l)
        if m:
            para(m.group(2), f"titre{len(m.group(1))}")
        elif re.match(r"\s*<!--\s*saut-de-page\s*-->", l):
            doc.add_page_break()
        elif (m := re.match(r"\s*!\[(.*?)\]\((.+?)\)", l)):
            ch = m.group(2) if os.path.isabs(m.group(2)) else os.path.join(base, m.group(2))
            if os.path.exists(ch):
                s = doc.sections[-1]
                doc.add_picture(ch, width=s.page_width - s.left_margin - s.right_margin)
                if m.group(1): para(m.group(1), "legende")
            else:
                alertes.add(f"image introuvable : {ch}")
        elif (m := re.match(r"^(\s*)[-*]\s+\[( |x)\]\s+(.*)", l)):
            para(("☑ " if m.group(2) == "x" else "☐ ") + m.group(3), "paragraphe")
        elif (m := re.match(r"^(\s*)[-*]\s+(.*)", l)):
            para(m.group(2), "puce2" if len(m.group(1)) >= 2 else "puce")
        elif (m := re.match(r"^\s*\d+[.)]\s+(.*)", l)):
            para(m.group(1), "numero")
        elif l.startswith(">"):
            para(l.lstrip("> ").strip(), "citation")
        elif l.strip():
            para(l.strip(), "paragraphe")
        i += 1
    doc.save(a.out)
    print(f"✔ {a.out}")
    if "[À VÉRIFIER]" in "\n".join(lignes):
        alertes.add("le document contient encore [À VÉRIFIER]")
    if alertes:
        print("\nAlertes :"); print("\n".join(f"- {x}" for x in sorted(alertes))); sys.exit(2)

if __name__ == "__main__":
    main()
