# 🦀 🤠 Explorando as forças do mangue!!!

### Chegou a hora de invocar as forças culturais de ninguém menos que Chico Science !!! Se prepare para ajudar nosso protagonista nessa jornada manguelística! Aviso: Cuidado com as patolas cortantes dos carangueijos protetores...eles não deixam qualquer um passar pelo santuário MangueBeat...prove que nosso explorador é merecedor dessa conquista!
# 1. Título do Jogo💥: Uma Aventura MangueBeat

# 2. Membros🚹:
- Samuel de Almeida Farias Nascimento
- Eduardo Henrique do Rêgo Marques Cunha
- Gabriel Guimarães Brum
- Guilherme Calistrato Nunes Tavares
- Gabriel Ribeiro Lima Carleial
- Thiago José Barbosa Menezes de Oliveira
   
# 3. Arquitetura do Projeto🧱:
  ### O jogo foi desenvolvido com a biblioteca Pygame e estruturado em diferentes arquivos para melhor organização:

- main.py: controla o funcionamento geral do jogo, contendo as instâncias principais de todos os outros arquivos do projeto.ooo
- coletaveis.py: define a classe "Coletavel" para ser aplicada aos objetos que o player coleta durante o jogo.
- colisoes.py: lida com o comportamento do player durante a interação física com os coletáveis e com os inimigos.oo
- inimigo.py: define a movimentação e o comportamento do inimigo durante o jogo.o
- mapas.py: programa a alternância entre os diferentes cenários de acordo com a movimentação do player.
- player.py: define a classe player, programando a movimentação desse objeto através das teclas W, A, S e D.
- tela_inicial.py: gera o plano de fundo inical do jogo, contendo os botões de "Iniciar" e de "Instruções" / importa a função "mostrar_instrucao()".
- instrucoes.py: gera o plano de fundo de instruções, informandosobre os obejtivos e movimentação do player / estruturado a partir de uma função principal.
- interface.py: registra a quantidade de coletáveis coletador pelo player / mostra na tela esse registro.    


# 4. Capturas de Tela 📸:
- Testando as movimentações básicas.
<img width="500" height="403" alt="Captura de Tela (462)" src="https://github.com/user-attachments/assets/2c6d0b44-73b3-4a67-b494-cbd7ee49325b" />


- Testando perseguição inimigo -> player.
<img width="500" height="395" alt="Captura de Tela (463)" src="https://github.com/user-attachments/assets/78541df0-e8d5-4350-b78c-9ff9fe013f87" />

    
- Incluindo os sprites e o cenário.
<img width="500" height="281" alt="arquivo png" src="https://github.com/user-attachments/assets/aca3b319-f1d0-4c4a-9545-1ea8bfa32c65" />


- Atualizando as sprites e o cenário / adicionando os coletáveis
<img width="500" height="347" alt="Captura de Tela (464)" src="https://github.com/user-attachments/assets/15d7ba27-94ee-4ad9-b29a-d6d6f6243873" />
    

# 5. Ferramentas, bibliotecas e frameworks utilizados 🛠:
### Python 3.13.7
### Biblioteca Pygame : biblioteca principal usada para renderização, eventos e lógica do jogo.
- O pygame possui uma ampla gama de informações de uso, além de lidar com os aspectos mais complexos de baixo nível, permitindo que você se concentre nos conceitos fundamentais de desenvolvimento de jogos, como game loop, detecção de colisão, gerenciamento de sprites e estados do jogo.

# 6. Divisão de trabalho 📝:
  - Samuel: Fez o README, o tela_inicial.py e o instrucoes.py.
  - Guilherme: Fez os mapas, colisões e suas lógicas
  - Gabriel Brum: Fez os inimigos e a lógica de perseguição
  - Gabriel Ribeiro: Fez o player.py e a movimentação do jogador
  - Eduardo: Fez os Coletáveis, HUD e efeitos sonoros
  - Thiago: Fez main_2.py, sprites do Sprites-possíveis, slides.

# 7. Conceitos de Programação utilizados 📚:
  - Programação Orientada a Objetos: Excluindo o arquivo main(), todos os outros arquivos possuem a definição de classes para instanciação no arquivo main().
  - Estruturas de Controle de:
    1.  Dados: Uso de listas e variáveis para o registro e a contagem dos coletáveis.
    2.  Fluxo: loops aninhados para diversas funções, tais como a visibilidade do jogo na tela e a análise dos coletávies.
  - Modularização: separação do código em vários arquivos.

# 8. Aprendizados e Desafios 📈:
- Dificuldade com a lógica do github: Aprendemos muito sobre como gerenciar arquivos e versões no github.
- Funções nativas do pygame: Compreendemos a ideia das funções básicas da biblioteca do pygame e como usá-las ao nosso favor.
- Construção do código em equipe: Gerenciar o jogo em equipe exige muita comunicação, e durante o projeto evoluímos bastante nesse tópico, sempre dando feedbacks e alinhando os objetivos e tarefas de cada membro.


# 9. Como jogar 💻:
### Requisitos:
- Python 3.x instalado.
- Pygame instalado (pip install pygame).
### Instruções:
- Acesse nosso código em nosso repositório github: https://github.com/safn007/Projeto-Final-IP---CC---2025.2.git
- Use as teclas W, A, S, D para movimentar oplayer, fugir dos carangueijos defensores e coletar os itens.

## BOM JOGO! SE DIVIRTA NESSA INCRÍVEL AVENTURA MANGUEBEAT!

