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

AIR = mapping.Tile(' ')

if __name__ == "__main__":
    # initial parameters
    #level = 0
   # name = input('como queres que me llame?')

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    player = Human('heroe',dungeon.find_free_tile())
    gnome = Gnome('gnome',dungeon.find_free_tile())

    sword = items.Sword("sword", "/" , 20 , 40 )
    pickaxe = items.PickAxe("pickaxe", ")")
        
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
                    player.tool = True
                    player.has_pickaxe()
                    print("El jugador ha obtenido el pico")

            climb_stair(dungeon, player)
            descend_stair(dungeon, player)

            key = msvcrt.getch().decode('UTF-8')
            if key == "w":
                location = player.loc()
                xy = get_loc_up(dungeon,location)
                if dungeon.is_walkable(xy) == True:
                    set_move(dungeon, player, xy)
                else: 
                    if player.has_pickaxe: 
                        dungeon.dig(xy)
            elif key == "a":
                location = player.loc()
                xy = get_loc_left(dungeon,location)
                if dungeon.is_walkable(xy) == True:
                    set_move(dungeon, player, xy)
                else: 
                    if player.has_pickaxe: 
                        dungeon.dig(xy)
            elif key == "s":
                location = player.loc()
                xy = get_loc_down(dungeon,location)
                if dungeon.is_walkable(xy) == True:
                    set_move(dungeon, player, xy)
                else: 
                    if player.has_pickaxe: 
                        dungeon.dig(xy)
            elif key == "d":
                location = player.loc()
                xy = get_loc_right(dungeon,location)
                if dungeon.is_walkable(xy) == True:
                    set_move(dungeon, player, xy)
                else:
                    if player.has_pickaxe: 
                        dungeon.dig(xy)
            
