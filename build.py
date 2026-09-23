"""Rebuild the static website: python build.py (Python standard library only)."""
import json
import re
from html import escape as esc
from pathlib import Path
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'data/content.json').read_text(encoding='utf-8'));P=D['profile']
METRICS=json.dumps(json.loads((ROOT/'data/metrics.json').read_text(encoding='utf-8')),ensure_ascii=True).replace('<',r'\u003c')
def e(v):return esc(str(v),quote=True)
def rich(v):return re.sub(r"\*\*(.+?)\*\*", lambda m: "<strong>"+m.group(1)+"</strong>", e(v))
def link(label,url,cls=''):
 extra=' target="_blank" rel="noopener noreferrer"' if url.startswith('https://scholar.google.com/') else ''
 return f'<a class="{cls}" href="{e(url)}"{extra}>{e(label)}</a>' 
def links(items):return '<div class="resource-links">'+''.join(link(x['label'],x['url']) for x in items)+'</div>'
def head(title,note=''):
 return f'<header class="section-heading"><div><h2>{e(title)}</h2></div>'+ (f'<p>{e(note)}</p>' if note else '')+'</header>'
def section(id,title,body,note=''):
 return f'<section class="section" id="{id}" aria-label="{e(title)}">{head(title,note)}{body}</section>'
def publication(p):
 authors=e(p['authors']).replace('Shifat Islam','<strong>Shifat Islam</strong>')
 status=f'<span class="status-review">{e(p["status"])}</span>' if p['status']!='Published' else f'<span>{e(p["type"])}</span>'
 return f'''<article class="publication" id="{e(p['id'])}">
<div class="publication-year">{p['year']}<span>{e(p['type'])}</span></div>
<div><h3>{e(p['title'])}</h3><p class="authors">{authors}</p><p class="venue">{e(p['venue'])}</p>
<div class="publication-footer"><div class="tags"><span class="topic">{e(p['topic'])}</span>{status}</div>{links(p['links'])}</div></div></article>'''
def card(x):
 return f'<article class="resource-card"><p class="eyebrow">{e(x["subtitle"])}</p><h3>{e(x["title"])}</h3><p>{e(x["description"])}</p><ul class="plain-tags">'+''.join(f'<li>{e(t)}</li>' for t in x['tags'])+'</ul>'+links(x['links'])+'</article>'
def timeline(items):
 rows=[]
 for x in items:
  dates=(e(x['from'])+' – '+e(x['to'])) if x.get('from') and x.get('to') else 'Dates to be added'
  when='<div class="timeline-when"><p class="timeline-date">'+dates+'</p><p class="timeline-label">'+e(x['label'])+'</p></div>'
  org=link(x['org'],x['url']) if x.get('url') else e(x['org'])
  content='<div class="timeline-content"><h3>'+e(x['role'])+'</h3><p class="institution">'+org+'</p>'+''.join('<p class="timeline-note">'+e(n)+'</p>' for n in x['notes'])+'</div>'
  rows.append('<article class="timeline-row">'+when+content+'</article>')
 return '<div class="timeline">'+''.join(rows)+'</div>'

nav=[('research','Research'),('publications','Publications'),('artifacts','Code & data'),('grants','Grants'),('mentorship','Mentorship'),('experience','Experience'),('contact','Contact')]
navhtml=''.join(link(t,'#'+i) for i,t in nav)
html=f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(P['name'])} | {e(P['field'])}</title>
<meta name="description" content="{e(P['metaDescription'])}">
<meta name="author" content="Shifat Islam"><meta name="theme-color" content="#185b4d">
<meta property="og:type" content="profile"><meta property="og:title" content="Shifat Islam | Research Engineer"><meta property="og:description" content="Language, Vision & Healthcare AI · Seeking PhD opportunities"><meta property="og:url" content="https://shifatislam.github.io/">
<link rel="canonical" href="https://shifatislam.github.io/"><link rel="icon" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&amp;family=IBM+Plex+Sans:wght@400;500;600&amp;display=swap">
<link rel="stylesheet" href="style.css"><script id="metrics-snapshot" type="application/json">{METRICS}</script><script src="script.js" defer></script>
</head><body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="container header-inner"><a class="brand" href="#about">Shifat Islam<span>Research Engineer</span></a><nav aria-label="Primary">{navhtml}</nav></div></header>
<main id="main" class="container">
<section id="about" class="hero" aria-label="About Shifat Islam">
<div class="hero-copy"><p class="eyebrow hero-kicker">{e(P['field'])}</p><h1>{e(P['name'])}</h1>
<p class="hero-role">{e(P['role'])}</p>
<p class="hero-intro">Connecting language and vision<br class="desktop-break"> to real-world health challenges.</p>
<p class="hero-summary">{e(P['summary'])}</p>
<div class="phd-note"><span class="phd-label">{e(P['seeking'])}</span><p>Language models, multimodal learning, and AI for healthcare.</p></div>
<div class="hero-links">{link('Get in touch','mailto:'+P['email'],'button solid')}{link('Google Scholar ↗',P['scholar'],'button')}{link('GitHub ↗',P['github'],'button')}{link('ORCID ↗',P['orcid'],'button')}{link('LinkedIn ↗',P['linkedin'],'button')}</div></div>
<aside class="hero-aside" aria-label="Profile and citation history">
<div class="portrait-row"><img src="assets/profile.jpg" width="150" height="150" class="portrait" alt="Shifat Islam"><div><p class="portrait-name">Shifat Islam</p><p class="muted">Co-Founder &<br>Deputy Director, A.R.i.S.E</p>{link('Institute profile ↗','https://ariserl.org/people/shifat-islam','small-link')}</div></div>
<div class="citation-panel"><div class="panel-head"><h2>Citations by year</h2><span>Google Scholar</span></div>
<div id="citation-chart"><div class="citation-empty"><p class="citation-label">Research impact</p><p>Explore the latest citation history and research metrics on my Google Scholar profile.</p>{link('View citation history ↗',P['scholar'],'button')}</div></div>
<p id="citation-note" class="panel-foot">Yearly figures will appear here once verified.</p></div>
</aside></section>
<div class="output-strip" aria-label="Research overview"><div><strong>{P['publishedCount']}</strong><span>Published papers</span></div><div><strong>{len(D['datasets'])}</strong><span>Open datasets with DOIs</span></div><div><strong id="total-citations">{e(P["citationDisplay"])}</strong><span>{link('Citations ↗',P['scholar'])}</span></div><div><strong>{e(P["mentoredCount"])}</strong><span>Undergraduate students mentored</span></div></div>
'''
research='<div id="research-interests" class="research-grid">'
for r in D['research']:
 research+=f'<article class="research-card {e(r["id"])}"><h3>{e(r["title"])}</h3><p>{rich(r["description"])}</p><ul>'+''.join('<li>'+e(t)+'</li>' for t in r['threads'])+'</ul>'+link(r['linkLabel']+' →',r['link'],'research-link')+'</article>'
html+=section('research','Research',research+'</div>','Three connected directions across language, visual understanding, and health.')
selected=[p for p in D['publications'] if p['selected']];more=[p for p in D['publications'] if not p['selected']]
pubs='<div class="publication-list">'+''.join(publication(p) for p in selected)+'</div>'
pubs+=f'<details class="more-publications" id="all-publications"><summary><span class="when-closed">View all {len(D["publications"])} publications</span><span class="when-open">Show selected publications only</span><span class="expand-icon" aria-hidden="true">+</span></summary><div class="expanded-heading"><h3>More publications & manuscripts</h3><p>{len(more)} additional entries</p></div>'+''.join(publication(p) for p in more)+'</details>'
pubs+='<p class="section-tail">'+link('Full profile on Google Scholar ↗',P['scholar'])+'</p>'
html+=section('publications','Selected publications',pubs,'Six representative studies across my research areas.')
html+=section('artifacts','Code & data','<div class="resource-grid">'+''.join(card(x) for x in D['code'])+'</div>','Open implementations and collaborative research resources.')
datasets='<div class="dataset-list">'
for d in D['datasets']:
 datasets+=f'<article class="dataset-row"><div><span class="dataset-type">DATASET / {d["year"]}</span><h3>{e(d["title"])}</h3></div><div><p>{e(d["description"])}</p><a class="doi" href="{e(d["url"])}">DOI: {e(d["doi"])}</a></div>'+link('Mendeley Data ↗',d['archive'],'dataset-action')+'</article>'
datasets+='</div><p class="section-tail">'+link('Dataset records on ORCID ↗',P['orcid'])+'</p>'
html+=section('datasets','Open datasets',datasets,'Versioned research datasets linked from my ORCID record.')
html+=section('projects','Applied projects','<div class="resource-grid two-columns">'+''.join(card(x) for x in D['projects'])+'</div>','From research methods to working systems.')
mentorship='<div class="mentorship-list">'
for m in D['mentorship']:
 mentorship+='<article class="mentorship-card"><div class="mentorship-heading"><h3>'+e(m['title'])+'</h3><p class="mentorship-topics">'+e(m['topics'])+'</p></div><ul>'+''.join('<li>'+rich(point)+'</li>' for point in m['points'])+'</ul></article>'
mentorship+='</div>'
html+=section('mentorship','Research Mentorship',mentorship)
grants='''<article class="grant"><div class="grant-meta"><span class="grant-role">Research Mentor</span><span>REG-NER</span></div><div><h3>Bangla Regional Named Entity Recognition Corpus</h3><p class="institution">Institute of Research and Training, Southeast University</p><p>Research on regional Bangla named entities, with a shared corpus and baseline evaluations supporting low-resource NLP.</p><p class="grant-reference">Grant reference: SEU/IRT/RG/2025/01/09</p><div class="grant-outcomes"><span>Research outputs</span><a href="https://doi.org/10.1371/journal.pone.0342786">ANCHOLIK-NER · PLOS ONE, 2026 ↗</a><a href="https://doi.org/10.17632/gbkszkt8z3.1">Public dataset · Mendeley Data ↗</a></div><p class="small-note">Project grant awarded to M. A. Hoque; my project role is Research Mentor.</p></div></article>
<article class="grant"><div class="grant-meta"><span class="grant-role neutral">Publication support</span><span>IAR · UIU</span></div><div><h3>Institute for Advanced Research Publication Grant</h3><p class="institution">United International University</p></div></article>'''
html+=section('grants','Grants & research support',grants)
html+=section('experience','Experience & leadership',timeline(D['experience']))
html+=section('education','Education',timeline(D['education']))
awards='<div class="awards-list">'
for a in D['awards']:
 awards+='<article><div><h3>'+e(a['title'])+'</h3><p>'+e(a['detail'])+'</p></div>'+(link(a['linkLabel']+' ↗',a['url']) if a.get('url') else '')+'</article>'
awards+='</div>'
html+=section('achievements','Awards & recognition',awards)
skills='<div class="skills-grid">'
for group,items in D['skills'].items():skills+='<div><h3>'+e(group)+'</h3><ul>'+''.join('<li>'+e(x)+'</li>' for x in items)+'</ul></div>'
html+=section('skills','Research toolkit',skills+'</div>')
html+=f'''<section id="contact" class="contact" aria-label="Get in touch"><div><p class="eyebrow">PHD OPPORTUNITIES & RESEARCH COLLABORATION</p><h2>Get in touch.</h2><p>{e(P['contactText'])}</p></div><div class="contact-actions">{link(P['email'],'mailto:'+P['email'],'contact-email')}{link('LinkedIn ↗',P['linkedin'],'button')}{link('Google Scholar ↗',P['scholar'],'button')}{link('A.R.I.S.E ↗','https://ariserl.org/','button')}</div></section>
</main><footer class="site-footer"><div class="container footer-inner"><p>© <span id="year">2026</span> Shifat Islam</p><div>{link('GitHub',P['github'])}{link('LinkedIn',P['linkedin'])}{link('Google Scholar',P['scholar'])}{link('A.R.I.S.E','https://ariserl.org/')}{link('Scopus',P['scopus'])}{link('Back to top ↑','#about')}</div></div></footer>
</body></html>'''
(ROOT/'index.html').write_text(html,encoding='utf-8')
print('Built index.html:',len(D['publications']),'papers;',len(selected),'selected;',len(D['datasets']),'datasets')
