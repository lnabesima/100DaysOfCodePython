print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

print(
    "As the sun rises, casting a warm golden glow over the vast ocean, you find yourself on the shores of Adventure Island. This remote and enigmatic landmass is shrouded in legends of long-lost treasures and untold mysteries. Lush jungles, towering cliffs, and sparkling waterfalls decorate the landscape, all whispering tales of the forgotten past.\n")

print(
    "In the distance, you notice a winding road, seemingly untouched by time, leading deeper into the heart of the island. This road, worn smooth by the footsteps of countless explorers before you, beckons you to embark on your own thrilling journey. Every step forward fills the air with anticipation, as the road promises both challenges and rewards.\n")

print(
    "As you follow the winding road, you come across a critical moment - a bifurcation in the path. The forest around you is dense, and the air carries a sense of foreboding mystery. Two diverging trails lie before you, each holding its own promise and peril.\n")
left_or_right = input("Which path do you choose? Type 'left' or 'right'.\n").lower()
if left_or_right == "left":
    print(
        'The path meanders through a dense thicket, hinting at hidden secrets and potential discoveries. The foliage casts playful shadows on the ground, and you can hear the distant sounds of creatures stirring in the underbrush. This route beckons with curiosity, inviting you to explore further into the unknown.\n')
else:
    print(
        "With a heart full of uncertainty, you choose to take the right path, tempted by the sense of adventure and the possibility of an unconventional route to the treasure.\n")
    print(
        "Suddenly, a deafening crack echoes through the air, and before you can react, the ground beneath your feet collapses. You find yourself plummeting into a dark, bottomless pitfall. The world around you blurs as you descend, and your hopes of finding the treasure chest come to an end.")
    print("Game Over")
    exit()

print(
    "As you bravely venture down the path to the left, the thick forest finally gives way, revealing a glistening river that cuts through the island. The river's waters flow with a gentle yet determined current, reflecting the sunlight like a shimmering mirror. The other side of the river holds the promise of unexplored territories and potential clues to the treasure chest's whereabouts.\n")

print(
    "As you approach the water's edge, a sense of wonder and excitement fills your heart. However, your path seems blocked, and you realize that a crucial choice awaits you.\n")

swim_or_wait = input(
    "Type 'wait' to wait for a boat. Type 'swim' to swim across the river.\n").lower()
if swim_or_wait == "wait":

    print(
        'With wisdom and foresight, you decide to wait for a boat, acknowledging that patience can be a virtue. As the moments pass, a small wooden rowboat arrives at the dock, steered by a fellow explorer who welcomes you aboard. The boat\'s planks creak softly as you step in, and the gentle lap of water against the hull soothes your senses.\n')

    print(
        "As your boat companion expertly navigates the river, you feel a sense of camaraderie with a fellow adventurer. They share tales of their own journey, providing you with valuable insights into the island's landscape and its secrets. Their knowledge proves to be invaluable, helping you avoid potential pitfalls and directing you towards promising paths.\n")

    print(
        "As you approach the other side, your boat companion bids you farewell, and you step ashore with gratitude for their assistance. The river's crossing was not only successful but also enlightening, providing you with a deeper understanding of the island's mysteries.\n")

    print(
        "Your adventure continues, and the treasure chest awaits further exploration. You are now one step closer to uncovering the legendary prize. With renewed determination and the memory of the boat journey in your heart, you venture forth into the unknown, ready to face the challenges that lie ahead.\n")
else:
    print(
        "Emboldened by your determination to expedite your quest, you decide to take the daring leap and plunge into the river. With each stroke, you push through the water with all your strength, making steady progress towards the other side. The river's cool embrace invigorates you, and for a moment, you feel an invincible surge of energy.\n")

    print(
        "Yet, just as you begin to feel the thrill of nearing your goal, an ominous shadow emerges beneath the water's surface. With a sudden jolt of panic, you realize that a giant trout, lurking in the depths, has set its sights on you. The legendary creature, rumored to be a guardian of the river, reveals itself in all its awe-inspiring and fearsome glory.\n")

    print(
        "Desperately, you try to outmaneuver the colossal fish, but its immense power overtakes you. With a swift, massive lunge, the trout devours you whole, taking you into the dark depths of the river.\n")

    print(
        "Alas, your tale ends here, swallowed by the very waters that you sought to conquer. The treasure chest remains untouched, and your dream of discovering it will remain unfulfilled.\n")
    print("Game Over")
    exit()

print(
    "As you venture deeper into the heart of the jungle, your steps lead you to a mysterious cave. The entrance is adorned with ancient symbols, hinting at secrets buried within its depths. Cautiously, you step inside, and the darkness envelops you.\n")

print(
    "Torch in hand, you make your way through the dimly lit passages until you stumble upon a chamber bathed in an eerie glow. In the center of the room stand three imposing doors, each painted with a distinct color: one door is red, another is blue, and the last one is yellow.\n")

print(
    "The air is charged with anticipation as you recognize the significance of your discovery. These doors seem to hold the key to the next stage of your quest, but each door may lead to vastly different outcomes.\n")

red_blue_or_yellow_door = input(
    "Which color do you choose? Type 'red', 'blue', or 'yellow'.\n").lower()

if red_blue_or_yellow_door == "red":
    print(
        "You venture forth into the room beyond, fully aware of the risks that lie ahead. As you step inside, the door slams shut behind you, sealing your fate within the chamber.\n")

    print(
        "Without warning, the room comes alive with a sudden burst of flames. The once tranquil space transforms into a fiery inferno, with walls of fire shooting up from the floor and scorching the ceiling. Panic sets in, and you realize that you've stumbled upon a deadly fire trap.\n")

    print(
        "The fire trap is relentless, and despite your best efforts, you find yourself engulfed in the unyielding blaze. The flames mercilessly lick at your body, and your skin burns with searing pain. Your cries for help are stifled by the inferno, and it becomes clear that survival in this treacherous trial is unlikely.\n")

    print(
        "As the flames finally take their toll, your world fades into darkness. The fire trap has claimed its price, and your journey on Adventure Island comes to a tragic end.\n")

    print("Game Over")
    exit()
elif red_blue_or_yellow_door == "blue":
    print(
        "With a thirst for knowledge and answers, you opt to enter the blue door, seeking the enlightenment promised by this mysterious path. As you step inside, the door closes behind you with a soft click, and you find yourself in a room enveloped by a soothing blue glow.\n")

    print(
        "However, your tranquility is short-lived. As your eyes adjust to the dim light, movement catches your attention. From the shadows emerge a pack of fierce and fearsome beasts, their eyes glinting with predatory hunger.\n")

    print(
        "Realization dawns upon you - this room is not a place of enlightenment but a cunning puzzle. The blue door has led you into a den of ferocious predators, and they are closing in fast.\n")

    print(
        "Though you fight with all your might, the beasts are relentless. Their savage hunger overpowers your efforts, and you find yourself surrounded and overwhelmed by their sheer ferocity. The room echoes with the sounds of your struggle, but alas, it is futile.\n")

    print(
        "In a heart-wrenching turn of events, you become prey to the denizens of the blue door, your quest for treasure meeting a bitter end. \n")

    print("Game Over")
    exit()
else:
    print(
        "You find yourself in a room bathed in warm and inviting light. The ambiance feels comforting, and you sense a profound sense of camaraderie. Your instincts guide you to an altar at the center of the room, and upon it lies a magnificent treasure chest.\n")

    print(
        "Anticipation builds in your heart as you approach the chest. With trembling hands, you carefully open it, and to your surprise, the chest contains not gold or jewels, but a single scroll adorned with intricate writing.\n")

    print(
        "As you unfurl the scroll, the words etched on it resonate deeply within you: 'The real treasure are the friends we make along the way.'\n")

    print("You won the game! Congratulations!")
