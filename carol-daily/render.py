#!/usr/bin/env python3
"""Render a fichamento .md into plain email HTML + text (PT-BR, single language).
Usage: render.py fichamentos/dayNN.md
Prints JSON: {"subject","send_date","day","theme","html","text"}
Design mirrors marxism-daily: plain text on white, one font, no cards, no boxes;
quotes set apart by indentation; ## section titles as simple bold headings.
"""
import sys, re, json

FONT = 'Helvetica,Arial,sans-serif'
P = f'margin:0 0 16px;font-family:{FONT};font-size:16px;line-height:1.6;color:#222222;'
H2 = f'margin:28px 0 12px;font-family:{FONT};font-size:16px;line-height:1.4;color:#111111;font-weight:bold;'


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def inline(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'(https?://[^\s<]+[^\s<.,;)])',
               r'<a href="\1" style="color:#1a5632;">\1</a>', s)
    return s


def strip_md(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'\1', s)
    return s


def render_body(subject, body):
    paras = re.split(r'\n\s*\n', body.strip())
    html_parts, text_parts = [], []
    for p in paras:
        p = p.strip()
        if not p:
            continue
        if p.startswith('## '):
            title = p[3:].strip()
            html_parts.append(f'<p style="{H2}">{inline(title)}</p>')
            text_parts.append(strip_md(title).upper())
        elif p.startswith('>'):
            quote = ' '.join(l.lstrip('> ').strip() for l in p.splitlines())
            html_parts.append(
                f'<p style="{P}padding-left:24px;font-style:italic;color:#444444;">{inline(quote)}</p>')
            text_parts.append('    ' + strip_md(quote))
        elif p.startswith('- '):
            items = [l[2:].strip() for l in p.splitlines() if l.strip().startswith('- ')]
            lis = ''.join(f'<li style="margin:0 0 8px;">{inline(i)}</li>' for i in items)
            html_parts.append(
                f'<ul style="{P}padding-left:24px;">{lis}</ul>')
            text_parts.append('\n'.join('  - ' + strip_md(i) for i in items))
        elif p.startswith('*Dia'):
            html_parts.append(
                f'<p style="{P}margin-top:28px;font-size:13px;color:#888888;">{inline(p)}</p>')
            text_parts.append(strip_md(p))
        else:
            html_parts.append(f'<p style="{P}">' + inline(p).replace(chr(10), '<br>') + '</p>')
            text_parts.append(strip_md(p))
    html = ('<div style="background:#ffffff;padding:24px 16px;">'
            '<div style="max-width:600px;margin:0 auto;">'
            f'<h1 style="margin:0 0 24px;font-family:{FONT};font-size:22px;line-height:1.3;'
            f'color:#111111;font-weight:bold;">{inline(subject)}</h1>'
            + ''.join(html_parts) + '</div></div>')
    text = subject + '\n\n' + '\n\n'.join(text_parts)
    return html, text


path = sys.argv[1]
raw = open(path).read()
m = re.match(r'---\n(.*?)\n---\n(.*)', raw, re.S)
meta = dict(re.findall(r'(\w+):\s*"?(.*?)"?\s*$', m.group(1), re.M))
html, text = render_body(meta['subject'], m.group(2))
print(json.dumps({'subject': meta['subject'], 'send_date': meta.get('send_date', ''),
                  'day': meta.get('day', ''), 'theme': meta.get('theme', ''),
                  'html': html, 'text': text}, ensure_ascii=False))
