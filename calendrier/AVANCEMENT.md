# Avancement du calendrier (mis à jour le 27 novembre 2026, 8 h 20 GMT)

Rythme : 2 publications par jour et par réseau, à 8 h et 14 h GMT, 7 jours sur 7, sans décalage. Ordre des créneaux : J2 à J9, J11 à J16, J10 (Black Friday, le 27/11 à 8 h), puis J17 à J30.

| Jours | État |
|---|---|
| J1 | Publié le 19/11 (LinkedIn publié deux fois : 10 h 13 et 21 h 55 ; Facebook et Instagram à 22 h 05) |
| J2 à J9 | Publiés (J2, J3 version sobre ; J4 à J9 visuels v2) |
| J11 | Publié le 24/11 à 8 h (texte Facebook adapté : « Question du jour ») |
| J12 | Publié le 24/11 à 14 h (le Reel Instagram est remplacé par un carrousel de 5 slides) |
| J13 | Publié le 25/11 à 8 h |
| J14 | Publié le 25/11 à 14 h |
| J15 | Publié le 26/11 à 8 h (LinkedIn en texte seul) |
| J16 | Publié le 26/11 à 14 h |
| J10 | Black Friday : le 27/11 à 8 h. Visuels v2 prêts dans j10v2 |
| J17 | Programmé le 27/11 à 14 h |
| J18 | Programmé le 28/11 à 8 h |
| J19 | Programmé le 28/11 à 14 h (texte Facebook adapté : « Depuis une dizaine de jours… Une question pour faire le point ») |
| J20 à J30 | Textes dans posts.json (J20 le 29/11 à 8 h, J21 le 29/11 à 14 h, etc.) ; visuels à produire avec outils/ (design.py : scene, icon_list, icon_list_compact, cover_icon ; render.py : typo, avant_apres). Éviter les glyphes ≠ → ✓ dans les visuels |

## Textes à adapter selon le jour réel de publication
- J19 Facebook : « Une question dominicale » (à reformuler si le jour n'est pas un dimanche).
- J10 (Black Friday) : le texte dit « aujourd'hui » ; à publier uniquement le 27/11.

## Reprise
- Textes finaux : `calendrier/posts.json` (clé `texte_final`, hashtags inclus). Les textes de J11 Facebook et J12 Instagram publiés sont ceux de la version adaptée ci-dessus.
- Identifiants Buffer : organisation 670c0b83daa6d3430dc5eced · LinkedIn 6afdad98ece6dfde5f0b437c · Facebook 6afda1dbece6dfde5f0aad45 · Instagram 6afdae87ece6dfde5f0b4b73.
- Buffer : 10 publications programmées au plus ; créer avec `customScheduled` et `dueAt` en UTC (= GMT). Images par adresse raw.githubusercontent.com du dépôt, avec texte alternatif. Ne jamais publier à d'autres heures que 8 h et 14 h.
- Visuels : voir `outils/SKILL.md`. Vérifier d'abord l'état de la file avec list_posts avant de publier, pour éviter les doublons.
