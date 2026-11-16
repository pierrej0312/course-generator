---
name: profil-formateur
description: Crée ou met à jour le profil d'un formateur (ton, vocabulaire, personnalité, charte par défaut) à partir d'un entretien et de ses anciens supports. À lancer pour chaque nouvel utilisateur du dépôt, ou quand un formateur veut ajuster sa voix.
---
# Profil formateur

## Créer
1. Demander nom et identifiant (kebab-case). Si `formateurs/<identifiant>/` existe, passer en mode mise à jour.
2. Copier `formateurs/_modele/` vers `formateurs/<identifiant>/`.
3. Inviter le formateur à déposer 2 à 5 anciens supports dans `formateurs/<identifiant>/exemples/` (pptx, pdf, docx, md, transcriptions de cours enregistrés…).
4. **Entretien** — poser les questions de `profil.md` et `voix.md` par petits groupes (3-4 questions max à la fois). Ne jamais remplir une réponse à la place du formateur.
5. **Analyse des supports** — lire chaque exemple et relever :
   - tutoiement/vouvoiement, longueur des phrases, densité des slides ;
   - expressions et tournures récurrentes (citer le passage exact et le fichier) ;
   - analogies, structure type d'une séquence ;
   - termes techniques employés de façon constante.
   Tout est marqué « (observé dans `exemples/<fichier>`) ». Une seule occurrence n'est pas une habitude : ne retenir que ce qui revient.
6. **Validation** — présenter au formateur ce qui a été déduit des supports ; il confirme, corrige ou rejette chaque point. Seuls les points confirmés sont enregistrés.
7. Remplir `profil.md`, `voix.md`, `lexique.md` et y copier 2-3 extraits réels représentatifs.
8. Demander la charte par défaut ; si elle n'existe pas dans `chartes/`, proposer d'en créer une à partir de `chartes/_modele/`.
9. **Test** — rédiger une slide et un court énoncé d'atelier sur un sujet au choix du formateur, dans sa voix ; lui demander si « ça sonne comme lui ». Ajuster le profil selon ses retours.

## Mettre à jour
Lire le profil existant, demander ce qui ne sonne pas juste (ou analyser de nouveaux exemples), proposer des modifications précises, enregistrer après validation.

## Règles
- Ne jamais copier la voix d'un autre profil comme point de départ.
- Ne rien inventer sur la personnalité : déclaré ou observé, sinon vide.
