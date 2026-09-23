# Finding and embedding free photos

## Rules
- Only free-to-use photos: public domain, CC0, CC BY, CC BY-SA. No NC or ND licenses.
- **Every picture lives inside the HTML** as base64. No image links. The page must work offline.
- A credit line under each photo: author, license, source (file name).
- Photos around 500 to 700 px wide, JPEG quality about 70. Keep the whole HTML under about 8 MB (the build fails above 8 MB).
- Look at each photo before you use it (Read tool). Reject blurry ones, big watermarks or text, and the wrong object.
- If no good free photo exists, **draw the part as an SVG** instead. Never leave an empty box or a link.

## Wikimedia Commons: what works from the cloud container
- The API rate-limits hard (HTTP 429). Send a User-Agent, wait 3 to 5 s between calls, wait 20 s and retry after a 429. Expect this search to be slow.
  `curl -sS -A "SessionLessonBot/1.0 (https://github.com/adeoo)" "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=QUERY&srnamespace=6&format=json&srlimit=20"`
- Category listing: `...&list=categorymembers&cmtitle=Category:NAME&cmtype=file&cmlimit=50`.
- License and author: `...&titles=File:NAME&prop=imageinfo&iiprop=extmetadata|size|url` (read LicenseShortName, Artist).
- Download a thumbnail: `curl -sSL -A "..." "https://commons.wikimedia.org/wiki/Special:FilePath/NAME?width=700"`. Check it is really a JPEG (`file x.jpg`), because a 429 saves an HTML page instead.
- Pixabay and Pexels block the container (403).

## Use parallel research agents, with a time limit
Send one agent per picture group. Tell each one: the list of items, the rules above, to save and view every candidate, and to report file name, local path, author, license and page URL. **Give them a time limit (about 20 minutes)** and ask them to report their best picks when time is up. In Session 2 they ran 45 minutes because of the rate limit.

## Already found (Session 2), reuse freely
| Subject | Commons file | Author, license |
|---|---|---|
| Open deep groove ball bearing | Ball bearing.jpg | Solaris2006, CC BY-SA 3.0 |
| Split pillow block cut open | Pillow block NSK SAFD522.jpg | SamuelFreli, CC BY-SA 3.0 |
| Worn shaft seat next to bearing | Albero ruota su cuscinetto.jpg | A7N8X, CC BY-SA 4.0 |
| Twist drill | Twist Drill Bit (6954956907).jpg | andersen_mrjh, CC BY-SA 2.0 |
| Reamers, straight flutes | Rozwiertak pilot.jpg | Krakuspm, CC BY-SA 3.0 |
| Outside micrometer | Mahr Micromar 40A 0–25 mm Micrometer.jpg | Lucasbosch, CC BY-SA 3.0 |
| 3-point inside micrometer | 3 point micrometer.jpg | Rrudzik, CC0 |
| Hardened dowel pins | Steel-Dowel-Pins.jpg | David J. Fred, CC BY-SA 2.5 |
| Bronze bushing | Boccola Minarelli AM345.jpg | A7N8X, CC BY-SA 4.0 |
| Sintered bronze bushes, with mm scale | Lagerbuchsen.jpg | Ulfbastel, public domain |

Not found on Commons (draw them): a cut-open ball bearing alone, a UCP pillow block unit, a diamond (relieved) pin, a linear ball bushing on a shaft, a clean technical drawing with a title block.
