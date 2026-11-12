import textwrap, os
T={'dark':dict(bg1='#060B18',bg2='#0A1A33',fg='#F5F8FF',mut='#8FA3BF',line='#1C2C47',card='#0D1B30',a='#0E75B6',b='#22D3EE',c='#7C9CFF'),
   'light':dict(bg1='#F7FAFF',bg2='#E8F1FB',fg='#0A1A33',mut='#4B5D78',line='#D5E2F1',card='#FFFFFF',a='#0E75B6',b='#0891B2',c='#4F6BED')}
F="font-family:'Inter','Segoe UI',-apple-system,BlinkMacSystemFont,'Helvetica Neue',Arial,sans-serif"
RM="@media (prefers-reduced-motion:reduce){*{animation:none!important;opacity:1!important}}"
UP="@keyframes up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}"

def hero(t):
  chips=''.join(f'<rect x="{x}" y="336" width="{w}" height="36" rx="10" fill="{t["card"]}" stroke="{t["line"]}"/><text x="{x+w/2}" y="359" text-anchor="middle" fill="{t["fg"]}">{s}</text>' for x,w,s in [(72,150,'Design systems'),(232,120,'Agent UX'),(362,150,'Next.js builds'),(522,140,'Product films')])
  return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="440" viewBox="0 0 1200 440">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg2']}"/></linearGradient>
<radialGradient id="g1"><stop offset="0" stop-color="{t['b']}" stop-opacity=".45"/><stop offset="1" stop-color="{t['b']}" stop-opacity="0"/></radialGradient>
<radialGradient id="g2"><stop offset="0" stop-color="{t['c']}" stop-opacity=".40"/><stop offset="1" stop-color="{t['c']}" stop-opacity="0"/></radialGradient>
<linearGradient id="tx" x1="0" x2="1"><stop offset="0" stop-color="{t['a']}"/><stop offset=".5" stop-color="{t['b']}"/><stop offset="1" stop-color="{t['c']}"/></linearGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{t['line']}" stroke-width="1"/></pattern>
<linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".55" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity=".3"/></linearGradient>
<mask id="m"><rect width="1200" height="440" fill="url(#fade)"/></mask>
<clipPath id="r"><rect width="1200" height="440" rx="28"/></clipPath>
<style>
.f{{{F}}}
.o1{{animation:d1 14s ease-in-out infinite alternate}} .o2{{animation:d2 18s ease-in-out infinite alternate}}
@keyframes d1{{to{{transform:translate(-120px,60px)}}}} @keyframes d2{{to{{transform:translate(140px,-50px)}}}}
.up{{opacity:0;animation:up .9s cubic-bezier(.2,.8,.2,1) forwards}}
{UP}
.dot{{animation:p 2s ease-in-out infinite}} @keyframes p{{50%{{opacity:.25}}}}
.orb{{transform-origin:960px 220px;animation:spin 40s linear infinite}} .orb2{{transform-origin:960px 220px;animation:spin 26s linear infinite reverse}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
{RM}
</style></defs>
<g clip-path="url(#r)">
<rect width="1200" height="440" fill="url(#bg)"/>
<rect width="1200" height="440" fill="url(#grid)" mask="url(#m)" opacity=".7"/>
<circle class="o1" cx="1020" cy="120" r="320" fill="url(#g1)"/>
<circle class="o2" cx="760" cy="420" r="300" fill="url(#g2)"/>
<g class="orb" fill="none" stroke="{t['b']}" stroke-opacity=".4"><circle cx="960" cy="220" r="150" stroke-dasharray="2 10"/><circle cx="1110" cy="220" r="6" fill="{t['b']}" stroke="none"/></g>
<g class="orb2" fill="none" stroke="{t['c']}" stroke-opacity=".4"><circle cx="960" cy="220" r="100"/><circle cx="960" cy="120" r="5" fill="{t['c']}" stroke="none"/></g>
<g transform="translate(960 220)"><rect x="-46" y="-46" width="92" height="92" rx="24" fill="{t['card']}" stroke="{t['line']}"/>
<path d="M-20 14 L-20 -14 L0 6 L20 -14 L20 14" fill="none" stroke="url(#tx)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>
</g>
<rect x=".5" y=".5" width="1199" height="439" rx="28" fill="none" stroke="{t['line']}"/>
<g class="f">
<g class="up" style="animation-delay:.1s"><rect x="72" y="74" width="300" height="34" rx="17" fill="{t['card']}" stroke="{t['line']}"/>
<circle class="dot" cx="94" cy="91" r="5" fill="#22C55E"/><text x="110" y="96" font-size="14" font-weight="500" fill="{t['mut']}">Open to AI product collaborations</text></g>
<text class="up" style="animation-delay:.25s" x="68" y="196" font-size="76" font-weight="800" letter-spacing="-2.5" fill="{t['fg']}">Mriganka Dey</text>
<text class="up" style="animation-delay:.4s" x="72" y="250" font-size="30" font-weight="600" letter-spacing="-.5" fill="url(#tx)">I design AI products, then I ship them.</text>
<text class="up" style="animation-delay:.55s" x="72" y="298" font-size="18" fill="{t['mut']}">Product Designer  ·  Frontend Architect  ·  AI Builder  ·  India</text>
<g class="up" style="animation-delay:.7s" font-size="14" font-weight="600">{chips}</g>
</g></svg>'''

def pillars(t):
  items=[('01','Design','Design systems, enterprise dashboards, agent and copilot interfaces, brands and decks that close deals.',t['a']),
         ('02','Build','Pixel faithful React and Next.js, Tailwind, motion and 3D scroll, with a tight design to code loop.',t['b']),
         ('03','Intelligence','LLM products, multi agent workflows, voice AI, and generative image and video for storytelling.',t['c'])]
  out=f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="250" viewBox="0 0 1200 250"><style>.f{{{F}}} .c{{opacity:0;animation:up .8s cubic-bezier(.2,.8,.2,1) forwards}} {UP} .bar{{transform:scaleX(0);animation:grow 1.4s cubic-bezier(.2,.8,.2,1) forwards}} @keyframes grow{{to{{transform:scaleX(1)}}}} @media (prefers-reduced-motion:reduce){{*{{animation:none!important;opacity:1!important;transform:none!important}}}}</style><g class="f">'
  for i,(n,h,d,col) in enumerate(items):
    x=i*404
    out+=f'<g class="c" style="animation-delay:{.15*i}s"><rect x="{x+.5}" y=".5" width="391" height="249" rx="22" fill="{t["card"]}" stroke="{t["line"]}"/>'
    out+=f'<rect class="bar" style="transform-origin:{x+32}px 0;animation-delay:{.3+.15*i}s" x="{x+32}" y="34" width="56" height="5" rx="2.5" fill="{col}"/>'
    out+=f'<text x="{x+359}" y="44" text-anchor="end" font-size="14" font-weight="600" fill="{t["mut"]}">{n}</text>'
    out+=f'<text x="{x+32}" y="96" font-size="30" font-weight="700" letter-spacing="-.8" fill="{t["fg"]}">{h}</text>'
    for j,l in enumerate(textwrap.wrap(d,38)): out+=f'<text x="{x+32}" y="{140+j*26}" font-size="16.5" fill="{t["mut"]}">{l}</text>'
    out+='</g>'
  return out+'</g></svg>'

def process(t):
  steps=['Brief','Research','System','Interface','Build','Story']
  out=f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="130" viewBox="0 0 1200 130"><defs><linearGradient id="l" x1="0" x2="1"><stop offset="0" stop-color="{t["a"]}"/><stop offset=".5" stop-color="{t["b"]}"/><stop offset="1" stop-color="{t["c"]}"/></linearGradient></defs><style>.f{{{F}}} .run{{stroke-dasharray:6 10;animation:dash 1.2s linear infinite}} @keyframes dash{{to{{stroke-dashoffset:-16}}}} .pulse{{opacity:.35;animation:pl 6s ease-in-out infinite}} @keyframes pl{{0%,100%{{opacity:.35}}8%,16%{{opacity:1}}}} @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style><g class="f">'
  out+=f'<line class="run" x1="100" y1="46" x2="1100" y2="46" stroke="url(#l)" stroke-width="2"/>'
  for i,s in enumerate(steps):
    x=100+i*200
    out+=f'<circle cx="{x}" cy="46" r="20" fill="{t["card"]}" stroke="{t["line"]}" stroke-width="1.5"/><circle class="pulse" style="animation-delay:{i}s" cx="{x}" cy="46" r="8" fill="url(#l)"/>'
    out+=f'<text x="{x}" y="104" text-anchor="middle" font-size="17" font-weight="600" fill="{t["fg"]}">{s}</text>'
  return out+'</g></svg>'

def footer(t):
  return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="220" viewBox="0 0 1200 220"><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg2']}"/></linearGradient><linearGradient id="tx" x1="0" x2="1"><stop offset="0" stop-color="{t['a']}"/><stop offset=".5" stop-color="{t['b']}"/><stop offset="1" stop-color="{t['c']}"/></linearGradient><radialGradient id="g"><stop offset="0" stop-color="{t['b']}" stop-opacity=".35"/><stop offset="1" stop-color="{t['b']}" stop-opacity="0"/></radialGradient><clipPath id="r"><rect width="1200" height="220" rx="28"/></clipPath>
<style>.f{{{F}}} .o{{animation:d 12s ease-in-out infinite alternate}} @keyframes d{{to{{transform:translate(-300px,0)}}}} @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style></defs>
<g clip-path="url(#r)"><rect width="1200" height="220" fill="url(#bg)"/><circle class="o" cx="1000" cy="110" r="260" fill="url(#g)"/></g>
<rect x=".5" y=".5" width="1199" height="219" rx="28" fill="none" stroke="{t['line']}"/>
<g class="f"><text x="72" y="98" font-size="38" font-weight="800" letter-spacing="-1.2" fill="{t['fg']}">Building an AI product?</text>
<text x="72" y="146" font-size="38" font-weight="800" letter-spacing="-1.2" fill="url(#tx)">Let&apos;s make it feel inevitable.</text>
<rect x="880" y="82" width="248" height="56" rx="28" fill="url(#tx)"/><text x="1004" y="117" text-anchor="middle" font-size="18" font-weight="700" fill="#fff">Connect on LinkedIn  ↗</text></g></svg>'''

os.makedirs('assets',exist_ok=True)
for n,fn in [('hero',hero),('pillars',pillars),('process',process),('footer',footer)]:
  for m,t in T.items(): open(f'assets/{n}-{m}.svg','w',encoding='utf-8').write(fn(t))
