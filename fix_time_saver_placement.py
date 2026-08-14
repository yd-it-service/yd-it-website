from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

en_marker = '<section class="time-saver-section" aria-label="YD-IT handles your on-site datacenter visit">'
start = html.find(en_marker)
if start != -1:
    end = html.find('</section>', start)
    if end == -1:
        raise SystemExit('Could not find end of English time-saver section')
    end += len('</section>')
    en_section = html[start:end]
    html = html[:start] + html[end:]
else:
    raise SystemExit('English time-saver section not found')

hero_marker = '<h1>Remote Hands &amp; IT Solutions</h1>'
hero_pos = html.find(hero_marker)
if hero_pos == -1:
    raise SystemExit('English hero not found')
hero_end = html.find('</section>', hero_pos)
if hero_end == -1:
    raise SystemExit('English hero section end not found')
hero_end += len('</section>')
html = html[:hero_end] + '\n' + en_section + '\n' + html[hero_end:]

path.write_text(html, encoding='utf-8')
Path('YD-IT-aktuell.html').write_text(html, encoding='utf-8')
