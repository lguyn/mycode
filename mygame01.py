#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
The Haunted Mansion
You have been asked to calm the spirits of this haunted mansion.
Upon entering the mansion, the doors shut behind you and the power goes out.
Find a way to escape before it is too late.

========
Commands:
  go [direction]
  get [item]
  read [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
  if 'description' in rooms[currentRoom]:
    print(rooms[currentRoom]['description'])

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hallway' : {
                  'south' : 'Study',
                  'east'  : 'Kitchen',
                  'upstairs' : 'Upstairs',
                  'description' : 'A long corridor at the corner of the house. To the east is the kitchen, to the south is the study, and there is also a stairway leading upstairs.',
                },
            'Kitchen' : {
                  'west' : 'Hallway',
                  'south' : 'Entrance',
                  'secret passage' : 'Secret Passage', 
                  'description' : 'A large, but seemingly empty kitchen. The hallway is to the west and the entrance is south.',
                },
            'Dining Room' : {
                  'west' : 'Entrance',
                  'item' : 'knife',
                  'description' : 'Cabinets full of China and a large dining table fill the room. There is a knife on the table.',
               },
            'Upstairs' : {
                  'downstairs' : 'Hallway',
                  'north' : 'Dave\'s Room',
                  'description' : 'A narrow hallway with a single door at the end.',
               },
            'Dave\'s Room' : {
                  'south' : 'Upstairs',
                  'item' : 'diary',
                  'description' : 'A dark room with nothing but a bed and a nightstand. On the nightstand lies a diary.',
               },   
            'Entrance' : {
                  'north' : 'Kitchen' ,
                  'east' : 'Dining Room',
                  'west' : 'Study',
                  'description' : 'The entry area of the house. There is a study to the west, a dining room to the east, and the kitchen is north.', 
               },
            'Study' : {
                  'east' : 'Entrance',
                  'north' : 'Hall',
                  'item' : 'key',
                  'description' : 'A small room with a table. On the table is a key and a lamp. East from the study is the entrance and the hall is to the north.',
         }
    }

#start the player in the Entrance
currentRoom = 'Entrance'

showInstructions()

#loop forever
while True:
  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  if move[0] == "read" :
      print('Gosh my parents never let me have junk food. Good thing I made a SECRET PASSAGE under the sink in the kitchen that leads to the outdoors. Now I can go get whatever food whenever I want. I really love almond joy!')

 ## Define how a player can win
  if currentRoom == 'Secret Passage':
    print("You escaped... you win!")
    break

