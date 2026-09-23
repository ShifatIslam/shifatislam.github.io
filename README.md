# Shifat Islam — academic portfolio

A complete static website for https://shifatislam.github.io/, redesigned around the structure and restrained academic style of the supplied Tashreef Muhammad reference.

## Preview

Extract this ZIP and open `index.html` in a browser. Keep `style.css`, `script.js`, `data/`, and `assets/` alongside it. No server, npm, framework, API key, or installation is required. All main content is available without JavaScript.

## Final CV and Scholar update

- Every Google Scholar link uses `https://scholar.google.com/citations?user=xO32H0oAAAAJ&hl=en` and opens a new tab with `noopener noreferrer`.
- Automated Scholar retrieval still returns HTTP 403. Links are validated in the generated HTML; live profile loading and yearly metrics cannot be guaranteed from this environment.
- A.R.i.S.E leadership: **2024–Present**, using the reference start year as requested. Research Mentor & Member since **January 2024**, from your CV.
- UIU Research Engineer: **September 2023–Present**.
- BUET PG Research Assistant: **July 2022–August 2023**.
- AUST UG Research Student: **January 2019–December 2021**.
- BUET MSc: **April 2022–Present**, thesis defence pending.
- AUST BSc: **April 2017–January 2022**.
- Consolidated the duplicate postgraduate-research entry into the CV's BUET assistantship. Education remains separately dated.
- Citation overview shows **80+**, updated directly by the user; no explanatory note is displayed below the count. The annual chart still awaits verified year-by-year figures.
- Mentorship count is **20+**, updated directly by the user because the CV was backdated.
- VGDNet is now listed as **Submitted, QPAIN 2026**, matching the CV. Your requested published total remains 12; the supplied bibliography still has 11 published entries plus that submitted manuscript.

## Typography and mentorship edits

- Newsreader for headings and IBM Plex Sans for interface/body text, using the exact Google Fonts families and weights from the reference. Internet access is required to load these fonts; system fallbacks remain available offline.
- Header navigation includes both Mentorship and Experience.
- Research and mentorship body copy contains no bold emphasis.
- Each mentorship project is condensed to two bullets while retaining the key scale, scope and future target.
- Experience and education now use a vertical timeline. The six consolidated date ranges are populated from the CV/reference; edit `from` and `to` in `data/content.json` and rebuild. Use `Present` for an ongoing role/degree. No dates have been guessed.
- Published-paper total is 12, per your correction, stored in `profile.publishedCount` independently of the displayed paper list.
- A total-citation metric is beside the paper total. It uses the user-reported 80+ lower bound until a current Scholar total is provided; add an exact total to `data/metrics.json`. This total displays even if annual counts are still unavailable.
- The current list contains 11 published entries and VGDNet labeled Submitted (2026), as in the CV. Please confirm whether VGDNet is now published or provide the missing twelfth published paper so the detailed list can be reconciled.

## Earlier edits

- All five hero links use matching boxed buttons: Get in touch, Google Scholar, GitHub, ORCID, and LinkedIn.
- Portrait enlarged with responsive sizing.
- Section title changed to Research; all three topic descriptions and bullet lists use your supplied wording; body emphasis was subsequently removed.
- All section and topic numbering removed. Quantities, publication years, and research metrics remain.
- Added all five Research Mentorship projects, subsequently condensed at your request; the spice VQA figure remains a target, not a completed result.
- Updated meta description, hero summary and contact paragraph exactly as requested. Open Graph title remains Shifat Islam | Research Engineer.
- Footer includes A.R.I.S.E, LinkedIn and Google Scholar, with ORCID removed from the footer.
- Section order: Research → Publications → Code & Data → Open Datasets → Applied Projects → Research Mentorship → Grants → Experience → Education → Awards → Skills → Contact.

Research, mentorship, hero summary, meta description and contact copy can all be maintained in `data/content.json`.

## What changed

- Large **Shifat Islam** heading, with **Research Engineer** immediately below it.
- Combined career positioning: **Language, Vision & Healthcare AI**.
- Prominent **Seeking PhD opportunities** statement, without an invented intake or funding requirement.
- Three topic-based research areas: language models/low-resource NLP, multimodal learning/computer vision, and healthcare/public-health AI.
- Six selected papers, with six additional entries behind **View all 12 publications**. Selection reflects relevance, authorship, and coverage of your research areas; it is not a citation ranking.
- Code cards drawn from public repositories; three versioned datasets checked against ORCID.
- REG-NER grant with your requested **Research Mentor** designation; publication support from your original UIU profile retained.
- **Co-Founder & Deputy Director, A.R.i.S.E** added to your existing experience. No Treasurer designation or financial responsibilities included.
- Education, awards, research toolkit, and a final **Get in touch** section.

## Citation data: the same method as Tashreef's website

The reference site's `/Data/metrics.json` explicitly says its metrics need manual updating. Its JavaScript reads that JSON and draws a citation chart; it does not fetch live Scholar counts.

This portfolio now follows that method:

1. Open your Google Scholar profile and note the total citations, h-index, i10-index, and exact annual citation counts.
2. Edit `data/metrics.json` in your GitHub repository.
3. Set `asOf` to the date you checked, in YYYY-MM-DD format.
4. Fill in `scholar.citations`, `scholar.hIndex`, and `scholar.i10Index`. Leave unknown figures as `null`.
5. Fill `citationsByYear` with objects containing `year` and `count`; add `partial: true` for the current incomplete year. Do not infer yearly counts from the total.
6. Commit the change and let your existing GitHub Pages deployment finish. The page reads the JSON file and updates its total and bar-and-line chart, with snapshot date and accessible yearly-count table.

No API key, subscription, scraping script, or scheduled workflow is needed. The figures remain unchanged until you update the file.

Your exact Scholar figures are still unavailable. The JSON is deliberately unpopulated, so the page retains the user-reported 80+ total and the link to Scholar. Supply a screenshot of your own annual chart and metrics to populate it accurately. Do not use Tashreef's counts.

For a downloaded offline preview, run `python build.py` after changing `data/metrics.json`; this embeds the latest snapshot in `index.html`. Hosted pages read the JSON directly, so updating only the JSON is sufficient after deployment.

## Upload to your existing GitHub Pages repository

1. Sign in and open https://github.com/ShifatIslam/shifatislam.github.io.
2. Back up the current repository via **Code → Download ZIP** and record the current Pages publishing settings.
3. Create a `portfolio-redesign` branch from `main`.
4. Use **Add file → Upload files**. Upload `index.html`, `style.css`, `script.js`, the entire `data` folder, and the entire `assets` folder to the repository ROOT. Do not upload the ZIP itself or place the website inside an extra parent folder.
5. Add the empty `.nojekyll` file at the repository root. If hidden on your computer, create it using **Add file → Create new file**. You may also upload `build.py`, `README.md`, and `SOURCES.md` for future maintenance.
6. Review a pull request from `portfolio-redesign` into `main`, then merge when ready.
7. Under **Settings → Pages → Build and deployment**, select **Deploy from a branch**, **main**, **/(root)**, then **Save**. If an old custom Actions workflow deploys a different build, review and disable that deployment workflow before switching so it does not overwrite the static version.
8. Wait for the Pages deployment to succeed in the **Actions** tab, then visit https://shifatislam.github.io/. Refresh without cache if necessary.

Official GitHub instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

To roll back, revert the merged redesign pull request and restore your recorded Pages settings if changed.

## Edit the website later

The served website is `index.html`. You can edit it directly, but a later rebuild will overwrite those direct changes.

For repeatable editing:

1. Edit the organized fields in `data/content.json`.
2. Run `python build.py` from this folder (Python 3, standard library only).
3. Commit the updated `data/content.json` and generated `index.html`.

Set `selected` to `true` on the six papers you want featured; set the others to `false`. Array order controls display order. Edit colors, typography and spacing in `style.css`. Replace `assets/profile.jpg` to update your portrait.

Grant text and the hero/contact layout are in `build.py`. Citation data is stored in `data/metrics.json`. The builder embeds a copy for offline previews but does not modify the source JSON.

The supplied CV was used as a source; the complete PDF has not been published or linked on the website. To include one, add a PDF to `assets/` and link it in the hero. No PhD intake, employment dates, degree completion dates, CGPA or memberships were invented.

## Verification and review

- Checked valid nesting, unique IDs, local asset existence, and every internal anchor.
- Checked 12 paper entries, exactly six selected, all three datasets, and the absence of a Treasurer role.
- JavaScript syntax checked; responsive rules cover desktop, tablet and mobile; native HTML disclosure handles the additional publications.
- The browser could inspect the live design reference but its security policy disallowed opening local files. Therefore the finished layout has not been visually verified in that browser. Preview it on desktop and mobile before publishing.
- Employer was intentionally omitted from the name block, per your choice. UIU/BUET experience and dates now follow the supplied CV.
- VGDNet uses the Submitted, QPAIN 2026 status reported in the CV. Please confirm whether it has since been published.
- The Bangla healthcare paraphrasing author list remains as on your original portfolio; A.R.i.S.E lists one author differently (Azizul Hakim versus Azizul Fayaz). Check against the final publisher record before changing that author name.

See `SOURCES.md` for content provenance and confirmed publication updates. No changes have been pushed to your GitHub repository.
