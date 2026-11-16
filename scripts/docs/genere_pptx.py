#!/usr/bin/env python3
"""Génère un .pptx à partir d'un slides.md et du template de la charte.
Aucune couleur ni police n'est posée en dur : tout vient des mises en page du template
(seule exception : la police des blocs de code, définie dans la charte).

Usage : python3 genere_pptx.py slides.md --charte chartes/<nom> --out supports.pptx

Format de slides.md : diapositives séparées par une ligne '---'.
  <!-- layout: contenu -->      (titre | section | contenu | deux-colonnes | image | code | fin ; défaut : contenu)
  # Titre de la diapositive
  - puce            (indentation de 2 espaces = niveau suivant ; **gras**, *italique*, `code`)
  ```langage        (bloc de code)
  |||               (deux-colonnes : sépare colonne gauche / droite)
  ![légende](chemin/image.png)
  Notes:            (tout ce qui suit = notes orateur)
"""
import argparse, os, re, sys
from pptx import Presentation
from pptx.util import Pt, Emu
from pptx.enum.shapes import PP_PLACEHOLDER
from pptx.oxml.ns import qn
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import charge_charte, segments_inline

EXCLUS = {PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE, PP_PLACEHOLDER.DATE,
          PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.SLIDE_NUMBER}

def decoupe(md):
    slides, cur, dans_code = [], [], False
    for ligne in md.splitlines():
        if ligne.strip().startswith("```"):
            dans_code = not dans_code
        if ligne.strip() == "---" and not dans_code:
            slides.append(cur); cur = []
        else:
            cur.append(ligne)
    slides.append(cur)
    return [s for s in slides if any(l.strip() for l in s)]

def parse(lignes):
    s = {"layout": "contenu", "titre": "", "colonnes": [[]], "notes": [], "images": []}
    dans_notes = dans_code = False
    for l in lignes:
        m = re.match(r"\s*<!--\s*layout:\s*([\w-]+)\s*-->", l)
        if m:
            s["layout"] = m.group(1); continue
        if dans_notes:
            s["notes"].append(l); continue
        if l.strip().startswith("```"):
            dans_code = not dans_code
            if dans_code:
                s["colonnes"][-1].append(("code_debut", 0, ""))
            continue
        if dans_code:
            s["colonnes"][-1].append(("code", 0, l)); continue
        if l.strip() == "Notes:":
            dans_notes = True; continue
        if l.startswith("# ") and not s["titre"]:
            s["titre"] = l[2:].strip(); continue
        if l.strip() == "|||":
            s["colonnes"].append([]); continue
        m = re.match(r"\s*!\[(.*?)\]\((.+?)\)", l)
        if m:
            s["images"].append((m.group(1), m.group(2))); continue
        m = re.match(r"^(\s*)[-*]\s+(.*)", l)
        if m:
            s["colonnes"][-1].append(("puce", len(m.group(1)) // 2, m.group(2))); continue
        if l.strip():
            s["colonnes"][-1].append(("texte", 0, l.strip()))
    return s

def sans_puce(p):
    pPr = p._p.get_or_add_pPr()
    for t in ("a:buNone", "a:buChar", "a:buAutoNum"):
        for el in pPr.findall(qn(t)):
            pPr.remove(el)
    pPr.insert(0, pPr.makeelement(qn("a:buNone"), {}))

def remplit(tf, elements, charte):
    tf.clear()
    premier = True
    pc = charte["pptx"].get("police_code")
    tc = charte["pptx"].get("taille_code_pt", 14)
    for genre, niveau, texte in elements:
        if genre == "code_debut":
            continue
        p = tf.paragraphs[0] if premier else tf.add_paragraph()
        premier = False
        if genre == "code":
            r = p.add_run(); r.text = texte if texte else " "
            if pc: r.font.name = pc
            r.font.size = Pt(tc)
            sans_puce(p)
            continue
        p.level = min(niveau, 4)
        if genre == "texte":
            sans_puce(p)
        for t, style in segments_inline(texte):
            r = p.add_run(); r.text = t
            if style == "gras": r.font.bold = True
            elif style == "italique": r.font.italic = True
            elif style == "code" and pc: r.font.name = pc

def controle(i, s, lim, alertes):
    puces = [e for c in s["colonnes"] for e in c if e[0] == "puce"]
    code = [e for c in s["colonnes"] for e in c if e[0] == "code"]
    mots = sum(len(e[2].split()) for c in s["colonnes"] for e in c if e[0] != "code")
    if len(puces) > lim.get("puces_max", 99):
        alertes.append(f"Diapo {i} : {len(puces)} puces (max {lim['puces_max']})")
    for e in puces:
        if len(e[2]) > lim.get("caracteres_par_puce", 999):
            alertes.append(f"Diapo {i} : puce trop longue ({len(e[2])} car.) « {e[2][:40]}… »")
    if len(code) > lim.get("lignes_code_max", 999):
        alertes.append(f"Diapo {i} : {len(code)} lignes de code (max {lim['lignes_code_max']})")
    if mots > lim.get("mots_max", 9999):
        alertes.append(f"Diapo {i} : {mots} mots (max {lim['mots_max']})")
    if not s["titre"]:
        alertes.append(f"Diapo {i} : pas de titre")
    if "[À VÉRIFIER]" in "\n".join(e[2] for c in s["colonnes"] for e in c) + s["titre"]:
        alertes.append(f"Diapo {i} : contient [À VÉRIFIER]")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slides"); ap.add_argument("--charte", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    charte = charge_charte(a.charte)
    cp = charte.get("pptx") or sys.exit("Erreur : la charte n'a pas de section pptx.")
    prs = Presentation(os.path.join(a.charte, cp["template"]))
    for sid in list(prs.slides._sldIdLst):          # retire les diapositives d'exemple du template
        prs.part.drop_rel(sid.rId); prs.slides._sldIdLst.remove(sid)
    par_nom = {l.name: l for m in prs.slide_masters for l in m.slide_layouts}
    base = os.path.dirname(os.path.abspath(a.slides))
    alertes = []
    for i, brut in enumerate(decoupe(open(a.slides, encoding="utf-8").read()), 1):
        s = parse(brut)
        nom = cp["layouts"].get(s["layout"])
        if not nom or nom not in par_nom:
            sys.exit(f"Erreur diapo {i} : layout logique '{s['layout']}' sans correspondance dans la charte.")
        slide = prs.slides.add_slide(par_nom[nom])
        if slide.shapes.title is not None:
            slide.shapes.title.text = s["titre"]
        phs = sorted((p for p in slide.placeholders if p.placeholder_format.type not in EXCLUS),
                     key=lambda p: p.placeholder_format.idx)
        photos = [p for p in phs if p.placeholder_format.type == PP_PLACEHOLDER.PICTURE]
        textes = [p for p in phs if p.placeholder_format.type != PP_PLACEHOLDER.PICTURE and p.has_text_frame]
        utilises = set()
        for col, ph in zip([c for c in s["colonnes"] if c], textes):
            remplit(ph.text_frame, col, charte); utilises.add(ph.placeholder_format.idx)
        if len([c for c in s["colonnes"] if c]) > len(textes):
            alertes.append(f"Diapo {i} : plus de colonnes de contenu que de zones dans la mise en page '{nom}'")
        for (legende, chemin) in s["images"]:
            chemin = chemin if os.path.isabs(chemin) else os.path.join(base, chemin)
            if not os.path.exists(chemin):
                alertes.append(f"Diapo {i} : image introuvable {chemin}"); continue
            if photos:
                ph = photos.pop(0); idx = ph.placeholder_format.idx
                ph.insert_picture(chemin); utilises.add(idx)
            else:
                libres = [p for p in textes if p.placeholder_format.idx not in utilises]
                zone = libres[0] if libres else None
                if zone is None:
                    alertes.append(f"Diapo {i} : pas de zone libre pour l'image {chemin}"); continue
                from PIL import Image
                w, h = Image.open(chemin).size
                ratio = min(zone.width / w, zone.height / h)
                pw, phh = int(w * ratio), int(h * ratio)
                slide.shapes.add_picture(chemin, zone.left + (zone.width - pw) // 2,
                                         zone.top + (zone.height - phh) // 2, pw, phh)
        for ph in list(slide.placeholders):          # pas de « Cliquez pour ajouter du texte »
            t = ph.placeholder_format.type
            if t in (PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE) and s["titre"]:
                continue
            if ph.placeholder_format.idx in utilises or t in (PP_PLACEHOLDER.SLIDE_NUMBER, PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.DATE):
                continue
            ph._element.getparent().remove(ph._element)
        notes = "\n".join(s["notes"]).strip()
        if notes:
            slide.notes_slide.notes_text_frame.text = notes
        elif s["layout"] not in ("titre", "section", "fin"):
            alertes.append(f"Diapo {i} : pas de notes orateur")
        controle(i, s, cp.get("limites", {}), alertes)
    prs.save(a.out)
    print(f"✔ {a.out} — {len(prs.slides)} diapositives")
    if alertes:
        print("\nAlertes :"); print("\n".join(f"- {x}" for x in alertes))
        sys.exit(2)

if __name__ == "__main__":
    main()
