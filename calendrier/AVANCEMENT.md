# Avancement du calendrier (mis à jour le 24 novembre 2026, 11 h 30 GMT)

Rythme : 2 publications par jour et par réseau, à 8 h et 14 h GMT, 7 jours sur 7, sans décalage. Ordre des créneaux : J2 à J9, J11 à J16, J10 (Black Friday, le 27/11 à 8 h), puis J17 à J30.

| Jours | État |
|---|---|
| J1 | Publié le 19/11 (LinkedIn publié deux fois : 10 h 13 et 21 h 55 ; Facebook et Instagram à 22 h 05) |
| J2 à J9 | Publiés (J2, J3 version sobre ; J4 à J9 visuels v2) |
| J11 | Publié le 24/11 à 8 h (texte Facebook adapté : « Question du jour ») |
| J12 | Programmé le 24/11 à 14 h (le Reel Instagram est remplacé par un carrousel de 5 slides) |
| J13 | Programmé le 25/11 à 8 h |
| J14 | Programmé le 25/11 à 14 h |
| J15, J16 | À produire (visuels) puis programmer : J15 le 26/11 à 8 h, J16 le 26/11 à 14 h |
| J10 | Black Friday : le 27/11 à 8 h. Visuels v2 prêts dans j10v2 |
| J17 à J30 | Textes dans posts.json ; visuels à produire avec outils/ |

## Textes à adapter selon le jour réel de publication
- J19 Facebook : « Une question dominicale » (à reformuler si le jour n'est pas un dimanche).
- J10 (Black Friday) : le texte dit « aujourd'hui » ; à publier uniquement le 27/11.

## Reprise
- Textes finaux : `calendrier/posts.json` (clé `texte_final`, hashtags inclus). Les textes de J11 Facebook et J12 Instagram publiés sont ceux de la version adaptée ci-dessus.
- Identifiants Buffer : organisation 670c0b83daa6d3430dc5eced · LinkedIn 6afdad98ece6dfde5f0b437c · Facebook 6afda1dbece6dfde5f0aad45 · Instagram 6afdae87ece6dfde5f0b4b73.
- Buffer : 10 publications programmées au plus ; créer avec `customScheduled` et `dueAt` en UTC (= GMT). Images par adresse raw.githubusercontent.com du dépôt, avec texte alternatif. Ne jamais publier à d'autres heures que 8 h et 14 h.
- Visuels : voir `outils/SKILL.md`. Vérifier d'abord l'état de la file avec list_posts avant de publier, pour éviter les doublons.
