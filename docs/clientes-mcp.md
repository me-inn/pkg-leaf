# O que cada cliente de IA exige, e o que ele faz com o dado

Levantamento de documentação oficial — Claude, ChatGPT, Gemini Enterprise,
Copilot Studio — e do próprio protocolo. Feito para responder duas perguntas
que não podem ser respondidas por suposição:

1. O que a Treesy precisa oferecer para que cada um consiga conectar?
2. O que acontece com o dado de uma pessoa nossa depois que ele sai daqui?

**Limite deste levantamento.** A rede desta sessão bloqueia busca direta das
páginas. O que está aqui vem de resultados de busca que citam a documentação
oficial, não das páginas lidas por inteiro. Cada linha tem a fonte. Antes de
qualquer decisão que custe dinheiro ou exponha dado, a página correspondente
tem que ser aberta e lida.

---

## 1. Como cada um se identifica para nós

Este é o eixo onde eles divergem, e é o que decide quem consegue conectar.

| | CIMD | DCR | Credencial estática | Transporte |
|---|---|---|---|---|
| **Claude** | sim | sim | sim (*Advanced settings*) | Streamable HTTP |
| **ChatGPT** | sim, se o servidor anunciar | — | sim, e tem precedência | Streamable HTTP e SSE |
| **Gemini Enterprise** | não | não | **só isso** | **só Streamable HTTP** |
| **Copilot Studio** | não citado | sim, com e sem discovery | sim | Streamable HTTP |

**A Treesy hoje oferece só CIMD.**

Consequência direta, e é a descoberta que justifica o levantamento:
**Claude e ChatGPT conectam. Gemini Enterprise e Copilot Studio não conseguem
conectar.** Não é preferência nem afinidade — é que a única porta que a gente
abriu não existe do lado deles.

Detalhes que importam:

- **ChatGPT** aceita `none` (cliente público) e `private_key_jwt`
  (asserção assinada). Se houver credencial estática configurada, ela é usada
  e a CIMD nem entra.
- **Gemini Enterprise** pede `client_id`, `client_secret`, URL de autorização
  e URL de token, preenchidos à mão, com um botão *Verify Auth*. Exige
  certificado TLS de autoridade publicamente confiável — autoassinado é
  recusado.
- **Copilot Studio** tem três modos: *Dynamic Discovery* (DCR + descoberta),
  *Dynamic* (DCR com endpoints à mão) e *Manual* (estático). A certificação
  exige pelo menos um método aprovado: OAuth 2.0 (preferido), chave de API ou
  Basic.
- **Claude** é o mais permissivo dos quatro: aceita os três caminhos.

**O que fazer com isso.** Emitir credencial estática — um `client_id` e um
`client_secret` que a gente gera para quem pedir. É pouco código, usa o
`/token` que já existe, e é a única coisa que abre Gemini Enterprise e Copilot
Studio. Não substitui a CIMD; convive.

---

## 2. Onde eles concordam

Em tudo que não é registro de cliente, os quatro pedem a mesma coisa:

- OAuth 2.1, código de autorização com **PKCE S256**.
- O servidor é *resource server*: valida o token a cada chamada.
- Descoberta por `.well-known` — RFC 9728 (recurso protegido) e RFC 8414
  (servidor de autorização).
- Streamable HTTP.

Isso a Treesy já tem, inteiro, e foi provado em produção.

E concordam em mais uma coisa, que ninguém anuncia:

- **Nenhum dos quatro tem como receber uma resposta depois.**

---

## 3. Assíncrono: o estado real

Esta parte foi levantada porque a pergunta era se dá para devolver a resposta
ao agente sem ele perguntar de novo.

- A especificação **2026-07-28** tirou *Tasks* do núcleo experimental e a
  colocou como extensão `io.modelcontextprotocol/tasks`, **baseada em
  consulta** — `tasks/get`, `tasks/update`.
- A proposta de webhook (**PR #593**) foi **fechada**, em favor de um
  mecanismo de gatilhos mais geral que ainda não existe.
- O roadmap põe isso no Grupo de Trabalho de *Triggers & Events*: canais e
  assinaturas para entrega por push, webhook incluído, com o objetivo
  declarado de acabar com a dependência de consulta pelo cliente. **É plano.**
- **Nenhum cliente implementou Tasks.** Há pedido aberto no ChatGPT
  (*Developer Mode* e *Web*) e no Claude Code (issue #76571).

Ou seja: não existe hoje nem a versão com consulta. Não é que o webhook falte
— **o assíncrono inteiro falta.** Não há endereço para empurrar nada, em
nenhum dos quatro.

Isso confirma, com documentação, o que estava sendo tratado como intuição: a
volta da resposta tem que chegar na pessoa, porque não existe caminho até o
agente.

---

## 4. O que acontece com o dado depois que ele sai daqui

A parte que decide o que a gente pode devolver.

**Claude.** O dado trocado com servidores MCP — **definições de ferramenta e
resultados de execução** — é retido conforme a política padrão de retenção.
O conector MCP **não é coberto por ZDR** (retenção zero). Em conta de
consumidor: 30 dias por padrão, e **cinco anos** se a pessoa aceitou uso para
treino. Em conta comercial: não é usado para treino por padrão.

**ChatGPT.** Em Business, Enterprise e Edu, dado vindo de conectores **não é
usado para treino por padrão**; criptografado em trânsito e em repouso;
conversas apagadas somem em até 30 dias; retenção controlada pelo
administrador do workspace. Para conta de consumidor não achei declaração
específica sobre conector — **lacuna, precisa ser lida na fonte.**

**Gemini Enterprise e Copilot Studio.** Não levantado. Lacuna.

### O que isso significa na prática

Quando a Treesy devolve o telefone de alguém numa resposta de ferramenta,
esse telefone passa a viver na infraestrutura da plataforma, sob a política
**dela**, por um prazo que **a pessoa da Treesy não escolheu e não conhece** —
e que no pior caso documentado é cinco anos, com uso para treino.

A Treesy não tem contrato de operador com nenhuma delas. Quem aceita os termos
é o dono da conta do agente, não a pessoa cuja página foi lida.

Isso não é argumento contra devolver dado. É argumento contra devolver dado
**a mais**. O que sai tem que ser o que foi perguntado, e nada além — e a
regra não é de bom gosto, é de prazo de retenção que a gente não controla.

É exatamente o que o `read_person` já faz, e é por isso que o teste que
proíbe telefone e documento na leitura para agente é o teste mais importante
do repositório.

---

## 5. O que este levantamento decide

1. **Emitir credencial estática.** Sem isso, Gemini Enterprise e Copilot
   Studio ficam de fora. É a única coisa aqui que abre mercado.
2. **Não construir webhook.** Não existe para onde apontar, e a proposta que
   existia foi fechada.
3. **Manter a volta pela pessoa** — e-mail e push. Não é contorno; é o único
   caminho que existe.
4. **Classificar campo a campo o que pode sair.** A retenção do outro lado é
   longa, alheia e, num dos casos, alimenta treino. O que não sai não é retido.
5. **Quando o push do protocolo existir, publicar só aviso vazio** — um
   identificador opaco, corpo sem dado pessoal, leitura autenticada depois.

---

## 6. Ferramenta de desenvolvedor não é a mesma coisa que app de conversa

Levantado depois, porque a pergunta "os chineses têm?" revelou que duas coisas
diferentes estavam sendo contadas como uma.

**Ferramenta de quem programa** — Qwen Code, Kimi Code, Cursor, VS Code,
Cline, os *harnesses* do DeepSeek. São muitas, e várias falam MCP remoto com
OAuth: o Qwen Code abre o navegador para autorizar, documentado pela Alibaba.

**Não serve para a Treesy.** Roda no terminal. A dona do salão não chega por
aí, e é ela que precisa chegar.

**App de conversa onde uma pessoa comum adiciona um conector** — Claude e
ChatGPT. Mais dois produtos corporativos, Gemini Enterprise e Copilot Studio.
São quatro.

### Chineses: não sei, e isso está registrado como não sei

O que achei de oficial é da Alibaba, e é plataforma de desenvolvedor: o Model
Studio conecta a MCP, e os catálogos Bailian e ModelScope têm mercado de
servidores MCP com OAuth tratado — mas é catálogo curado deles, não "cole uma
URL qualquer". Existe um QwenWork com gestão de conectores, aparentemente o
equivalente do Gemini Enterprise; **não foi aberto.**

De DeepSeek, Kimi e Doubao só apareceu blog de terceiro. **Não é fonte.**
Fica como lacuna, não como ausência.

### O que isso muda

A lista de lugares onde uma pessoa comum consegue conectar é **curta**, e dois
dos quatro são produto corporativo.

Logo: **credencial estática mais CIMD cobre o mercado praticamente inteiro.**
Não é trabalho que se repete a cada cliente novo — é trabalho que fecha a
conta.

E confirma de onde vem a pessoa comum: não é do conector. É do endereço
`treesy.me/familia-mancini` e do QR Code. O conector é para quem já tem
agente.

### Fontes desta seção

- [Conectar a MCP pela API do Qwen](https://www.alibabacloud.com/help/en/model-studio/mcp)
- [Gestão de conectores — QwenWork](https://www.alibabacloud.com/help/en/qwenwork/connectors-management)
- [Servidor MCP da OpenAPI da Alibaba Cloud](https://www.alibabacloud.com/help/en/openapi/user-guide/openapi-mcp-server-guide)

---

## Fontes

Protocolo:
- [Especificação 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28)
- [A especificação 2026-07-28 (blog)](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [O novo roadmap do MCP](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/)
- [Evolução do registro de cliente OAuth](https://blog.modelcontextprotocol.io/posts/client_registration/)
- [Operações assíncronas no MCP (discussão #491)](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/491)
- [SEP-1391: operações de longa duração](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1391)
- [Tasks no cliente do Claude Code (issue #76571)](https://github.com/anthropics/claude-code/issues/76571)

Claude:
- [Conectores personalizados com MCP remoto](https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)
- [Servidores MCP remotos](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers)
- [Conector MCP](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector)
- [API e retenção de dados](https://docs.anthropic.com/en/docs/build-with-claude/zero-data-retention)
- [Por quanto tempo os dados são guardados](https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-personal-data)

ChatGPT:
- [Construindo servidores MCP](https://developers.openai.com/api/docs/mcp)
- [Developer mode e apps MCP](https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta)
- [Privacidade empresarial](https://openai.com/enterprise-privacy/)
- [Apps conectados no ChatGPT](https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt)

Gemini Enterprise:
- [Configurar servidor MCP personalizado](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server)

Copilot Studio:
- [Conectar a um servidor MCP existente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent)
- [Certificação de servidor MCP](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-server-certification)
