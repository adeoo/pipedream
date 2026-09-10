# Carol Daily — artigo científico por dia

Irmão do `marxism-daily/`: todo dia às 06:00 (América/São_Paulo) a Carol (ana.ruberrime@gmail.com) recebe um e-mail com **um artigo científico real** relevante para a dissertação dela (planejamento urbano insurgente · multiespécies · ecofeminismo queer · transição sustentável), com citação literal, discussão analítica e referência ABNT pronta — um fichamento por dia para escrever a tese mais rápido e melhor.

- `PROGRAM.md` — o programa completo: perfil da tese, rotação de temas, regras de seleção, formato do e-mail e mecânica da Routine.
- `state.json` — próximo dia, artigos já cobertos, referências que ela já tem.
- `fichamentos/dayNN.md` — um arquivo por e-mail enviado (arquivo = acervo de fichamentos dela).
- `render.py` — converte um fichamento em subject/html/text para envio.

Diferença estrutural para o marxism-daily: aqui **não há** rotina semanal de escrita — a Routine diária pesquisa, verifica, escreve, envia e faz commit na mesma manhã, porque cada e-mail depende de pesquisa fresca.

Branch fonte da verdade: `claude/daily-programs`. Transporte: Inkbox, de `adeosagent@inkboxmail.com`.

## Envio (protocolo desde 2026-09-10)

`python3 carol-daily/render.py fichamentos/dayNN.md --write /tmp/send` escreve `subject.txt`, `body.html` e `body.txt` prontos para envio. A Routine copia cada arquivo sem alteração para o parâmetro correspondente do `inkbox_email_send`, depois relê a mensagem enviada com `inkbox_email_get` e confere que `body_html` começa com `<div style=` e `body_text` começa com o subject. Se falhar, manda no máximo uma "Cópia corrigida" e relata. Nada de e-mail de teste ou placeholder. Antes do push a Routine chama `add_repo` (acesso push).

Histórico: entre 04/09 e 09/09 as execuções retranscreviam o corpo à mão e a Carol recebeu 2 ou 3 cópias por dia (placeholder, HTML escapado, comando de shell). Os dias 6 a 9 foram enviados mas não chegaram ao repositório (push sem repositório anexado); os fichamentos foram reconstruídos a partir dos e-mails em 2026-09-09 e estão marcados com `reconstructed` no front matter.
