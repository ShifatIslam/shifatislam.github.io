'use strict';
// The whole portfolio is static HTML; JS only enhances citations and navigation.
document.getElementById('year').textContent = new Date().getFullYear();
function showCitationHistory(metrics) {
  if (metrics && Number.isInteger(metrics.total) && metrics.total >= 0) {
    document.getElementById('total-citations').textContent = metrics.total.toLocaleString();
  }
  if (!metrics || !Array.isArray(metrics.years) || !metrics.years.length) return;
  const points = [...metrics.years].sort((a,b) => a.year-b.year);
  const seen = new Set();
  const valid = points.every(p => Number.isInteger(p.year) && p.year >= 1900 && p.year <= new Date().getFullYear() && Number.isInteger(p.count) && p.count >= 0 && !seen.has(p.year) && seen.add(p.year));
  if (!valid || !/^\d{4}-\d{2}-\d{2}$/.test(metrics.asOf || '') || Number.isNaN(Date.parse(metrics.asOf))) return;
  const NS='http://www.w3.org/2000/svg';
  const svg=(tag,attributes,text) => {const el=document.createElementNS(NS,tag);Object.entries(attributes).forEach(([k,v])=>el.setAttribute(k,String(v)));if(text!==undefined)el.textContent=String(text);return el;};
  const width=Math.max(370,points.length*50+55),height=224,left=36,right=15,top=30,bottom=32;
  const plotW=width-left-right,plotH=height-top-bottom,max=Math.max(1,...points.map(p=>p.count));
  const ceiling=Math.max(1,Math.ceil(max/5)*5),step=plotW/points.length;
  const y=v=>top+plotH-(v/ceiling)*plotH;
  const chart=svg('svg',{viewBox:`0 0 ${width} ${height}`,class:'citation-svg',role:'img','aria-label':'Google Scholar citations by year: '+points.map(p=>`${p.year}: ${p.count}${p.partial?' (partial year)':''}`).join('; ')});
  [...new Set([0,Math.round(ceiling/2),ceiling])].forEach(v=>{chart.append(svg('line',{x1:left,x2:width-right,y1:y(v),y2:y(v),class:'gridline'}));chart.append(svg('text',{x:left-8,y:y(v)+4,'text-anchor':'end'},v));});
  points.forEach((p,i)=>{const x=left+step*(i+.5),barW=Math.min(30,step*.5),bar=svg('rect',{x:x-barW/2,y:y(p.count),width:barW,height:Math.max(0,top+plotH-y(p.count)),rx:2,class:p.partial?'bar partial':'bar'});bar.append(svg('title',{},`${p.year}: ${p.count} citations${p.partial?' (partial year)':''}`));chart.append(bar,svg('text',{x,y:y(p.count)-9,'text-anchor':'middle',class:'value'},p.count),svg('text',{x,y:height-10,'text-anchor':'middle'},p.year));});
  const path=points.map((p,i)=>`${i?'L':'M'}${left+step*(i+.5)},${y(p.count)}`).join(' ');
  chart.append(svg('path',{d:path,class:'citation-trend',fill:'none'}));
  points.forEach((p,i)=>chart.append(svg('circle',{cx:left+step*(i+.5),cy:y(p.count),r:3,class:'citation-point'})));
  const mount=document.getElementById('citation-chart');mount.replaceChildren(chart);
  const stats=[];[['total','total citations'],['hIndex','h-index'],['i10Index','i10-index']].forEach(([key,label])=>{if(Number.isInteger(metrics[key])&&metrics[key]>=0)stats.push(`${metrics[key]} ${label}`);});
  if(stats.length){const p=document.createElement('p');p.className='citation-metrics';p.textContent=stats.join(' · ');mount.append(p);}
  // A text table makes the exact counts accessible without relying on the graphic.
  const details=document.createElement('details');details.className='citation-data';const summary=document.createElement('summary');summary.textContent='View yearly counts';details.append(summary);
  const table=document.createElement('table');const caption=document.createElement('caption');caption.textContent='Google Scholar citations by year';table.append(caption);const thead=document.createElement('thead'),tr=document.createElement('tr');['Year','Citations'].forEach(t=>{const th=document.createElement('th');th.scope='col';th.textContent=t;tr.append(th);});thead.append(tr);table.append(thead);const tbody=document.createElement('tbody');points.forEach(p=>{const row=document.createElement('tr');[`${p.year}${p.partial?' (partial)':''}`,p.count].forEach(t=>{const td=document.createElement('td');td.textContent=String(t);row.append(td);});tbody.append(row);});table.append(tbody);details.append(table);mount.append(details);
  document.getElementById('citation-note').textContent=`Google Scholar snapshot · ${metrics.asOf}${points.some(p=>p.partial)?' · Lighter bars indicate partial years.':''}${metrics.chartNote?' · '+metrics.chartNote:''}`;
}
// The source of truth is a local JSON snapshot, as on the reference site.
// The embedded copy keeps downloaded, offline previews usable after a rebuild.
function renderMetricsSnapshot(snapshot) {
  if (!snapshot || typeof snapshot !== 'object') return;
  showCitationHistory({
    asOf: snapshot.asOf,
    total: snapshot.scholar?.citations,
    hIndex: snapshot.scholar?.hIndex,
    i10Index: snapshot.scholar?.i10Index,
    years: snapshot.citationsByYear,
    chartNote: snapshot.chartNote
  });
}
try { renderMetricsSnapshot(JSON.parse(document.getElementById('metrics-snapshot').textContent)); }
catch (_) { /* Retain the labeled CV figures if no valid snapshot is available. */ }
if (location.protocol === 'https:' || location.protocol === 'http:') {
  fetch('data/metrics.json', {cache: 'no-cache'})
    .then(response => {if (!response.ok) throw new Error('Metrics unavailable'); return response.json();})
    .then(renderMetricsSnapshot)
    .catch(() => { /* Retain the embedded snapshot; do not replace real counts with zeros. */ });
}
if ('IntersectionObserver' in window) {
  const links=[...document.querySelectorAll('nav a')];
  const observer=new IntersectionObserver(entries=>{
    for(const entry of entries){if(!entry.isIntersecting)continue;links.forEach(link=>{if(link.hash==='#'+entry.target.id)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');});}
  },{rootMargin:'-10% 0px -65% 0px',threshold:0});
  links.forEach(link=>{const section=document.querySelector(link.hash);if(section)observer.observe(section);});
}
