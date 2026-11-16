#!/usr/bin/env python3
"""Analyse les templates d'une charte (template.pptx / template.docx) et écrit
charte-technique.brouillon.json + un résumé lisible. Rien n'est inventé : tout
provient des fichiers. Le formateur valide ensuite le mapping (skill preparation-charte).

Usage : python3 analyse_charte.py chartes/<nom>
"""
import json, os, sys, zipfile
from lxml import etree

NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}

def theme_pptx(path):
    """Couleurs et polices du thème, lues dans ppt/theme/theme*.xml."""
    res = {"couleurs": {}, "polices": {}}
    with zipfile.ZipFile(path) as z:
        themes = sorted(n for n in z.namelist() if n.startswith("ppt/theme/theme"))
        if not themes:
            return res
        root = etree.fromstring(z.read(themes[0]))
    sch = root.find(".//a:clrScheme", NS)
    if sch is not None:
        for el in sch:
            nom = etree.QName(el).localname
            srgb = el.find("a:srgbClr", NS)
            sysc = el.find("a:sysClr", NS)
            if srgb is not None:
                res["couleurs"][nom] = "#" + srgb.get("val")
            elif sysc is not None and sysc.get("lastClr"):
                res["couleurs"][nom] = "#" + sysc.get("lastClr")
    for cle, tag in (("titres", "majorFont"), ("corps", "minorFont")):
        f = root.find(f".//a:{tag}/a:latin", NS)
        if f is not None:
            res["polices"][cle] = f.get("typeface")
    return res

def devine(noms, *mots):
    for mot in mots:
        for n in noms:
            if mot in n.lower():
                return n
    return None

def analyse_pptx(path):
    from pptx import Presentation
    prs = Presentation(path)
    layouts = {}
    for m in prs.slide_masters:
        for l in m.slide_layouts:
            layouts[l.name] = [
                {"idx": ph.placeholder_format.idx, "type": str(ph.placeholder_format.type).split(".")[-1].split(" ")[0],
                 "nom": ph.name}
                for ph in l.placeholders]
    noms = list(layouts)
    proposition = {
        "titre": devine(noms, "title slide", "titre", "diapositive de titre", "title"),
        "section": devine(noms, "section"),
        "contenu": devine(noms, "title and content", "titre et contenu", "content", "contenu"),
        "deux-colonnes": devine(noms, "two content", "deux contenus", "comparison", "comparaison"),
        "image": devine(noms, "picture", "image"),
        "code": devine(noms, "code", "title only", "titre seul"),
        "fin": devine(noms, "end", "fin", "closing"),
    }
    return layouts, proposition, (prs.slide_width, prs.slide_height)

def analyse_docx(path):
    from docx import Document
    from docx.enum.style import WD_STYLE_TYPE
    doc = Document(path)
    para = [s.name for s in doc.styles if s.type == WD_STYLE_TYPE.PARAGRAPH]
    tabl = [s.name for s in doc.styles if s.type == WD_STYLE_TYPE.TABLE]
    def p(*m):
        return devine(para, *m)
    proposition = {
        "titre1": p("heading 1", "titre 1"), "titre2": p("heading 2", "titre 2"),
        "titre3": p("heading 3", "titre 3"), "paragraphe": p("normal"),
        "puce": p("list bullet", "liste à puces"), "puce2": p("list bullet 2", "liste à puces 2"),
        "numero": p("list number", "liste numérotée"), "citation": p("quote", "citation"),
        "code": p("code", "html preformatted", "macro"), "tableau": devine(tabl, "table grid", "grille", "table"),
    }
    return para, tabl, proposition

def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    d = sys.argv[1]
    brouillon = {"pptx": None, "docx": None, "palette": {}, "polices": {}}
    lignes = [f"# Analyse de la charte `{d}`", ""]
    pp = os.path.join(d, "template.pptx")
    if os.path.exists(pp):
        layouts, prop, (w, h) = analyse_pptx(pp)
        th = theme_pptx(pp)
        brouillon["palette"], brouillon["polices"] = th["couleurs"], th["polices"]
        brouillon["pptx"] = {"template": "template.pptx", "layouts": prop,
                             "limites": {"puces_max": 6, "caracteres_par_puce": 90, "lignes_code_max": 14, "mots_max": 60},
                             "police_code": None, "taille_code_pt": 14}
        lignes += [f"## template.pptx — format {round(w/914400*2.54,1)} × {round(h/914400*2.54,1)} cm", "",
                   "| Mise en page | Zones (idx : type) |", "|---|---|"]
        for n, phs in layouts.items():
            lignes.append(f"| {n} | " + ", ".join(f"{p['idx']}:{p['type']}" for p in phs) + " |")
        lignes += ["", "### Thème", "", "| Rôle | Couleur |", "|---|---|"]
        lignes += [f"| {k} | {v} |" for k, v in th["couleurs"].items()]
        lignes += ["", f"Polices : titres = {th['polices'].get('titres')}, corps = {th['polices'].get('corps')}", "",
                   "### Correspondance proposée (À VALIDER)", ""]
        lignes += [f"- {k} → {v if v else '**aucune mise en page trouvée**'}" for k, v in prop.items()]
    else:
        lignes.append("⚠️ template.pptx absent.")
    dp = os.path.join(d, "template.docx")
    if os.path.exists(dp):
        para, tabl, prop = analyse_docx(dp)
        brouillon["docx"] = {"template": "template.docx", "styles": prop, "police_code": None}
        lignes += ["", "## template.docx", "", "Styles de paragraphe : " + ", ".join(para), "",
                   "Styles de tableau : " + ", ".join(tabl), "", "### Correspondance proposée (À VALIDER)", ""]
        lignes += [f"- {k} → {v if v else '**aucun style trouvé**'}" for k, v in prop.items()]
    else:
        lignes.append("\n⚠️ template.docx absent.")
    lignes += ["", "⚠️ `police_code` est vide : à choisir avec le formateur (police monospace installée chez lui)."]
    json.dump(brouillon, open(os.path.join(d, "charte-technique.brouillon.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    open(os.path.join(d, "analyse.md"), "w", encoding="utf-8").write("\n".join(lignes) + "\n")
    print("\n".join(lignes))

if __name__ == "__main__":
    main()
