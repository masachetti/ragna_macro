# Notes

Proximos passos:

- Possibilitar multi keys hotkeys

- Fazer tratamento de erros basicos (ex: qnd inicia o app sem um client do rag aberto)
- Criar uma maneira de fechar o app de maneira mais segura e mais adequada
- Achar uma maneira de criar uma release do app
  - Update: Pyinstaller é uma opção, porém fica meio fora do proposito do app de ser uma tool para desenvolvimento


Proximos passos agora:

- Add um listener para o botão backspace para poder voltar para a tela de seleção de profile
  - O botão End já faz isso, mas dentro do Macro monitor como uma abort key
  - Transferir o listener do botao para dentro do App (uma vez q o cursers será executado la)
  - Criar um method de Abort no macro monitor ao em vez de ser via Event
- Fazer com que o App cuide da screen (oq é mais obvio)
  - Fazer com que o macro monitor seja um pedaço da screen do app (ele recebe a screen pelo App)
  - Adicionar um cabeçalho do App informando os botões de pause e retorno
  - Adicionar um cabeçalho do Macro monitor informando o nome do profile
- Criar maneiras de fechar o app de maneira mais segura