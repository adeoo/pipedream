#!/usr/bin/env python3
"""Render a lesson .md into email HTML + plain text. Usage: render.py lessons/weekNN/dayNN.md
Prints JSON: {"subject":..., "send_date":..., "html":..., "text":...}"""
import sys, re, json

def inline(s):
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'<em>\1</em>', s)
    return s

def strip_md(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'\1', s)
    return s

path = sys.argv[1]
raw = open(path).read()
m = re.match(r'---\n(.*?)\n---\n(.*)', raw, re.S)
meta = dict(re.findall(r'(\w+):\s*"?(.*?)"?\s*$', m.group(1), re.M))
body = m.group(2).strip()
paras = re.split(r'\n\s*\n', body)

P = 'margin:0 0 16px;font-family:Georgia,serif;font-size:16px;line-height:1.65;color:#2b2b2b;'
html_parts, text_parts = [], []
for p in paras:
    p = p.strip()
    if p.startswith('>'):
        quote = ' '.join(l.lstrip('> ').strip() for l in p.splitlines())
        html_parts.append(f'<blockquote style="margin:0 0 16px;padding:12px 18px;border-left:4px solid #b22222;background:#faf6f2;font-family:Georgia,serif;font-size:16px;line-height:1.65;color:#4a3f38;font-style:italic;">{inline(quote)}</blockquote>')
        text_parts.append('    ' + strip_md(quote))
    elif p.startswith('\U0001F4DC'):  # context box
        html_parts.append(f'<div style="margin:0 0 20px;padding:14px 18px;background:#f4efe8;border-radius:6px;"><p style="{P}margin:0;">{inline(p)}</p></div>')
        text_parts.append(strip_md(p))
    elif p.startswith('*Week'):
        html_parts.append(f'<hr style="border:none;border-top:1px solid #ddd;margin:24px 0 12px;"><p style="{P}font-size:13px;color:#8a8a8a;">{inline(p)}</p>')
        text_parts.append('--\n' + strip_md(p))
    elif re.match(r'^\d+\.', p):
        num = re.compile(r'^\d+\.\s*')
        items = ''.join('<li style="margin:0 0 8px;">' + inline(num.sub('', l.strip())) + '</li>'
                        for l in p.splitlines() if l.strip())
        html_parts.append(f'<ol style="{P}padding-left:22px;">{items}</ol>')
        text_parts.append(strip_md(p))
    else:
        html_parts.append(f'<p style="{P}">' + inline(p).replace(chr(10), '<br>') + '</p>')
        text_parts.append(strip_md(p))

title = re.sub(r'^☭\s*', '', meta['subject'])
html = (f'<div style="background:#fdfcfa;padding:24px 12px;"><div style="max-width:600px;margin:0 auto;background:#ffffff;padding:32px 28px;border-radius:8px;border:1px solid #eee;">'
        f'<p style="margin:0 0 4px;font-family:Georgia,serif;font-size:12px;letter-spacing:2px;color:#b22222;text-transform:uppercase;">Daily Marxism</p>'
        f'<h1 style="margin:0 0 20px;font-family:Georgia,serif;font-size:24px;line-height:1.3;color:#1a1a1a;">{inline(title)}</h1>'
        + ''.join(html_parts) + '</div></div>')
text = meta['subject'] + '\n\n' + '\n\n'.join(text_parts)
print(json.dumps({'subject': meta['subject'], 'send_date': meta.get('send_date',''), 'html': html, 'text': text}))
