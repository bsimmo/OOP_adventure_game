from room import Room
from item import Item
from rpginfo import RPGInfo
from character import Character, Enemy, Animal

# game settings
game_name = "Adventure around the house"
RPGInfo.author = "Raspberry Pi Foundation and Me"

# setup rooms
kitchen = Room("kitchen")
kitchen.description= "a dank and dirty room buzzing with flies"

ballroom = Room("ballroom")
ballroom.description = "a large clean room with a sparkling floor"

dining_hall = Room("dining hall")
dining_hall.description = "a dimly lit room with scraps of food surrounding a table"

office = Room("office")
office.description = "a small room with bright LED lighting, looks a nice place to work"

garden = Room("garden")
garden.description = "a large space, recently mown.  There is a large stone in the corner"

#setup room maze
kitchen.link_room(dining_hall, "south")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(garden, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(office, "south")
office.link_room(dining_hall, "north")
office.link_room(garden, "west")
garden.link_room(office, "east")
garden.link_room(ballroom, "north")

# setup items
table = Item("table")
table.description = "round and has places for four people"
table.mass = "heavy"
table.material = "metal"

sword = Item("sword", "light", "wood")
sword.description = "long and pointy with a small handle, it has lots of small holes in it"

cheese = Item("cheese", "light", "cheese")
cheese.description = "Smelly, a little bit gooey"

metal_key = Item("metal_key", "heavy", "iron")
metal_key.description = "large rusty old key, seems a little bent"

plastic_key = Item("plastic_key", "light", "plastic")
plastic_key.description = "a 3D printed key, red in colour.  You can see the layer lines"

# setup items in rooms
dining_hall.item = table
kitchen.item = cheese
garden.item = sword


#setup characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains... no like.s.ords")
dave.set_weakness("sword")

pam = Enemy("Pam", "A glowing zombie afraid of swords")
pam.set_conversation("foood....fooood,")
pam.set_weakness("sword")

fred = Character("Fred", "Busy making computer games")
fred.set_conversation("Sorry, to busy. Send me an email")

cat = Animal("Cat", "Laid down, half sleeping. Acts like it owns the place")
cat.set_huggable(True)
cat.set_food("cheese")
cat.set_hug_sound("purrrrr")

#setup character items
pam.item = metal_key
fred.item = plastic_key

#setup character locations
dining_hall.character = dave
office.character = fred
kitchen.character = cat 
ballroom.character = pam 


#set starting room
current_room = kitchen


#start game
alive = True
storage = [] # players items
the_game = RPGInfo(game_name)
the_game.welcome()
RPGInfo.info()
the_game.rules()


print(f"There are {str(Room.number_of_rooms)} rooms to explore.\ntype help for command and more information")


while alive:
    current_room.get_details()
    inhabitant = current_room.character
    
    if inhabitant is not None:
        inhabitant.describe()
    
        # loop so we don't display room details after every action.
    while True:
        command = input(f" What would would you like to do? >")
        
            # Check whether a direction was typed
        if command in ["north", "south", "east", "west"]:
            in_room = current_room
            current_room = current_room.move(command)
            if current_room == in_room:
                pass
            else:
                break # Moved so we need to start the main loop again
        
        elif command == "talk":
            if inhabitant is not None:
                inhabitant.talk()
        
        elif command == "fight":
            if isinstance(inhabitant, Enemy):
                fight_item = input(f" What item do you want to use >?")
                if fight_item in storage:
                    print(f"You take out the {fight_item} and lunge towards {inhabitant.name}")
                    if inhabitant.fight(fight_item):
                        current_room.character = None
                    else:
                        print(f"You died, they are not weak to a {fight_item}")
                        alive = False
                        break # You're dead, so no more action, break this while and the the main while using above
                else:
                    print(f"You do not have a {fight_item}")
            else:
                print(f"You cannot fight anyone")

        elif command == "info":
            break
        
        elif command == "help":
            print(f"\n\n### ### ###")
            the_game.commands()
            the_game.rules()
            print(f"In the {the_game.storage} you have", end="; ")
            if len(storage) == 0:
                print(f"There is nothing in your {the_game.storage}")
            else:
                for item in storage:
                        print(f"{item.name}", end=", ")
                print("")
            
        elif command == "feed":
            if isinstance(inhabitant, Animal):
                feed_item = input(f" What item do you want to use >?")
                if feed_item in storage:
                    if inhabitant.feed(feed_item):
                            storage.remove(feed_item)
                            current_room.character = None
                            print(f"{inhabitant.name} has left the room")
                else:
                    print(f"you do not have {feed_item}")
            else:
                print(f"you cannot feed anyone")

        elif command == "hug":
            if isinstance(inhabitant, Animal):
                inhabitant.hug()
            
            elif isinstance(inhabitant, Enemy):
                print(f"{inhabitant.name} is an Enemy")
            
            else:
                print(f"nothing to hug")
                
        elif command == "steal":
            if inhabitant is not None:
                steal_item = input(f" What item do you want to steal >?")
                if isinstance(inhabitant, Enemy):
                    if inhabitant.steal(steal_item) is False:
                        alive = False
                        break # You're dead, so no more action, break this while and the the main while using above
                    print(f"you have stolen the {steal_item} and placed it in the {the_game.storage}")
                    storage.append(inhabitant.item)
                    inhabitant.item = None
                else:
                    print(f"you cannot steal from {inhabitant.name}")
            else:
                print(f"There is nothing to steal")
                
        elif command == "take":
            if current_room.item is not None:
                take_item = input(f" What item do you want to take >?")
                if current_room.item.name == take_item:
                    print(f"you have taken the {take_item} and placed it in the {the_game.storage}")
                    storage.append(current_room.item)
                    current_room.item = None
                elif inhabitant.item is not None and inhabitant.item.name == take_item:
                    print(f"{inhabitant.name} will not let you take the item")
                else:
                    print(f"That is not in the room")
            else:
                print(f"There is nothing to take")
                                   
        else:
            print(f"That is not a known command, type help for commands and more information")

RPGInfo.credits()