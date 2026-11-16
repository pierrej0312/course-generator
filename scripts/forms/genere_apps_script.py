#!/usr/bin/env python3
"""Génère un script Google Apps Script qui crée un Google Form (quiz ou questionnaire)
à partir d'un fichier JSON d'évaluation (format : templates/evaluation-forms.json).

Usage : python3 genere_apps_script.py evaluation.json > creer_formulaire.gs

API utilisée (Apps Script, service Forms) : FormApp.create(title, isPublished), Form.setIsQuiz,
addMultipleChoiceItem, addCheckboxItem, addParagraphTextItem, addScaleItem,
createChoice(value, isCorrect), setPoints, setFeedbackForCorrect/Incorrect,
FormApp.createFeedback().setText().build(), getPublishedUrl, getEditUrl.
"""
import json, sys

TYPES = {"choix_unique", "choix_multiple", "texte_long", "echelle"}

def js(s):
    return json.dumps(s if s is not None else "", ensure_ascii=False)

def erreur(msg):
    sys.exit(f"Erreur : {msg}")

def valide(d):
    if not d.get("titre"):
        erreur("champ 'titre' manquant")
    qs = d.get("questions") or []
    if not qs:
        erreur("aucune question")
    for i, q in enumerate(qs, 1):
        t = q.get("type")
        if t not in TYPES:
            erreur(f"question {i} : type '{t}' inconnu ({', '.join(sorted(TYPES))})")
        if not q.get("titre"):
            erreur(f"question {i} : titre manquant")
        if t in ("choix_unique", "choix_multiple"):
            ch = q.get("choix") or []
            if len(ch) < 2:
                erreur(f"question {i} : au moins 2 choix")
            nb_ok = sum(1 for c in ch if c.get("correct"))
            if d.get("quiz"):
                if t == "choix_unique" and nb_ok != 1:
                    erreur(f"question {i} : un choix unique doit avoir exactement 1 bonne réponse (trouvé {nb_ok})")
                if t == "choix_multiple" and nb_ok < 1:
                    erreur(f"question {i} : au moins 1 bonne réponse")

def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    d = json.load(open(sys.argv[1], encoding="utf-8"))
    valide(d)
    quiz = bool(d.get("quiz"))
    L = []
    L.append("function creerFormulaire() {")
    L.append(f"  var form = FormApp.create({js(d['titre'])}, true);")
    if d.get("description"):
        L.append(f"  form.setDescription({js(d['description'])});")
    if quiz:
        L.append("  form.setIsQuiz(true);")
    L.append("  var item;")
    for q in d["questions"]:
        t = q["type"]
        L.append("")
        if t in ("choix_unique", "choix_multiple"):
            meth = "addMultipleChoiceItem" if t == "choix_unique" else "addCheckboxItem"
            L.append(f"  item = form.{meth}().setTitle({js(q['titre'])});")
            choix = ", ".join(
                f"item.createChoice({js(c['texte'])}, {'true' if (quiz and c.get('correct')) else 'false'})"
                for c in q["choix"])
            L.append(f"  item.setChoices([{choix}]);")
            if quiz:
                L.append(f"  item.setPoints({int(q.get('points', 1))});")
                for cle, meth_fb in (("feedback_correct", "setFeedbackForCorrect"),
                                     ("feedback_incorrect", "setFeedbackForIncorrect")):
                    if q.get(cle):
                        L.append(f"  item.{meth_fb}(FormApp.createFeedback().setText({js(q[cle])}).build());")
        elif t == "texte_long":
            L.append(f"  item = form.addParagraphTextItem().setTitle({js(q['titre'])});")
        elif t == "echelle":
            L.append(f"  item = form.addScaleItem().setTitle({js(q['titre'])})"
                     f".setBounds({int(q.get('min', 1))}, {int(q.get('max', 5))});")
            if q.get("label_min") or q.get("label_max"):
                L.append(f"  item.setLabels({js(q.get('label_min'))}, {js(q.get('label_max'))});")
        if q.get("aide"):
            L.append(f"  item.setHelpText({js(q['aide'])});")
        L.append(f"  item.setRequired({'true' if q.get('obligatoire', True) else 'false'});")
    L.append("")
    L.append("  Logger.log('Lien à envoyer aux apprenants : ' + form.getPublishedUrl());")
    L.append("  Logger.log('Lien d\\'édition (formateur) : ' + form.getEditUrl());")
    L.append("}")
    print("\n".join(L))

if __name__ == "__main__":
    main()
