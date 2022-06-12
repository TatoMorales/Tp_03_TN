from typing import Union
import items
import mapping
import player


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def attack(dungeon, player, gnome): 
    # completar
    raise NotImplementedError
#%%
def set_move(dungeon: mapping.Dungeon, player, location):
    player.loc()
    player.x, player.y = location
    return player.x,player.y

def get_loc_up(dungeon: mapping.Dungeon, location):
    x, y = location
    y -= 1  
    xy = x, y
    return xy

def get_loc_down(dungeon: mapping.Dungeon, location):
    x, y = location
    y += 1  
    xy = x, y
    return xy

def get_loc_left(dungeon: mapping.Dungeon, location):
    x, y = location
    x -= 1  
    xy = x, y
    return xy

def get_loc_right(dungeon: mapping.Dungeon, location):
    x, y = location
    x += 1  
    xy = x, y
    return xy
#%%
def move_to(dungeon: mapping.Dungeon, player: player.Player, location):
    player.loc#ubicacionactual
    raise NotImplementedError


def move_up(dungeon: mapping.Dungeon, player: player.Player):
    player.loc()
    player.y -= 1   
    return player.x, player.y


def move_down(dungeon: mapping.Dungeon, player: player.Player):
    player.loc()
    player.y += 1
    return player.x, player.y


def move_left(dungeon: mapping.Dungeon, player: player.Player):
    player.loc()
    player.x -= 1
    return player.x, player.y


def move_right(dungeon: mapping.Dungeon, player: player.Player):
    player.loc()
    player.x += 1
    return player.x, player.y


def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    if player.loc() == dungeon.index(mapping.STAIR_UP):
        dungeon.level -= 1
        print("Subiendo...")
    return dungeon.level 


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    if player.loc() == dungeon.index(mapping.STAIR_DOWN):
        dungeon.level += 1
        print("Bajando...")
    return dungeon.level


def pickup(dungeon: mapping.Dungeon, player: player.Player, item: items.Item):
    if player.loc() == item.loc():
        return item.loc()

    
