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
    
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).
    for floor in dungeon.dungeon:
        dungeon.add_item(sword, 1)
        dungeon.add_item(pickaxe, 1)
        turns = 0
        while dungeon.level >= 0:
            turns += 1
            # render maps
            print(player.loc())
            dungeon.render(player)

            item_adquired = dungeon.get_items(player.loc())
            if len(item_adquired) >= 1:
                if item_adquired[0] == sword:
                    print("El jugador ha obtenido la espada")
                    player.weapon = True
                    player.has_sword()
                elif item_adquired[0] == pickaxe:
                    print("El jugador ha obtenido el pico")

            climb_stair(dungeon, player)
            descend_stair(dungeon, player)

            key = msvcrt.getch().decode('UTF-8')
            if key == "w":
                move_up(dungeon,player)
            elif key == "a":
                move_left(dungeon,player)
            elif key == "s":
                move_down(dungeon, player)
            elif key == "d":
                move_right(dungeon, player)
        
    print("GAME OVER")
            
             
        
        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego
