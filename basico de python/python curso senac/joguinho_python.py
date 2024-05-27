from random import randint
lista_npcs = []

player = {
    "nome": "Halyson",
    "level": 1,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,
    "exp": 0,
    "exp_max": 30
    }

def criar_npc(level):
    level += 1
    adicionar_npc = {
        "nome": f"monstro #{level}",
        "level": level,
        "hp": 100*level,
        "hp_max": 100*level,
        "dano": 5*level,
        "exp": 7,
        "exp_max": 50
    }
    lista_npcs.append(adicionar_npc)
    

def gerar_npcs(qnt):
    for x in range(qnt):
        criar_npc(x)

def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)

def exibir_npc(npc):
    print(
            f'Nome : {npc['nome']} | Level : {npc['level']} | HP {npc['hp']}/{npc["hp_max"]} | Dano : {npc["dano"]} | EXP : {npc["exp"]}/{npc["exp_max"]}'
        )

def exibir_player():
    print(
            f'Nome : {player['nome']} | Level : {player['level']} | HP {player['hp']}/{player["hp_max"]} | Dano : {player["dano"]} | EXP : {player["exp"]}/{player["exp_max"]}'
        )

def batalha(npc):
    while player['hp'] > 0 and npc['hp'] > 0:
        print('-='*30)
        atacar_npc(npc_selecionado)
        atacar_player(npc_selecionado)
        exibirinfobatalha(npc_selecionado)
    
    if npc['hp'] == 0:
        print('NPC DERROTADO!!!')
        npc['hp'] = npc['hp_max']
        player['exp'] += npc['exp']
    elif player["hp"] == 0:
        print('PLAYER DERROTADO!!!')
        player["hp"] = player["hp_max"]

    if player["exp"] >= 30:
        player["level"] += 1

    exibir_npc(npc_selecionado)
    exibir_player()
    

def atacar_npc(npc):
    npc['hp'] -= player['dano']

def atacar_player(npc):
    player['hp'] -= npc['dano']

def exibirinfobatalha(npc):
    print(f'player: {player['hp']}/{player["hp_max"]}')
    print(f'monstro: {npc['nome']} | {npc['hp']}/{npc["hp_max"]}')


    

gerar_npcs(5)
npc_selecionado = lista_npcs[0]
batalha(npc_selecionado)
batalha(npc_selecionado)
batalha(npc_selecionado)
batalha(npc_selecionado)
batalha(npc_selecionado)
batalha(npc_selecionado)
batalha(npc_selecionado)
batalha(npc_selecionado)
