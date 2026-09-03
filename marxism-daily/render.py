#!/usr/bin/env python3
"""Render a lesson .md into plain email HTML + text, in both languages.
Usage: render.py lessons/weekNN/dayNN.md
Prints JSON: {"subject","subject_pt","send_date","html","text","html_pt","text_pt"}
Design per PROGRAM.md v2: plain text on white, one font, no cards, no boxes,
no horizontal lines, quote set apart simply by indentation.
"""
import sys, re, json

FONT = 'Helvetica,Arial,sans-serif'
P = f'margin:0 0 16px;font-family:{FONT};font-size:16px;line-height:1.6;color:#222222;'


def inline(s):
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'<em>\1</em>', s)
    return s


def strip_md(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'\1', s)
    return s


def render_body(subject, body):
    """Return (html, text) for one language's lesson body."""
    paras = re.split(r'\n\s*\n', body.strip())
    html_parts, text_parts = [], []
    for p in paras:
        p = p.strip()
        if not p:
            continue
        if p.startswith('>'):
            quote = ' '.join(l.lstrip('> ').strip() for l in p.splitlines())
            html_parts.append(
                f'<p style="{P}padding-left:24px;font-style:italic;color:#444444;">{inline(quote)}</p>')
            text_parts.append('    ' + strip_md(quote))
        elif p.startswith('*Week') or p.startswith('*Semana'):
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
body = m.group(2)

parts = re.split(r'^===\s*PT-BR\s*===\s*$', body, maxsplit=1, flags=re.M)
en_body = parts[0]
pt_body = parts[1] if len(parts) > 1 else ''

out = {'subject': meta['subject'], 'send_date': meta.get('send_date', '')}
out['html'], out['text'] = render_body(meta['subject'], en_body)
if pt_body.strip():
    subject_pt = meta.get('subject_pt', meta['subject'])
    out['subject_pt'] = subject_pt
    out['html_pt'], out['text_pt'] = render_body(subject_pt, pt_body)
print(json.dumps(out))
