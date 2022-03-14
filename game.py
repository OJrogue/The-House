from random import choice

# texts for game , imp as text with impression for first time entering

error_message = "That's not a valid command try <help> to see available commands."

# items
torch_text = "A torch? What is it doing here. It may be useful tho. I will keep it in case it gets handy."
bottle_with_message_text = "Oh a glass bottle with a rolled piece of paper inside it. I wonder if there is anything written on it, but the lid isn't moving. Should I break it?"
lighter_text = "Woah a lighter! I wonder if it still works. Wow it does still work. Nice! It may be useful."
pickaxe_text = "Pickaxe? Here? I really wonder what was it doing here lol."
crowbar_text = "Aaaah a crowbar! This may come in handy!"
dust_text = "Just some dust there."
cobweb_text = "Uh a big pile of cobwebs."

items_texts = {
    "torch": torch_text,
    "bottle with message": bottle_with_message_text,
    "lighter": lighter_text,
    "pickaxe": pickaxe_text,
    "crowbar": crowbar_text,
    "dust":dust_text,
    "cobweb":cobweb_text
}

# rooms
location_texts = {
    'vault_imp': "Ohh nice! A vault hidden under the painting. Only problem is that it's locked.. I can either try to insert the passcode or leave.",
    'vault': "A vault hidden under the painting. Only problem is that it's locked.. I can either try to insert the passcode or leave.",

    'shelf': "Hmmm.. All the books on this shelf are still in a good shape just a bit dusty. But that's weird they only have name of the author written on the edge. Maybe they need to be put in some order to unlock something?\nbooks:\n1: Haro\n2: Sapkowski\n3: Erikson\n4: Dashner\n5: Cline\nI can either try to sort them or leave.\n(for sorting use just numbers like <12345>)",

    'start': "Welcome to the GAME!\nCommands:\n<go (left/right/forward/back/up/down)>\n<search **place**>\n<help> to see available commands\n<inventory> to see items in your inventory\n\n\nYou are standing in front of an abandoned house in the middle of nowhere. Rumor says there is a big treasure hidden inside!(type <go forward> to get in)",

    'front_hall_imp': "Nice! The front door wasn't locked. You are standing in a front hall. There is a small shoe {}. There isn't much more besides a door on the left, front and stairs on the right.",
    'front_hall': "You are standing in a front hall. There is a small {}. There isn't much more besides a door on the left, front and stairs on the right.",

    'down_bath_imp': "Woah a bathroom. It's not really in a good shape. A broken sink, shower and {}. I don't think I can find anything useful here.",
    'down_bath': "A bathroom. It's not really in a good shape. A broken sink, shower and {}. I don't think I can find anything useful here.",

    'living_room_imp': "Oh that's some old furniture here! Looks like this used to be a living room and dining room together. A {} on an old dusty carpet. A bookshelf mostly empty but just one {} still has all the books in it. Weird. Then there is just dining table with a few chairs and also a door on the right.",
    'living_room': "Some old furniture here. Looks like this used to be a living room and dining room together. A {} on an old dusty carpet. A bookshelf mostly empty but just one {} still has all the books in it. Then there is just dining table with a few chairs and also a door on the right.",

    'stairs_imp': "Hmmm, wanna go up or down?",
    'stairs': "Wanna go up or down?",

    'kitchen_imp': "A kitchen, but ew it's in a really bad shape. Few {} are barely holding onto the wall. And.. is that oven? It probably once was but it's nowhere close to being one now.",
    'kitchen': "Kitchen, but it's in a really bad shape. Few {} are barely holding onto the wall. And.. is that oven? It probably once was but it's nowhere close to being one now.",

    'working_place_imp': "This looks like a working place. {} in the middle, some empty shelves but this is interesting! A deer {} on the wall. I'm surprised it's still intact!",
    'working_place': "Working place. {} in the middle, some empty shelves but this is interesting! A deer {} on the wall. I'm surprised it's still intact!",

    # 'up_hallway_imp': "Empty hallway, just one door on the top and on the left.",
    'up_hallway': "Pretty much an empty hallway, just one door in front and on the left.",

    'bedroom_imp': "This must have been a bedroom. A {} under a window with remains of a night desk next to it. A door in front, that's probably a bathroom. But this is weird a {} but it's blocked with planks? I wonder if I can open it somehow.",
    'bedroom': "Bedroom. A {} under a window with remains of a night desk next to it. A door in front. But this is weird a {} but it's blocked with planks? I wonder if I can open it somehow.",

    'up_bath_imp': "Just like I thought! A bathroom. Remains of a shower and sink but the {} seems in a good shape still. I wouldn't use it tho.",
    'up_bath': "A bathroom. Remains of a shower and sink but the {} seems in a good shape still. I wouldn't use it tho.",

    'basement_stairs': "It's pretty dark in here! There's just a little light coming from a crack in wall on the right but I still can't see to the end of this basement. Will need some light to look there.",
    'only_torch_basement': "It's pretty dark in here! There's just a little light coming from a crack in wall on the right but I still can't see to the end of this basement. I have a torch but nothing to light it with..",
    'only_lighter_basement': "It's pretty dark in here! There's just a little light coming from a crack in wall on the right but I still can't see to the end of this basement. I have a lighter but it's not making enough light.. maybe i can find something to light up.",

    'basement_imp': "It's pretty dark in here! There's just a little light coming from a crack in wall on the right but I still can't see to the end of this basement. Thankfully I have the torch and lighter. Wait a sec I will make some light! Looks like there's just hallway going forward leading to an armored door. Oh, it has three key holes.",
    'basement': "Looks like there's just hallway going forward leading to an armored door. The door has three key holes.",

    'end': "YES!! So the rumour was indeed true! A whole room filled with gold! I don't even know how will I carry this out!\n\nThanks for playing!\nMade by @\_OJ\_#4248\n[source code](https://github.com/OJrogue/The-House)"
}

movement = {
    'start': {'forward': 'front_hall'},
    'front_hall': {'left': 'down_bath', 'forward': 'living_room', 'right': 'stairs', 'up': 'up_hallway'},
    'down_bath': {'right': 'front_hall'},
    'living_room': {'right': 'kitchen', 'back': 'front_hall'},
    'stairs': {'up': 'up_hallway','left':'front_hall'},
    'kitchen': {'left': 'living_room'},
    'working_place': {'back': 'up_hallway'},
    'up_hallway': {'forward': 'working_place', 'left': 'bedroom', 'back': 'stairs', 'down': 'front_hall'},
    'bedroom': {'forward': 'up_bath', 'right': 'up_hallway'},
    'up_bath': {'back': 'bedroom'}
}

search = {
    'down_bath': 'toilet',
    'living_room': ['shelf', 'sofa'],
    'kitchen': 'cabinets',
    'working_place': ['painting', 'table'],
    'bedroom': ['closet','bed'],
    'up_bath': 'toilet',
    'front_hall': 'cabinet',
}


# game class
class Game:

    def __init__(self):
        self.location = "tutorial"
        self.inventory = []
        self.items = ["torch", "bottle with message", "lighter", "pickaxe", "crowbar", "dust", "cobweb"]

        self.bottle_with_message_location = ""

        self.vault_imp = True

        self.basement_door_imp = True

        self.items_loc = {
            'down_bath': ["**toilet**"],
            'living_room': ["**sofa**", "**shelf**"],
            'kitchen': ["**cabinets**"],
            'working_place': ["**Table**", "**painting**"],
            'bedroom': ["**bed**","**closet**"],
            'up_bath': ["**toilet**"],
            'front_hall': ["**cabinet**"]
        }

        self.loc_texts = {
            'front_hall': location_texts['front_hall_imp'],
            'down_bath': location_texts['down_bath_imp'],
            'living_room': location_texts['living_room_imp'],
            'stairs': location_texts['stairs_imp'],
            'kitchen': location_texts['kitchen_imp'],
            'working_place': location_texts['working_place_imp'],
            'up_hallway': location_texts['up_hallway'],
            'bedroom': location_texts['bedroom_imp'],
            'up_bath': location_texts['up_bath_imp'],
            'vault': location_texts['vault_imp'],
            'shelf': location_texts['shelf'],
            'start': location_texts['start'],
            'basement':location_texts['basement_imp']
        }

    # returns inventory formatted to text
    def inv(self):
        if len(self.inventory) == 0:
            return "You don't have anything in your inventory."
        else:
            inv_text = "Inventory: "
            for item in self.inventory:
                inv_text = inv_text + item
                if not item == self.inventory[-1]:
                    inv_text = inv_text + ", "
            return inv_text

    # add item
    def additem(self):
        item = choice(self.items)
        self.items.remove(item)
        if item not in ['dust','cobweb']:
            self.inventory.append(item)
        return item

    # search command
    def search(self, place):
        if place == 'painting' and self.items_loc['working_place'][1] == "**painting**":
            self.location = 'vault'
            if self.vault_imp:
                self.vault_imp = False
                return location_texts['vault_imp']
            return location_texts['vault']
        elif place == 'shelf' and self.items_loc['living_room'][1] == "**shelf**":
            self.location = 'shelf'
            return location_texts['shelf']
        elif place == 'closet' and self.items_loc['bedroom'][1] == '**closet**':
            if "crowbar" in self.inventory:
                self.inventory.append("Copper key")
                self.items_loc['bedroom'][1] = "closet"
                if self.loc_texts['basement'] == location_texts['basement']:
                    return "The crowbar really comes in handy!.. Woah A **COPPER KEY!** This must be somehow connected to the basement door!"
                return "The crowbar really comes in handy!.. Woah A **COPPER KEY!** This must be somehow connected to the treasure!"
            return "Doesn't seems like i can open it just like that. Maybe I can find some tool that can help with that."
        elif place == 'down_toilet' and self.items_loc['down_bath'] == ['**toilet**']:
            self.items_loc['down_bath'] = ['toilet']
            item = self.additem()
            if item == "bottle with message":
                self.bottle_with_message_location = self.location
                self.location = "bottle_with_message"
            return items_texts.get(item)
        elif place == 'sofa' and self.items_loc['living_room'][0] == '**sofa**':
            self.items_loc['living_room'][0] = 'sofa'
            item = self.additem()
            if item == "bottle with message":
                self.bottle_with_message_location = self.location
                self.location = "bottle_with_message"
            return items_texts.get(item)
        elif place == 'cabinets' and self.items_loc['kitchen'] == ['**cabinets**']:
            self.items_loc['kitchen'] = ['cabinets']
            item = self.additem()
            if item == "bottle with message":
                self.bottle_with_message_location = self.location
                self.location = "bottle_with_message"
            return items_texts.get(item)
        elif place == 'table' and self.items_loc['working_place'][0] == '**Table**':
            self.items_loc['working_place'][0] = 'Table'
            item = self.additem()
            if item == "bottle with message":
                self.bottle_with_message_location = self.location
                self.location = "bottle_with_message"
            return items_texts.get(item)
        elif place == 'up_toilet' and self.items_loc['up_bath'] == ['**toilet**']:
            self.items_loc['up_bath'] = ['toilet']
            item = self.additem()
            if item == "bottle with message":
                self.bottle_with_message_location = self.location
                self.location = "bottle_with_message"
            return items_texts.get(item)
        elif place == 'cabinet' and self.items_loc['front_hall'] == ['**cabinet**']:
            self.items_loc['front_hall'] = ['cabinet']
            item = self.additem()
            if item == "bottle with message":
                self.bottle_with_message_location = self.location
                self.location = "bottle_with_message"
            return items_texts.get(item)
        elif place == 'bed' and self.items_loc['bedroom'][0] == '**bed**':
            self.items_loc['bedroom'][0] = 'bed'
            item = self.additem()
            if item == "bottle with message":
                self.bottle_with_message_location = self.location
                self.location = "bottle_with_message"
            return items_texts.get(item)
        else:
            return "Nothing useful there."

    # main function
    def com(self, command):
        command = command.lower()
        command_split = command.split()

        if command == "inventory":
            return self.inv()

        elif len(command_split) == 0:
            return error_message

        # go (move)
        elif command_split[0] == "go":
            if len(command_split) > 1:
                try:
                    # gets new location based on previous location and direction
                    self.location = movement[self.location][command_split[1]]
                    # gets text for current location
                    text = self.loc_texts[self.location]
                    self.loc_texts[self.location] = location_texts[self.location]
                    if '{}' in text:
                        return text.format(*self.items_loc[self.location])
                    return text
                except KeyError:
                    if command_split[1] == 'right' and (self.location == 'basement' or self.location == 'basement_stairs'):
                        if 'Easter egg!' not in self.inventory:
                            if "pickaxe" in self.inventory:
                                self.inventory.append("Easter egg!")
                                return "The wall isn't looking really stable. I wonder if there is something behind it. I guess I will just use the pickaxe to get the wall down.. Oh, this is where the light was coming from! A shiny golden Easter egg!"
                            else:
                                return "The wall isn't looking really stable. I wonder if there is something behind it. Wish i had some tool or something to take it down."
                        else:
                            return "Nothing there."

                    if self.location == 'start' and (command_split[1] == 'right' or command_split[1] == 'left' or command_split[1] == 'back'):
                        return "It's too late to escape"

                    elif self.location == 'front_hall' and command_split[1] == 'back':
                        return "No going back now."

                    elif command_split[1] == 'down' and (self.location == 'front_hall' or self.location == 'stairs'): # basement texts
                        if "torch" in self.inventory and "lighter" in self.inventory:
                            self.location = "basement"
                            text = self.loc_texts[self.location]
                            self.loc_texts[self.location] = location_texts[self.location]
                            return text
                        elif "torch" in self.inventory:
                            self.location = "basement_stairs"
                            return location_texts['only_torch_basement']
                        elif "lighter" in self.inventory:
                            self.location = "basement_stairs"
                            return location_texts['only_lighter_basement']
                        else:
                            self.location = "basement_stairs"
                            return location_texts['basement_stairs']

                    elif self.location == 'basement':
                        if command_split[1] == "forward":
                            if "Copper key" in self.inventory and "Jade key" in self.inventory and "Crystal key" in self.inventory:
                                self.location = "end"
                                return location_texts['end']
                            elif 'Copper key' in self.inventory or "Jade key" in self.inventory or "Crystal key" in self.inventory:
                                keys = []
                                if 'Copper key' in self.inventory:
                                    keys.append('Copper')
                                if 'Jade key' in self.inventory:
                                    keys.append('Jade')
                                if 'Crystal key' in self.inventory:
                                    keys.append('Crystal')
                                if len(keys) == 1:
                                    text = 'The door is locked. The ' + keys[0] + ' key fits into the lock, but looks like I need the remaining two keys too.'
                                    if self.basement_door_imp:
                                        self.basement_door_imp = False
                                        return 'Damn it! ' + text
                                    return text
                                text = 'The door is locked. The ' + keys[0] + ' and ' + keys[1] + ' keys fit into the locks, but seems like I need the last one too.'
                                if self.basement_door_imp:
                                    self.basement_door_imp = False
                                    return 'Damn it! ' + text
                                return text
                            else:
                                text = "The door is locked. Looks like I'm not getting through without the keys.."
                                if self.basement_door_imp:
                                    self.basement_door_imp = False
                                    return 'Damn it! ' + text
                                return text
                        elif command_split[1] == 'up':
                            self.location = 'front_hall'
                            return location_texts['front_hall'].format(*self.items_loc['front_hall'])

                    elif self.location == 'basement_stairs' and command_split[1] == 'up':
                        self.location = 'front_hall'
                        return location_texts['front_hall'].format(*self.items_loc['front_hall'])

                    elif command_split[1] in ['forward','right','back','left']:
                        return 'Wanna bump into a wall?'

                    return "Where do you wanna go? (Type <help> for available commands)"
            else:
                return 'Where do you wanna go? (Type <help> for available commands)'

        # search place
        elif command_split[0] == "search":
            if len(command_split) > 1:
                place = command_split[1]
                if place in search[self.location]:
                    if place == 'toilet':
                        if self.location == 'down_bath':
                            return self.search('down_toilet')
                        return self.search('up_toilet')
                    return self.search(place)
                else:
                    return "Nothing useful there."
            else:
                return 'Where do you wanna search?'

        # help
        elif command_split[0] == "help":
            try:
                hlp = ""
                for mov in movement[self.location].keys():
                    hlp = hlp + '<go ' + mov + '>\n'
                if self.location == 'front_hall' or self.location == 'stairs':
                    hlp = hlp + '<go down>\n'
                try:
                    for pl in self.items_loc[self.location]:
                        if pl.startswith('*'):
                            hlp = hlp + '<search ' + pl.split('*')[2].lower() + '>\n'
                finally:
                    hlp = hlp + '<inventory>'
                    return hlp
            except KeyError:
                if self.location == 'bottle_with_message':
                    return "Wanna break the bottle or not? (use <yes> or <no>)"
                elif self.location == 'vault':
                    return "<leave>\n<(passcode)>\n<inventory>"
                elif self.location == 'basement_stairs':
                    return "<go up>\n<inventory>"
                elif self.location == 'basement':
                    return "<go forward>\n<go up>\n<inventory>"
                elif self.location == 'shelf':
                    return "<leave>\n<(order of books[just numbers like <12345>])>\n<inventory>"
                elif self.location == 'tutorial':
                    return "<start> to start the game!"
                elif self.location == 'end':
                    return "<reset> to restart the game"


        # bottle with message
        elif self.location == 'bottle_with_message':
            if command_split[0] == "yes":
                self.inventory.append("note:8055")
                self.inventory.remove("bottle with message")
                self.location = self.bottle_with_message_location
                return "It's broken! Nice there actually is something written there! Oh it's just numbers: 8055. I wonder if it's some passcode or something."
            elif command_split[0] == "no":
                self.inventory.append("note:8055")
                self.inventory.remove("bottle with message")
                self.location = self.bottle_with_message_location
                return "NO! Your clumsy hands! You dropped it! At least there is something written on the paper. Oh it's just numbers: 8055. I wonder if it's some passcode or something."
            else:
                return "Wanna break the bottle or not? (use <yes> or <no>)"

        elif self.location == 'vault':
            if command.strip() == "8055" or command.strip() == "8 0 5 5" or command.strip() == "8-0-5-5":
                self.inventory.append("Crystal key")
                self.items_loc['working_place'][1] = 'painting'
                self.location = "working_place"
                if self.loc_texts['basement'] == location_texts['basement']:
                    return "Yes! It opened! Oh a **CRYSTAL KEY!** This must be somehow connected to the door in the basement!"
                return "Yes! It opened! Oh a **CRYSTAL KEY!** This must be somehow connected to the treasure!"
            elif command_split[0] == "exit" or command_split[0] == "leave":
                self.location = "working_place"
                return location_texts['working_place'].format(*self.items_loc['working_place'])
            else:
                return "Nope that's not the right passcode."

        elif self.location == 'shelf':
            if command.strip() == "5 4 3 1 2" or command.strip() == "54312" or command.strip() == "5-4-3-1-2" or command.strip() == "5,4,3,1,2":
                self.inventory.append("Jade key")
                self.location = "living_room"
                self.items_loc['living_room'][1] = 'shelf'
                if self.loc_texts['basement'] == location_texts['basement']:
                    return "Yes this is the correct order! A small box came out. Ooh there's a **JADE KEY** in it! Bet it's one of the keys for the basement door!"
                return "Yes this is the correct order! A small box came out. Ooh there's a **JADE KEY** in it! Pretty sure I'm one step closer to the treasure!"
            elif command_split[0] == "exit" or command_split[0] == "leave":
                self.location = "living_room"
                return location_texts['living_room'].format(*self.items_loc['living_room'])
            else:
                return "Nope that's not the right order."

        elif self.location == 'tutorial':
            if command == 'start':
                self.location = 'start'
                return location_texts['start']
            else:
                return '<start> to start the game!'

        elif self.location == 'end':
            if command in ['reset','restart']:
                g = Game()
                self.location = 'start'
                self.inventory = []
                self.items = g.items
                self.bottle_with_message_location = g.bottle_with_message_location
                self.vault_imp = g.vault_imp
                self.basement_door_imp = g.basement_door_imp
                self.items_loc = g.items_loc
                self.loc_texts = g.loc_texts
                del g
                return location_texts['start']
            else:
                return '<reset> to restart the game!'


        elif self.location == 'stairs':
            if command == 'down':  # basement texts
                if "torch" in self.inventory and "lighter" in self.inventory:
                    self.location = "basement"
                    text = self.loc_texts[self.location]
                    self.loc_texts[self.location] = location_texts[self.location]
                    return text
                elif "torch" in self.inventory:
                    self.location = "basement_stairs"
                    return location_texts['only_torch_basement']
                elif "lighter" in self.inventory:
                    self.location = "basement_stairs"
                    return location_texts['only_lighter_basement']
                else:
                    self.location = "basement_stairs"
                    return location_texts['basement_stairs']
            elif command == 'up':
                self.location = 'up_hallway'
                self.loc_texts[self.location] = location_texts[self.location]
                return self.loc_texts[self.location]
            else:
                return error_message

        else:
            return error_message


if __name__ == "__main__":
    g = Game()
    g.location = 'start'
    print(g.loc_texts['start'])

    while True:
        print(g.com(input()))
