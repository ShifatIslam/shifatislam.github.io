# Sources and editorial decisions

Prepared 23 September 2026. Source statements are kept separate from user-confirmed roles and editorial descriptions.

## Your website and GitHub

- https://shifatislam.github.io/ — original biography, all 12 paper entries, education, experience, skills, awards, grants and mentorship count. Downloaded deployed HTML and CSS; this was not a full repository audit.
- https://api.github.com/users/ShifatIslam/repos?per_page=100 — public repository inventory. Only relevant original repositories and the explicitly linked collaborative ANCHOLIK resource were included; tutorial forks are not presented as original research.
- https://github.com/ShifatIslam/ShifatIslam — profile README, supporting language/vision/healthcare research positioning.
- https://github.com/ShifatIslam/BLP25-Task-1
- https://github.com/ShifatIslam/BLP-Task-2
- https://github.com/ShifatIslam/Sushastho-chatbot
- https://github.com/ShifatIslam/Adolscent-Bot-for-SRMH-
- https://github.com/ShifatIslam/Intent_Based_Search_Engine

## ORCID datasets

- https://orcid.org/0009-0008-8433-0264
- Public API: https://pub.orcid.org/v3.0/0009-0008-8433-0264/works

The ORCID record identifies these datasets with their versioned DOIs:

- BengaliVQA (2025): https://doi.org/10.17632/y9fw6k37n9.1
- ANCHOLIK-NER (2025): https://doi.org/10.17632/gbkszkt8z3.1
- PerilPix (2025): https://doi.org/10.17632/3rwjgbj4k8.1

ORCID is used for works and datasets; code repositories come from GitHub and explicit paper/project links. Duplicate preprint and conference records in ORCID were not counted as additional papers.

## Confirmed updates

- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0342786 — ANCHOLIK-NER published 25 February 2026 in PLOS ONE. Changed the original under-review entry to Published, 2026. The publisher lists Shifat Islam as a coauthor and reports funding from SEU's Institute of Research and Training, grant SEU/IRT/RG/2025/01/09 to M. A. Hoque.
- https://ariserl.org/people/shifat-islam — confirms Deputy Director and links the REG-NER project.
- https://ariserl.org/projects/reg-ner — confirms project funding through IRT, SEU, and Shifat Islam's involvement.
- https://ariserl.org/publications/comparative-study-of-llms-and-transformers-for-bangla-healthcare-paraphrasing — supplies DOI 10.1109/ICCIT68739.2025.11491250 for the existing ICCIT 2025 paper. The original author list is retained pending resolution of a discrepancy noted in README.

## Reference and user instructions

- https://tashreefmuhammad.github.io/ — principal design reference: large name, concise designation, right-side metrics panel, topic-based research, selected publications, research artifacts, grants, and contact.
- https://tashreefmuhammad.github.io/Data/cv.json — REG-NER project and institutional funder. His Co-Investigator designation, unrelated employment, financial duties, dates and educational results were not copied to Shifat's profile.
- https://tashreefmuhammad.github.io/Data/publications.json — explicit collaborative ANCHOLIK-NER code link.
- User confirms Co-Founder & Deputy Director and requests Research Mentor for REG-NER. Co-founder and mentor titles are user-supplied; Deputy Director has additional public corroboration.
- User selects Research Engineer without employer below the name and asks for a common research name. “Language, Vision & Healthcare AI” is editorial synthesis, not a degree or formal appointment.
- The six featured papers are selected for research fit and authorship, not ranked by unverifiable citation totals.

## Still unavailable

- https://scholar.google.com/citations?user=xO32H0oAAAAJ&hl=en — access returned rate-limit/forbidden responses; exact annual citations, current total, h-index, and i10-index remain unverified. `data/citations.js` deliberately contains null/empty values, with a functioning renderer ready for verified data.

No grant amounts, personal funding receipts, employment dates, degree completion dates, CV, or PhD intake were inferred. The main page does not describe the REG-NER award as a personal grant to Shifat.

## User-supplied revision

The research theme text, hero summary, meta description, contact paragraph, and all five mentorship project descriptions and quantitative details were supplied directly by the user. They are not presented as newly verified external claims. Approximate image/question counts and the targeted 100,000 spice QA pairs retain their original qualifiers. No links, publications, dates or completed outputs were invented for the mentorship projects.

## Latest user correction

Published-paper total is now 12, explicitly supplied by the user. The detailed paper list still requires reconciliation: VGDNet was previously reported as under review. No paper status has been silently changed. Experience/education dates and total citations remain pending user input. Fonts match the previously retrieved reference stylesheet (Newsreader and IBM Plex Sans). Mentorship descriptions are condensed from the user-provided descriptions while retaining counts and target qualifiers.

## CV-based final revision

Shifat_CV.pdf, supplied by the user, is the authoritative source for UIU, BUET and AUST dates and role descriptions, MSc thesis-defence status, the 10+ mentee count, and the reported citation lower bound of more than 60. A.R.i.S.E co-founder/deputy-director start year 2024 follows the reference CV at the user's explicit request; the user's own CV gives January 2024 for Research Mentor & Member. Duplicate postgraduate research was consolidated with PG Research Assistant rather than assigned speculative dates. VGDNet is submitted to QPAIN 2026 according to this CV, not a confirmed published twelfth paper. Personal phone, street address, references' contact information, and the full CV PDF were not added to the public website.

All generated Scholar links were parsed and checked for the exact requested URL and new-tab attributes. The remote Scholar page returned HTTP 403 on this attempt. No live-loading or citation-scraping success is claimed.

## Reference citation implementation inspected

Fetched https://tashreefmuhammad.github.io/Data/metrics.json and https://tashreefmuhammad.github.io/JS/main.js. The JSON comment explicitly states the metrics require manual updating. JavaScript loads that local JSON and renders bars plus a line. This portfolio now uses the same local-JSON snapshot pattern through data/metrics.json, with an embedded offline fallback. Reference-author numbers were not copied. No live Scholar feed or third-party API was added.

## Latest user-provided counts

The user corrected citations to 80+ and undergraduate mentees to 20+, explaining that the CV is backdated. These supersede its older figures. The explanatory note below the citation count was removed at the user’s request. No live update or exact annual citation counts are implied.
