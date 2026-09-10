#!/usr/bin/env python3
"""Render a fichamento .md into plain email HTML + text (PT-BR, single language).

Usage:
  render.py fichamentos/dayNN.md
      prints JSON: {"subject","send_date","day","theme","html","text"}
  render.py fichamentos/dayNN.md --write DIR
      also writes the ready-to-send files into DIR and prints one check line per file:
        subject.txt  body.html  body.txt
      The daily Routine copies each file's content verbatim into the matching
      inkbox_email_send parameter (subject, body_html, body_text). It never retypes,
      escapes or reformats the content.

Design mirrors marxism-daily: plain text on white, one font, no cards, no boxes; quotes
set apart by indentation; ## section titles as simple bold headings. The HTML is
deliberately compact: one styled wrapper, bare <p> tags inside, so the send step has as
little to copy as possible.
"""
import json
import os
import re
import sys

FONT = 'Helvetica,Arial,sans-serif'
WRAP = ('max-width:600px;margin:0 auto;padding:24px 16px;background:#ffffff;'
        f'font-family:{FONT};font-size:16px;line-height:1.6;color:#222222;')
H1 = 'margin:0 0 24px;font-size:22px;line-height:1.3;color:#111111;'
H2 = 'margin:28px 0 12px;line-height:1.4;color:#111111;font-weight:bold;'
QUOTE = 'padding-left:24px;font-style:italic;color:#444444;'
FOOTER = 'margin-top:28px;font-size:13px;color:#888888;'
LINK = 'color:#1a5632;'


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def inline(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'(https?://[^\s<]+[^\s<.,;)])',
               rf'<a href="\1" style="{LINK}">\1</a>', s)
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
            html_parts.append(f'<p style="{QUOTE}">{inline(quote)}</p>')
            text_parts.append('    ' + strip_md(quote))
        elif p.startswith('- '):
            items = [l[2:].strip() for l in p.splitlines() if l.strip().startswith('- ')]
            lis = ''.join(f'<li>{inline(i)}</li>' for i in items)
            html_parts.append(f'<ul style="padding-left:24px;">{lis}</ul>')
            text_parts.append('\n'.join('  - ' + strip_md(i) for i in items))
        elif p.startswith('*Dia'):
            html_parts.append(f'<p style="{FOOTER}">{inline(p)}</p>')
            text_parts.append(strip_md(p))
        else:
            html_parts.append('<p>' + inline(p).replace('\n', '<br>') + '</p>')
            text_parts.append(strip_md(p))
    html = (f'<div style="{WRAP}"><h1 style="{H1}">{inline(subject)}</h1>'
            + ''.join(html_parts) + '</div>')
    text = subject + '\n\n' + '\n\n'.join(text_parts)
    return html, text


def render(path):
    raw = open(path, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n(.*)', raw, re.S)
    if not m:
        sys.exit(f'{path}: missing front matter')
    meta = dict(re.findall(r'(\w+):\s*"?(.*?)"?\s*$', m.group(1), re.M))
    if 'subject' not in meta:
        sys.exit(f'{path}: missing subject')
    html, text = render_body(meta['subject'], m.group(2))
    return {'subject': meta['subject'], 'send_date': meta.get('send_date', ''),
            'day': meta.get('day', ''), 'theme': meta.get('theme', ''),
            'html': html, 'text': text}


def write_files(out, directory):
    """Write one file per send parameter and print a check line for each."""
    os.makedirs(directory, exist_ok=True)
    files = [('subject.txt', out['subject']),
             ('body.html', out['html']),
             ('body.txt', out['text'])]
    for name, content in files:
        full = os.path.join(directory, name)
        with open(full, 'w', encoding='utf-8') as f:
            f.write(content)
        head = content[:24].replace('\n', ' ')
        tail = content[-12:].replace('\n', ' ')
        print(f'{full}\t{len(content.encode("utf-8"))} bytes\tstarts {head!r}\tends {tail!r}')


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    out = render(args[0])
    if '--write' in args:
        write_files(out, args[args.index('--write') + 1])
    else:
        print(json.dumps(out, ensure_ascii=False))
