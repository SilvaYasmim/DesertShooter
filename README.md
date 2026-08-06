# 🏜️ Desert Shooter

Jogo 2D de tiro (shoot 'em up) com rolagem lateral, desenvolvido em **Python** com **Pygame**, como Atividade Prática da disciplina de Linguagem de Programação Aplicada (Uninter — Análise e Desenvolvimento de Sistemas).

## Descrição

O jogador enfrenta duas fases (Deserto e Montanhas), desviando e atirando em inimigos, até alcançar a tela de vitória com a pontuação final.

## Tecnologias

- Python 3
- Pygame 2.6.1

## Como jogar

### Requisitos
```
pip install -r requirements.txt
```

### Executar
```
python main.py
```

### Controles
- **Setas direcionais**: mover o personagem
- **Espaço**: atirar
- **Enter**: confirmar opção no menu

## Modos de jogo

- Novo Jogo 1 Jogador
- Novo Jogo 2 Jogadores — Cooperativo
- Novo Jogo 2 Jogadores — Competitivo
- Pontuação (Score)

## Estrutura do projeto

```
GameDesertShooter/
├── main.py              → Ponto de entrada do jogo
├── requirements.txt      → Dependências (Pygame)
├── asset/                → Imagens, sons e músicas
└── code/
    ├── game.py           → Loop principal e transição entre telas/fases
    ├── menu.py           → Tela de menu e seleção de modo
    ├── level.py          → Lógica de cada fase
    ├── entity.py         → Classe base das entidades do jogo
    ├── entityFactory.py  → Criação de entidades (jogador, inimigos, tiros)
    ├── player.py         → Lógica e controles do jogador
    ├── enemy.py          → Lógica dos inimigos
    ├── PlayerShot.py      → Tiros do jogador
    ├── EnemyShot.py       → Tiros dos inimigos
    ├── EntityMediator.py  → Coordenação/colisões entre entidades
    ├── background.py     → Rolagem do cenário (parallax)
    └── const.py          → Constantes do jogo (cores, velocidades, opções de menu)

```

## Condições de vitória e derrota

- **Vitória**: completar a Fase 1 (Deserto) e a Fase 2 (Montanhas), chegando à tela "Missão Cumprida" com a pontuação final.
- **Derrota**: perder todos os pontos de vida (3) ao ser atingido pelos inimigos.

## Autora

Yasmim Luana Ferreira da Silva — Bacharelado em Análise e Desenvolvimento de Sistemas (Uninter)
