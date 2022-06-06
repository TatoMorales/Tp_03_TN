#!/usr/bin/env python3
import msvcrt
from re import A
import time
import mapping
import random
from human import Human
from items import Item
from actions import *
from gnome import Gnome

ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    # initial parameters
    #level = 0
   # name = input('como queres que me llame?')

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    player = Human('heroe',dungeon.find_free_tile())
    gnome = Gnome('gnome',dungeon.find_free_tile())

    sword = items.Sword("sword", "/" , 20 , 40 )
    pickaxe = items.PickAxe("pickaxe", ")")
    
    
    dungeon.render(player)
    location = player.index()
    xy = get_loc_up(dungeon,location)
    dungeon.render(player)
    print(player.loc())
    print(xy)
    print(dungeon.loc(xy))