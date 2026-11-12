# Generates the README SVGs (light + dark). Run from repo root: python assets/gen.py
import base64, textwrap
T = {
  'light': dict(bg='#FFFFFF', ink='#0B0D12', mut='#5B6270', rule='#E6E9F0', panel='#EEF2FF', panel2='#E0E7FF', acc='#1F4FFF', teal='#1F5F6B', card='#FFFFFF'),
  'dark':  dict(bg='#0B0D12', ink='#F4F6FB', mut='#9AA3B2', rule='#222838', panel='#E9EDFB', panel2='#D9E0FA', acc='#6E8BFF', teal='#5FB3C2', card='#121622'),
}
F = "font-family:'Google Sans Flex','Google Sans','Inter','Segoe UI',-apple-system,BlinkMacSystemFont,'Helvetica Neue',Arial,sans-serif"
S = "font-family:'Instrument Serif',Georgia,'Times New Roman',serif;font-style:italic"
RM = "@media (prefers-reduced-motion:reduce){*{animation:none!important;opacity:1!important;transform:none!important}}"
UP = "@keyframes up{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}"
b64 = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
CH, CHS = b64('assets/character.png'), b64('assets/character-sm.png')

def hero(t):
    chips = ''
    for i, (x, s) in enumerate([(72,'LLM agents'),(196,'RAG'),(262,'Voice AI'),(358,'Next.js'),(444,'Design systems')]):
        chips += f'<text x="{x}" y="446" font-size="17" font-weight="{700 if i==0 else 500}" fill="{t["ink"] if i==0 else t["mut"]}">{s}</text>'
    # agent network floating in the panel
    nodes = [(838, 92), (930, 60), (1010, 110), (868, 170), (960, 150)]
    edges = [(0,1),(1,2),(0,3),(3,4),(1,4),(2,4)]
    net = ''.join(f'<line class="e" style="animation-delay:{i*.35}s" x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}"/>' for i,(a,b) in enumerate(edges))
    net += ''.join(f'<circle class="n" style="animation-delay:{i*.5}s;transform-origin:{x}px {y}px" cx="{x}" cy="{y}" r="7"/>' for i,(x,y) in enumerate(nodes))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="520" viewBox="0 0 1200 520">
<defs><clipPath id="p"><rect x="760" y="24" width="416" height="472" rx="28"/></clipPath>
<linearGradient id="pg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t['panel']}"/><stop offset="1" stop-color="{t['panel2']}"/></linearGradient>
<style>
.f{{{F}}} .s{{{S}}}
.up{{opacity:0;animation:up .9s cubic-bezier(.2,.8,.2,1) forwards}} {UP}
.ch{{animation:float 5s ease-in-out infinite}} @keyframes float{{50%{{transform:translateY(-8px)}}}}
.e{{stroke:{t['acc']};stroke-width:2;stroke-dasharray:5 7;opacity:.55;animation:dash 1.4s linear infinite}} @keyframes dash{{to{{stroke-dashoffset:-24}}}}
.n{{fill:#fff;stroke:{t['acc']};stroke-width:3;animation:pulse 2.5s ease-in-out infinite}} @keyframes pulse{{50%{{transform:scale(1.35)}}}}
.dot{{animation:blink 2s ease-in-out infinite}} @keyframes blink{{50%{{opacity:.3}}}}
.cur{{animation:blink 1s steps(1) infinite}}
{RM}
</style></defs>
<rect width="1200" height="520" rx="28" fill="{t['bg']}"/>
<rect x=".5" y=".5" width="1199" height="519" rx="28" fill="none" stroke="{t['rule']}"/>
<g clip-path="url(#p)"><rect x="760" y="24" width="416" height="472" fill="url(#pg)"/>
<g opacity=".5">{''.join(f'<line x1="760" y1="{y}" x2="1176" y2="{y}" stroke="{t["acc"]}" stroke-opacity=".08"/>' for y in range(64,496,40))}</g>
<g class="ch"><image x="788" y="70" width="360" height="{int(360*860/588)}" href="data:image/png;base64,{CH}"/></g>
</g>
<g class="f">
<g class="up" style="animation-delay:.05s"><circle class="dot" cx="78" cy="74" r="5" fill="{t['acc']}"/>
<text x="94" y="80" font-size="15" font-weight="700" letter-spacing="1.4" fill="{t['acc']}">AI ENGINEER  ·  PRODUCT DESIGNER  ·  INDIA</text></g>
<text class="up" style="animation-delay:.18s" x="66" y="200" font-size="112" font-weight="800" letter-spacing="-5" fill="{t['ink']}">Mriganka</text>
<text class="up" style="animation-delay:.28s" x="66" y="300" font-size="112" font-weight="800" letter-spacing="-5" fill="{t['ink']}">Dey<tspan class="cur" fill="{t['acc']}">_</tspan></text>
<g class="up" style="animation-delay:.42s"><text x="72" y="364" font-size="28" font-weight="400" letter-spacing="-.3" fill="{t['ink']}">I build AI agents and design the <tspan class="s" font-size="34" fill="{t['acc']}">products</tspan></text>
<text x="72" y="400" font-size="28" font-weight="400" letter-spacing="-.3" fill="{t['ink']}">people use them through.</text></g>
<g class="up" style="animation-delay:.58s"><line x1="72" y1="412" x2="680" y2="412" stroke="{t['rule']}" stroke-opacity="0"/>{chips}</g>
</g></svg>'''

def pillars(t):
    items = [('01', 'Agents', 'Multi agent systems, tool use, RAG and evals. Orchestration that holds up in production, not just in a demo.'),
             ('02', 'Interfaces', 'Copilots, agent consoles and enterprise dashboards that make complex AI feel calm and obvious.'),
             ('03', 'Shipping', 'Next.js, TypeScript and Python on Azure. One loop from Paper frame to deployed product.')]
    o = f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300"><style>.f{{{F}}} .s{{{S}}} .c{{opacity:0;animation:up .8s cubic-bezier(.2,.8,.2,1) forwards}} {UP} {RM}</style><g class="f">'
    o += f'<line x1="0" y1="1" x2="1200" y2="1" stroke="{t["ink"]}" stroke-width="2"/>'
    for i, (n, h, d) in enumerate(items):
        x = i * 410
        o += f'<g class="c" style="animation-delay:{.12*i}s">'
        if i: o += f'<line x1="{x-24}" y1="40" x2="{x-24}" y2="270" stroke="{t["rule"]}"/>'
        o += f'<text x="{x}" y="54" font-size="15" font-weight="700" letter-spacing="1.2" fill="{t["acc"]}">{n}</text>'
        o += f'<text x="{x}" y="120" font-size="48" font-weight="800" letter-spacing="-2" fill="{t["ink"]}">{h}</text>'
        for j, l in enumerate(textwrap.wrap(d, 36)):
            o += f'<text x="{x}" y="{170+j*28}" font-size="18" fill="{t["mut"]}">{l}</text>'
        o += '</g>'
    return o + '</g></svg>'

def process(t):
    steps = ['Brief', 'Research', 'Agent design', 'Interface', 'Build', 'Ship + measure']
    o = f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="120" viewBox="0 0 1200 120"><style>.f{{{F}}} .run{{stroke-dasharray:4 8;animation:d 1.2s linear infinite}} @keyframes d{{to{{stroke-dashoffset:-24}}}} .on{{opacity:.25;animation:on 6s ease-in-out infinite}} @keyframes on{{0%,100%{{opacity:.25}}6%,16%{{opacity:1}}}} {RM}</style><g class="f">'
    o += f'<line class="run" x1="40" y1="40" x2="1160" y2="40" stroke="{t["acc"]}" stroke-width="2"/>'
    for i, s in enumerate(steps):
        x = 40 + i * 224
        o += f'<circle cx="{x}" cy="40" r="14" fill="{t["bg"]}" stroke="{t["ink"]}" stroke-width="2"/><circle class="on" style="animation-delay:{i}s" cx="{x}" cy="40" r="7" fill="{t["acc"]}"/>'
        anchor = 'start' if i == 0 else ('end' if i == len(steps)-1 else 'middle')
        o += f'<text x="{x if i else x-14}" y="92" text-anchor="{anchor}" font-size="18" font-weight="600" fill="{t["ink"]}">{s}</text>'
    return o + '</g></svg>'

def footer(t):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="260" viewBox="0 0 1200 260"><defs><clipPath id="c"><rect width="1200" height="260" rx="28"/></clipPath></defs><style>.f{{{F}}} .s{{{S}}} .w{{transform-origin:110px 200px;animation:wave 3s ease-in-out infinite}} @keyframes wave{{0%,70%,100%{{transform:rotate(0)}}80%{{transform:rotate(-4deg)}}90%{{transform:rotate(3deg)}}}} {RM}</style>
<g clip-path="url(#c)"><rect width="1200" height="260" fill="{t['panel']}"/>
<g class="w"><image x="56" y="40" width="160" height="234" href="data:image/png;base64,{CHS}"/></g></g>
<g class="f"><text x="260" y="112" font-size="44" font-weight="800" letter-spacing="-1.8" fill="#0B0D12">Building something with AI?</text>
<text x="260" y="166" font-size="44" font-weight="400" letter-spacing="-1" fill="#0B0D12">Let&apos;s make it feel <tspan class="s" font-size="52" fill="#1F4FFF">inevitable.</tspan></text>
<rect x="912" y="100" width="232" height="60" rx="30" fill="#0B0D12"/><text x="1028" y="137" text-anchor="middle" font-size="18" font-weight="700" fill="#fff">Say hi on LinkedIn  ↗</text></g></svg>'''

for n, fn in [('hero', hero), ('pillars', pillars), ('process', process), ('footer', footer)]:
    for m, t in T.items():
        open(f'assets/{n}-{m}.svg', 'w', encoding='utf-8').write(fn(t))
