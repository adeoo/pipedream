#!/usr/bin/env python3
"""Render a lesson .md into plain email HTML + text, in both languages.

Usage:
  render.py lessons/weekNN/dayNN.md
      prints JSON: {"subject","subject_pt","send_date","html","text","html_pt","text_pt"}
  render.py lessons/weekNN/dayNN.md --write DIR
      also writes the ready-to-send files into DIR and prints one check line per file:
        en.subject.txt  en.html  en.txt  pt.subject.txt  pt.html  pt.txt
      The daily send Routine copies each file's content verbatim into the matching
      inkbox_email_send parameter (subject, body_html, body_text). It never retypes,
      escapes or reformats the content.

Design per PROGRAM.md v2: plain text on white, one font, no cards, no boxes, no
horizontal lines, the quote set apart simply by indentation. The HTML is deliberately
compact: one styled wrapper, bare <p> tags inside, so the send step has as little to
copy as possible (the old per-paragraph inline styles doubled the size of every email).
"""
import json
import os
import re
import sys

FONT = 'Helvetica,Arial,sans-serif'
WRAP = ('max-width:600px;margin:0 auto;padding:24px 16px;background:#ffffff;'
        f'font-family:{FONT};font-size:16px;line-height:1.6;color:#222222;')
H1 = 'margin:0 0 24px;font-size:22px;line-height:1.3;color:#111111;'
QUOTE = 'padding-left:24px;font-style:italic;color:#444444;'
FOOTER = 'margin-top:28px;font-size:13px;color:#888888;'


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
            html_parts.append(f'<p style="{QUOTE}">{inline(quote)}</p>')
            text_parts.append('    ' + strip_md(quote))
        elif p.startswith('*Week') or p.startswith('*Semana'):
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
    return out


def write_files(out, directory):
    """Write one file per send parameter and print a check line for each."""
    os.makedirs(directory, exist_ok=True)
    files = [('en.subject.txt', out['subject']),
             ('en.html', out['html']),
             ('en.txt', out['text'])]
    if 'subject_pt' in out:
        files += [('pt.subject.txt', out['subject_pt']),
                  ('pt.html', out['html_pt']),
                  ('pt.txt', out['text_pt'])]
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
        print(json.dumps(out))
