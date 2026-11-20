---
name: branding-visuels-brou-paulin-xavier
description: Système de design et procédure de fabrication de tous les visuels (Facebook, Instagram, LinkedIn) de Brou Paulin-Xavier KADJO, Conseil en stratégie de marque. À appliquer à chaque visuel, sans qu'on ait à le redemander. Fusionne ui-ux-pro-max, elite-ux-art-direction et skill-creator.
---

# Visuels de marque : Brou Paulin-Xavier KADJO

## Concept en une phrase
Minimalisme éditorial premium : un message par visuel, une hiérarchie typographique tranchée, beaucoup d'espace blanc, des icônes et des illustrations géométriques qui servent le sens, jamais le décor.

## Jetons de design (valeurs mesurées sur le visuel de référence)
- Couleurs : vert profond #0C4830 (titres, fonds inversés) · vert doux #4C7C68 (accroche, accents) · anthracite #242424 (texte) · blanc #FFFFFF · gris très clair #F2F2EF (panneaux « avant ») · sur fond vert : vert clair #A9C7B8 et #E9F1EC.
- Typographie : Inter (graisses 400, 500, 600, 900). Titres en capitales Inter Black, interlettrage serré, centrés. Accroche en capitales espacées (26 px, vert doux). Texte courant Inter 400 (34 px, interligne 1,5). Signature en capitales espacées, 19 px, centrée en pied à y = 1277.
- Signature : « BROU PAULIN-XAVIER KADJO | CONSEIL EN STRATÉGIE DE MARQUE ». Pas de logo.
- Formats : 1080 × 1350 (4:5) pour publications, carrousels, documents LinkedIn ; 1080 × 1920 pour les Reels. Marges 80 px. Coins arrondis 24 px.
- Seul glyphe interdit : le sous-ensemble Latin d'Inter n'a pas ≠ → ✓. Les remplacer par des mots ou par une icône dessinée.

## Règles qualité (ordre de priorité, issues des trois skills)
1. Accessibilité : contraste du texte ≥ 4,5:1 ; texte jamais sous 26 px ; texte alternatif obligatoire sur chaque image envoyée à Buffer.
2. Un seul message, un seul point focal. Titre ≤ 8 mots. Test des 3 secondes : on doit comprendre sans lire la légende.
3. Icônes : trait arrondi unique (grille 24, trait 1,9), jamais d'emoji, mêmes couleurs que la marque, pastille ronde. Une icône doit porter un sens (œil = visibilité, cible = clients, calques = cohérence, horloge = temps, bulle = parole, utilisateur = expérience, loupe = diagnostic).
4. Illustrations : compositions géométriques à deux termes (« connu → choisi », « ce qu'on dit → ce qu'on vit »), deux couleurs maximum, pas de dégradé, pas d'ornement sans fonction.
5. Photos : lumière naturelle, tons chauds et neutres, expressions sincères, coins arrondis. Jamais de portrait IA pour représenter Brou Paulin-Xavier KADJO. Signaler les images IA réalistes selon les règles de chaque plateforme.
6. Pas de statistique, témoignage, logo client ou preuve inventés. Les exemples sont marqués « fictif ».
7. Cohérence : mêmes gabarits, mêmes marges, même signature sur tout le calendrier. Alterner fond blanc et fond vert pour rythmer sans changer de langage.

## Gabarits (fichier design.py et render.py)
- `typo(...)` : gabarit B (blanc) et B2 (vert inversé) : accroche, titre, texte.
- `avant_apres(...)` : gabarit E, deux panneaux empilés.
- `scene(...)` : deux icônes face à face avec légendes (illustration conceptuelle).
- `icon_list(...)` : liste de choix ou de points, une icône par ligne.
- `cover_icon(...)` : couverture ou slide de carrousel avec grosse icône.
- `make_photo(...)` (visual2.py) : gabarit A avec photo.
- 13 icônes : eye, check, target, bubble, clock, layers, search, user, arrow, x, pencil, mark, sparkle. Ajouter une icône = ajouter ses primitives dans `ICONS`.

## Procédure à chaque visuel
1. Lire le brief de la ligne du calendrier (sujet, titre, texte secondaire, gabarit).
2. Choisir le gabarit qui porte le mieux l'idée. Privilégier `scene` et `icon_list` quand le sujet oppose deux notions ou énumère des choix.
3. Rendre, puis REGARDER l'image (planche de contrôle). Corriger les retours à la ligne, les chevauchements, l'équilibre vertical.
4. Envoyer dans le dépôt GitHub public `PaulinXavier123/visuels-marque` (dossier `jNN/`), vérifier que l'adresse raw.githubusercontent.com répond 200 en image/jpeg ou png.
5. Joindre à la publication Buffer avec texte alternatif. Instagram : JPEG.

## Reconstruire l'environnement (le disque de travail est effacé entre deux conversations)
1. Récupérer les fichiers du dossier `outils/` du dépôt (raw.githubusercontent.com/PaulinXavier123/visuels-marque/main/outils/...) et les placer dans /home/claude/viz/.
2. Polices : `npm pack @fontsource/inter`, extraire `package/files/inter-latin-{400,500,600,700,900}-normal.woff`, convertir en .ttf avec fontTools (`TTFont(...).flavor = None`) vers /home/claude/viz/fonts/Inter-<graisse>.ttf.
3. Dépendances : Pillow, numpy, fontTools.

## Limites connues
- Aucune génération de photo ni de vidéo dans cet environnement ; le jeu de données de ui-ux-pro-max (icônes, palettes, associations de polices) n'y est pas installé : seules ses règles écrites sont appliquées.
- Buffer : 10 publications programmées au plus sur le compte actuel.
