🦀 🤠 Explorando as forças do mangue!!!

É um momento importante para a carreira do explorador Ricardo Jones...Chegou a hora de invocar as forças culturais de ninguém menos que Chico Science !!! Se prepare para ajudar nosso protagonista nessa jornada manguelística! Aviso: Cuidado com as patolas cortantes dos carangueijos protetores...eles não deixam qualquer um passar pelo santuário MangueBeat...prove que Ricardo Jones é merecedor dessa conquista!
1. Título e membros da equipe
Ricardo Jones...Uma aventura MANGUEBEAT
Membros:

Samuel de Almeida Farias Nascimento


2. Arquitetura do Projeto
O jogo foi desenvolvido com Pygame e estruturado em diferentes arquivos para melhor organização:

main.py: controla o funcionamento geral do jogo, contendo as instâncias principais de todos os outros arquivos do projeto.
coletaveis.py: define a classe "Coletavel" para ser aplicada aos objetos que o player coleta durante o jogo.
colisoes.py: lida com o comportamento do player durante a interação física com os coletáveis e com os inimigos.
inimigo.py: define a movimentação e o comportamento do inimigo durante o jogo.
mapas.py: programa a alternância entre os diferentes cenários de acordo com a movimentação do player.
player.py: define a classe player, programando a movimentação desse objeto através das teclas W, A, S e D.


3. Capturas de Tela

4. Ferramentas, bibliotecas e frameworks utilizados
Python 3.13.7
Pygame: biblioteca principal usada para renderização, eventos e lógica do jogo.
Justificativa:
O pygame possui umna ampla gama de informações de uso, além de lidar com os aspectos mais complexos de baixo nível, permitindo que você se concentre nos conceitos fundamentais de desenvolvimento de jogos, como game loop, detecção de colisão, gerenciamento de sprites e estados do jogo.

6. Divisão de trabalho
Samuel: Fez o README, a tela principal 
Guilherme: Fez o mapas.py, colisoes.py, e conectou as mudanças dos mapas com o player, 
Gabriel Brum: Fez o sistema de 
Gabriel Ribeiro: Fez parte dos sprites, ajudou nos slides e deu suporte no ajuste da movimentação e das fases.
Eduardo: Fez parte dos sprites, os slides, o README do projeto e ajudou no desenvolivimento dos inimigos.
Thiago: Fez parte dos sprites, ajudou nos slides e atuou dando suporte nos códigos.
8. Conceitos da disciplina utilizados
Programação Orientada a Objetos: todo o jogo é baseado em classes com encapsulamento e herança.
Tratamento de eventos: uso intensivo de eventos do Pygame.
Listas e estruturas de dados: armazenam balas, inimigos e itens coletáveis.
Controle de fluxo: loops aninhados para menus, fases e transições.
Modularização: separação do código em múltiplos arquivos.
9. Desafios, erros e lições aprendidas
Erro maior:
Mudança de lógica de movimentação do jogador muito tarde (de cenário fixo para o personagem fixo no centro), o que exigiu reestruturar grande parte do código em pouco tempo.

Maior desafio:
Implementar essa nova movimentação e, ao mesmo tempo, manter a lógica de colisão, spawn de inimigos e coleta de itens funcionando.
Animação dos inimigos.
Lições aprendidas:
Refatorar o código cedo evita retrabalho.
Organização no GitHub ajuda no progresso coletivo.
Dividir tarefas e manter comunicação clara no grupo é essencial.
8. Como jogar
Requisitos:
Python 3.x instalado
Pygame instalado (pip install pygame)
Instruções:
bash git clone (https://github.com/juliaandradel/IP-GRUPO1.git) cd jogo-copa-do-mundo python main.py

Use as teclas W, A, S, D para movimentar-se e o mouse para atirar.

