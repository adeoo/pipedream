# Carol Daily — programa

Um e-mail por dia para a Carol (Ana Carolina Oliveira, ana.ruberrime@gmail.com) com **um artigo científico real e relevante para a dissertação dela**, um trecho citado na íntegra, e uma discussão que faça trabalho analítico de verdade. Objetivo: acelerar e melhorar a escrita da dissertação — cada e-mail é um fichamento pronto para ser aproveitado no texto.

Enviado às 06:00 (América/São_Paulo) pela Routine diária, a partir de `adeosagent@inkboxmail.com` (identidade Inkbox), nome de exibição "Artigo do Dia".

## Perfil da tese

- **Título de trabalho:** Uma revisão bibliográfica sobre o planejamento insurgente na perspectiva multiespécies
- **Pergunta de pesquisa:** Como a literatura sobre planejamento insurgente e multiespécies, a partir da perspectiva do ecofeminismo queer, pode contribuir com diretrizes teórico-práticas para a transição sustentável nas cidades?
- **Palavras-chave:** planejamento urbano insurgente; ecofeminismo queer; planejamento urbano multiespécies; transição sustentável
- **Metodologia:** revisão bibliográfica (qualitativa, exploratória e analítica) — levantamento, análise de conteúdo, articulação teórico-crítica, sistematização propositiva
- **Capítulos:** 1 Introdução · 2 Fundamentação teórica (os 4 conceitos) · 3 Metodologia · 4 Movimentos sociais e espaços insurgentes (São Paulo) · 5 Análise e discussão · 6 Diretrizes · 7 Considerações finais
- **Referências que ela já tem** (nunca apresentar como novidade; podem aparecer como "pistas" só se fizer sentido dialogar): Houston et al. 2018 (*Make kin, not cities!*, Planning Theory); Sheikh, Foth & Mitchell 2023 (Regional Studies); Sheikh, Mitchell & Foth 2023 (Futures).

## Rotação de temas (ritmo semanal)

O dia global (`state.json → next_day`) define o tema: `((day - 1) % 7) + 1`.

1. **Planejamento urbano insurgente** — Miraftab, Holston, Sandercock, Friedmann e a produção recente do Sul global.
2. **Multiespécies / mais-que-humano e planejamento urbano** — Houston, Foth, Metzger, Tsing, Haraway aplicados à cidade.
3. **Ecofeminismo queer** — Gaard, Plumwood, Mortimer-Sandilands, Seymour; ecologia queer e feminismos ambientais.
4. **Transição sustentável nas cidades** — transições socioecológicas, justiça ambiental urbana, pós-crescimento urbano.
5. **Convergências e tensões entre os conceitos** — artigos-ponte entre dois ou mais eixos (o coração do Cap. 5).
6. **Movimentos sociais e espaços insurgentes** — de preferência São Paulo/Brasil/América Latina (hortas comunitárias, ocupações verdes, parques reivindicados) — alimenta o Cap. 4.
7. **Coringa / método** — o que mais ajudar naquele momento: metodologia de revisão bibliográfica, um clássico faltante, ou o maior buraco atual do `state.json`.

## Regras de seleção (inegociáveis)

- **Só artigo real e verificado.** Antes de escrever, extrair o texto da página do artigo (Tavily extract / WebFetch) e conferir título, autoria, ano, veículo e DOI. Nunca citar de memória sem verificar.
- **A citação é literal.** O trecho citado deve constar palavra por palavra no texto extraído. Se não conseguir extrair texto suficiente do artigo escolhido, escolher outro artigo. Trecho em língua estrangeira vem acompanhado de tradução em PT-BR.
- **Nunca repetir.** Conferir `state.json → covered` e `already_in_thesis` antes de escolher.
- **Preferências**, na ordem: acesso aberto (ela precisa conseguir ler!) > periódico revisado por pares > capítulo de livro relevante. Misturar textos canônicos e produção recente (últimos ~5 anos). Incluir produção em português e do Sul global sempre que possível.
- Se um artigo ideal for de acesso fechado mas essencial, pode entrar — avisando no e-mail e apontando versão aberta (repositório, preprint) quando existir.

## Formato do e-mail (fichamento)

Arquivo `fichamentos/dayNN.md` com front matter `subject`, `send_date`, `day`, `theme` e corpo em PT-BR com estas seções (`##`):

1. *(abertura, 1–2 frases, sem título)* — que eixo/capítulo o artigo de hoje serve e por que foi escolhido.
2. `## Referência (ABNT)` — pronta para colar na lista de referências, no padrão que ela já usa (SOBRENOME, Nome. Título. *Periódico*, v., n., p., ano. DOI. Disponível em. Acesso em).
3. `## Trecho para guardar` — a citação literal (blockquote), com página quando houver; se em inglês, tradução em PT-BR logo abaixo, também em blockquote, marcada "(tradução livre)".
4. `## Discussão` — 3 a 5 parágrafos que façam trabalho de verdade: o que o texto argumenta; onde conversa com a pergunta de pesquisa dela; **pelo menos uma convergência e uma tensão/lacuna** com os outros eixos da tese (isso alimenta o Cap. 5). Nada de resumo burocrático.
5. `## Como citar no texto` — 1–2 frases prontas em PT-BR, no tom de dissertação, com a chamada (SOBRENOME, ano), que ela possa colar e adaptar.
6. `## Pistas para aprofundar` — 2 ou 3 referências reais citadas no artigo ou próximas dele, cada uma com meia linha dizendo por que perseguir.
7. *(rodapé, itálico)* — `*Dia N · tema: X · link do artigo*`.

## Voz

Direta, quente e sem enrolação — como uma colega de orientação que leu o artigo primeiro e chegou animada. Rigor acadêmico sem burocratês. Português natural do Brasil. A discussão sempre toma posição: diz o que o artigo resolve para a tese e o que ele deixa em aberto. Extensão-alvo do e-mail: 500–800 palavras.

## Mecânica diária (o que a Routine faz)

1. `git fetch origin claude/carol-daily-article-emailer-eub1jz` e checkout/fast-forward (re-clonar se o contêiner foi reciclado).
2. Ler `PROGRAM.md` e `state.json`; tema do dia pela rotação.
3. Pesquisar, escolher e **verificar** o artigo (extração de texto obrigatória).
4. Escrever `fichamentos/dayNN.md` e validar: `python3 carol-daily/render.py <arquivo>` deve emitir subject/html/text sem erro.
5. Idempotência: conferir nos enviados do Inkbox se o subject do dia já saiu; se sim, parar.
6. Enviar via Inkbox de `adeosagent@inkboxmail.com` para `ana.ruberrime@gmail.com` (html + text). Verificar sucesso; uma nova tentativa em caso de falha; se falhar de novo, relatar o erro exato na sessão.
7. Atualizar `state.json` (próximo dia, artigo coberto), commit e `git push -u origin claude/carol-daily-article-emailer-eub1jz` (retry com backoff em erro de rede). Sem pull request.
