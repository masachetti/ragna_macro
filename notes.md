# Notes

Como pretendo fazer com python, alguns requisitos precisam ser 
cumpridos para funcionar com essa lang.
Caso não de certo com python, vou ter que aprender C# =)

- Ler os endereços de memoria Ok
- Wrappear o processo do rag OK 
- Enviar comandos de tecla pressionada para o processo do rag (isso já funcionava) OK
- Enviar comando de mouse click (isso eu acho q nao funcionava)  Ok

Funcionalidades que quero colocar na macro:

- Spam de skill
- Soltar skill (tempestade) e depois usar asa de mosca
- Após usar asa de mosca, checar se o Tp aconteceu (pelas coords. e pelo mapa)
- Só quando o tp acontecer executar novamente a rotina
  - Isso é pra previnir o spam de skill antes do TP acontecer
  - Deve previnir do char catar item do chao
- Auto pot (hp e mana)
- Auto buff
  - Usando o @buff (alt +2)
  - Concentração
  - Bagri
  - Garantir que o auto buff nao aconteça no meio do TP
- Pause da macro em condições especificas:
  - Mapa diferente do mapa definido
  - Status de muito peso
- Restock de flechas
  - (Ainda nao consegui ler na memoria a quantidade de flechas)
  - Talvez de pra fazer usando algum analisador de imagem
  - Uma possibilidade é estipular um numero X de vezes que a macro vai ser executada
  - por exemplo: 30k flechas = 3k execuções
  - Acabou, para a macro e roda um spam da aljava pra repor as flechas
    - O problema é sempre ter 30k de flechas qnd começar a macro


Endereços conhecidos:

- Curent HP: 0x011D1A04
- Buffs: 0x011D1E78 (a cada 4 tem um buff)
  - Tem que checar melhor, mas aparentemente os buffs começam em : 0x011D1E84
- Current SP:
- Mapa: ta no codigo
- Coordenadas(X,Y):
- Flechas: ???

Constantes:

- Bagri ID:
- @buff Ids
- Concentração Id: