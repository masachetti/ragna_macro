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

## Macro system:

O sistema de macro vai ser constituido de:

- Um ActionQueue - Vai armazenar e executar as ações presentes da queue
  - Singleton - uma unica instancia global
- Um MacroManager - Vai armazenar e controlar as macros
  - Tmb vai intermediar as macros com o ActionQueue
- Macros - Objetos reponsaveis por todo o controle do que uma macro deve fazer.

### Macro

A macro vai ser um objeto que vai conter os parametros:
- AlwaysAlive: Define se a macro será estará viva (nao depende de hotkey para ativar)
- TriggerType = Hold | Toggle : Define se a macro é ativada (pela hotkey) no tipo pressionar
ou no tipo On/Off
- HotKey : Define a key ou conjunto de keys que ativam a macro
- Action : É a função que define o comportamento da macro em si
- Condicional : É uma função que retorna True/False que checa se a action pode ser "despachada"
- Delay : É um tempo de espera que ocorre quando a macro despacha uma action
- Parametros: Parametros extras que o usuario pode passar (ex: %Hp, %Sp)

### MacroManager

O MacroManager vai:
- Carregar as macros dependendo do profile selecionado
- Criar uma thread para observar as teclas pressionadas pelo usuario
- Armazenar as macros habilitadas numa lista (AlwaysAlive + TriggeredMacros)
- Remover macros desabilitadas
- Separar as macros em espera das demais
- Colocar macros em espera quando estas depacharem uma action
- Encaminhar as Actions para a ActionQueue
- Pausar/Habilitar a execução de todas as macros

### Listagem de macros (apenas para fluir as ideias)

**Skill spam**

- Parametros: skill_key
- AlwaysAlive: False
- TriggerType: Hold
- Hotkey: Hotkey
- Action : 
  - Click Key
  - Delay
  - Click Mouse
  - Delay
- Delay : 10ms

---

**Skill + Asa de mosca**

- Parametros: skill_key, asa_de_mosca_key, map_name
- AlwaysAlive: False
- TriggerType: Toggle
- Hotkey: Hotkey
- Action : 
  - *Capturar a coordenada do char 
  - Click Skill Key
  - Delay
  - Click Mouse
  - Delay (grande)
  - Click Asa de Mosca Key
  - *Esperar até que a coordenada do char mude
    - Em caso de espera infinita -> Aborta o App -> Raise Exception
  - Delay(pequeno)
- *A checagem de coordenada pode ser substituida por um delay grande
- Condicional : 
  - Mapa ser igual ao map_name
  - Peso <85%
- Delay : 100ms
---

**AutoPot**

- Parametros: hp_percent, pot_key
- AlwaysAlive: True
- Action : 
  - Click Pot Key
  - Delay
- Condicional : 
  - Obter o Hp Atual do char
  - Obter o Hp Max do char
  - Calcular a % de HP
  - Comparar com a % definida nos parametros
- Delay : 100~500ms

---

**AutoBuff**

- Parametros: buff_code, buff_key
- AlwaysAlive: True
- Action : 
  - Click Buff Key
  - Delay
- Condicional : 
  - Obter a lista de buffs do char
  - Verificar se o buff_code está na lista de buffs
  - Caso não -> Despacha a action
- Delay : 100~500ms



