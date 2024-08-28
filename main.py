# Lost 1.5 
# For Scream Secrets Game Jam
# 22AUG2024

import time
import sys
import keyboard
import pygame 


# sound effects

pygame.mixer.init()

# Load your sound effects

outside_sound = pygame.mixer.Sound("Sounds/clearwavsound__night-time-crickets-call.wav")
battle_sound = pygame.mixer.Sound("Sounds/tomattka__girl-screaming_05.wav")
ladder_sound = pygame.mixer.Sound("Sounds/pointnemoprod__steps-on-squeaky-wooden-attic-ladder2.wav")
walking_sound = pygame.mixer.Sound("Sounds/dibko__walking-on-leaves.wav")
doorslam_sound = pygame.mixer.Sound("Sounds/adriann__door-slam-no-reverb.wav")

# credits 
def lost_credits():
    print()
    print('''Lost 2024 (C) 
Designed by: Red Door Creative, 
Story by: Red Door Creative,
Sound effects by: mastersoundboy2005, Poinrnemoprod, Adriann, Tomattka and dibko
Full relase fall 2026''')

# moral state of player
class MoralState:
    STATES = ["Hysterical", "Frantic", "Hopeless", "Sad", "Confused", "Determined"]

    def __init__(self):
        self.index = 4  # Start at "Confused"

    def increase_moral(self):
        if self.index < len(self.STATES) - 1:
            self.index += 1
            print()
            print(f"Mood increased. You are now {self.get_state()}.")
        self.check_hysterical()

    def decrease_moral(self):
        if self.index > 0:
            self.index -= 1
            print()
            print(f"Mood decreased. You are now {self.get_state()}.")
        self.check_hysterical()

    def get_state(self):
        return self.STATES[self.index]

    def check_hysterical(self):
        if self.STATES[self.index] == "Hysterical":
            slow_print("As your fear overcomes you, you fall into a fit of panic that you can't shake.")
            slow_print("The shadows consume you as you lie there, paralyzed by fear.")
            game_over()

moral_state = MoralState()


# slow print for dialogue
def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the text is printed



# Battle System
def battle_system(timer='5'):
    print()
    battle_sound.play()
    print("A specter appears! You have", timer, "seconds to press ENTER and flash your light!")
    
    start_time = time.time()
    success = False
  
    # Wait for the player to press 'enter' within the time limit
    while time.time() - start_time < timer:
        if keyboard.is_pressed('enter'):
            success = True
            
            moral_state.increase_moral()
            
            break

    # Evaluate the outcome after the loop finishes
    if success:
        print()
        print("You have vanquished the specter!")
        
        moral_state.increase_moral()
        
        return True
    
    else:
        print()
        print("You failed to react in time! The specter overwhelms you...")
        game_over()
        return False  # Player failed
    
    

# main menu   

def main_menu():
    print('##########################################################')
    print('')
    print()
    print("                      Lost                                ")
    print()
    print()                                    
    print('##########################################################')
    print('')
    menu=input("Press 1 to start game. Press 2 to exit. >").strip()

    if menu == '1':
        start_game()

    elif menu == '2':
        sys.exit()

    else:
        print("That's not an option. Try again.")
        main_menu()

def intro():
    print()
    outside_sound.play()
    time.sleep(10)
    slow_print("Where...", 0.50)
    slow_print("am...", 0.5)
    slow_print("I?", 0.5)
    slow_print("You wake up alone in a dense, dark forest. The trees are so tall it's as if they bolt up to the sky..." , 0.05)
    print("")
    slow_print("A chilling wind rustles through the leaves, carrying with it the eerie sounds of distant, unknown creatures.", 0.05)
    slow_print("Your breath forms misty clouds in the cold air, and the only light comes from the dim, fading glow of a distant moon.", 0.05)
    print("")
    slow_print("As you are trying to catch your bearings, you look down by your feet and see a flashlight on the ground.", 0.05)
    slow_print("You slap it on with your hand and it turns on. You look around and see what appears to be a path to the left and right." , 0.05)
    slow_print("Alternatively, you can eleect to camp out tonight as you don't know where you are or where the each path leads." , 0.05)
    slow_print("Without sheltter you run the risk of catching frostbite.", 0.05)
    print("")
    slow_print("What do you want to do?")
    print()
    print (F" Your Mood is {moral_state.get_state()}")
    print("")
    
    camp_out_or_travel()

def game_over():
    print()
    print("The darkness consumes you. You are lost...")
    print()
    print("GAME OVER")
    print()
    start_over=input("Press enter to start over or Q to quit.>").strip()

    if start_over == 'Q':
        sys.exit()

    elif start_over == '':
        start_game()
    
def start_game():
    intro()

def camp_out_or_travel():
 
 choice_1=input(" Press 1 to go left. Press 2 to go right. Press 3 to camp out.>").strip()

 if choice_1 == '1':
    
    print()
    choice_1_left()

 elif choice_1 == '2':
    
    print()
    choice_1_right()

 elif choice_1 == '3':
    
    camp_out()

 else:
    print("That's not an option. Try again.")
    camp_out_or_travel()

#defining the path for capmping out 
def camp_out():
    print()
    
    print('''You decide to make camp, setting your backpack down and wrapping your arms around yourself, 
trying to conserve warmth in the biting cold. The flashlight is your only source of comfort, 
its narrow beam casting a feeble circle of light that barely holds back the encroaching darkness. 
The sounds of the forest are unnerving—rustling leaves, distant cries of creatures you can't identify,
and the ever-present murmur of the wind through the trees. It feels as though the night is alive, breathing, and watching.''')
    print()
    time.sleep(20)
    print('''As you sit in the dim glow, the flashlight flickers occasionally, casting shadows that dance at the edges of your vision, 
forming shapes that seem to move with purpose. The wind carries faint whispers—soft, indistinct, and unsettling. You strain to hear, 
but all that meets your ears is the hum of the flashlight and the rapid thudding of your heart. The cold creeps in relentlessly, 
numbing your fingers and toes. You huddle closer to yourself, trying to find warmth, but the chill seems to seep into your very bones.''')
    print()
    time.sleep(20)
    print('''Hours pass, and just as your exhaustion begins to overpower your fear, the flashlight suddenly dims, 
and the forest around you seems to grow darker, more oppressive. In the periphery of your vision, you catch a glimpse of movement—a shadowy figure, 
indistinct and ethereal, just beyond the light’s reach. Panic surges within you, but before you can react, the whispering grows louder, more insistent. 
The words are still unclear, but their intent is unmistakable: you're not alone.''')
    print()
    time.sleep(20)
    camp_out_choice()

# Defining the path for going left
def choice_1_left():
    print("")
    print("you went left...")

    time.sleep(0.5)
    print()
    print('''You choose the left path, and as you step forward, the fog thickens, 
swirling around you like a living entity. The deeper you go, the more the world seems to close in, 
the trees leaning closer as if to observe your every move. 
The silence is deafening, broken only by the occasional snap of a twig underfoot. 
There's an oppressive weight in the air, as though the forest itself is holding its breath.''')
    game_over()

# Defining the path for going right
def choice_1_right():
    print('''You turn right, and the path twists and turns, leading you deeper into the forest. 
The trees seem less dense here, but the shadows they cast are long and dark. 
The further you walk, the more you notice that the ground beneath your feet is soft, almost spongy,
as if the earth is alive and breathing beneath you.''')
    print()
    time.sleep(15)
    print('''In the distance, a soft glow catches your attention. As you approach, 
the light intensifies, revealing a small, dilapidated cabin half-hidden by the trees.
The windows are broken, and the door hangs loosely on its hinges. 
Yet, the glow seems to emanate from within.''')
    walking_sound.stop()
    cabin_choice()

def cabin_choice(): # Defining the path for entering the cabin
    print("")
    print("Do you enter the cabin or go back to the path?")
    print("")
    choice_2=input("Press 1 to enter. Press 2 to go back.>").strip()

    if choice_2 == '1':
       outside_sound.stop()
       enter_cabin()

    elif choice_2 == '2':
        keep_walking()

    else:
        print("That's not an option. Try again.")
        cabin_choice()

def camp_out_choice(): # Defining the path camping out
    print()
    camp_choice = input("Press 1 to to flash the light. Press 2 to Stay Still.>").strip()
    if camp_choice == '1': # flash the light
        print()
        battle_system(timer=5)
        print()
        print('''Not being able to fall a sleep you to decided that maybe trying to rest in the middle of nowhere wasn't the best idea.
You grab your stuff and deceide to take the path on the right and hope for the best.''')
        print ()
        time.sleep(10)
        choice_1_right()
        print()
    elif camp_choice == '2': # stay still
        print()
        moral_state.decrease_moral()  # Decrease moral for camping out
        print()
        print('''You stay perfectly still, hardly daring to breathe as the shadow moves closer. 
The whispers grow louder, almost taunting in their intensity. But then, just as suddenly as it appeared, 
the shadow retreats, and the forest falls silent once more. The night drags on...''')
        print()
        time.sleep(10)
        moral_state.decrease_moral()  # Decrease moral for camping out
        print()
        print('''Not being able to sleep to decided that maybe trying to sleep in the middle of nowhere wasn't the best idea.
You grab your stuff and deceide to take the path on the right and hope for the best.' ''')
        print ()
        time.sleep(10)
        choice_1_right()
        
    
    else:
        print("That's not an option. Try again.")
def enter_cabin():
    
    print()
    print('''The door creaks loudly as you push it open, the sound reverberating 
through the empty forest. A pungent smell of damp wood and mildew immediately assaults your senses, 
the air inside thick with the weight of forgotten time. The cabin is small and claustrophobic, 
with a single, lantern in the center of the cabin, casting 
a dim, flickering light that only barely illuminates the room.''')
    time.sleep(20)
    print()
    doorslam_sound.play()
    print('''As you step inside, the door suddenly slams shut behind you with a force that sends a shiver down your spine. 
The sound echoes through the small space, and you instinctively reach out to the walls, 
feeling the rough, splintered wood beneath your fingers. 
The cabin feels oddly alive, as though it's been waiting for you all along.''')
    print()
    time.sleep(20)
    print('''The lantern's light flickers, casting dancing shadows that stretch and distort across the walls. 
For a moment, you see the shadow of a figure standing in the far corner, just beyond the reach of the light. 
But when you turn to look, the corner is empty, the darkness mocking your unease.''')
    print()
    time.sleep(20)
    print('''Your heart pounds as you slowly survey the room. The floorboards creak beneath your feet, 
and you can almost feel the eyes of the cabin watching you. There's a small table in the center of the room,
its surface covered in dust, and a tattered piece of parchment lies atop it. You pick it up, and though 
the writing is faded, you can just make out the words:''')
    time.sleep(10)
    print()
    slow_print('It was there all along… waiting for you...', 0.30)
    time.sleep(20)
    print()
    print('''As you read the final word, the lantern flickers again, then goes out completely, 
plunging the cabin into total darkness. You fumble for the flashlight, your hands trembling, but it refuses to turn on. 
Panic begins to set in as the shadows around you seem to grow thicker, more oppressive. 
The walls feel like they’re closing in, suffocating you.''')
    time.sleep(10)
    print()
    print('''Just when the darkness seems unbearable, you hear it—a low, guttural whisper, as though someone...''')
    print()
    print("or something... ")
    print("")
    print("is standing right behind you. The voice is ancient, worn, yet filled with an eerie familiarity:")
    print()
    time.sleep(5)
    slow_print('It was there all along… waiting for you...', 0.30)
    time.sleep(5)
    print()
    print('''A sudden chill runs down your spine. You spin around, 
trying to see through the pitch black, but there’s nothing—just the oppressive darkness pressing in from all sides.
And then, from the corner of your eye, you catch a glimpse of movement. Something is in here with you.''')
    print()
    time.sleep(20)
    print('''A specter emerges from the shadows, its form barely discernible but undeniably menacing. 
You feel its icy gaze on you, and you know you have only seconds to act before it strikes. 
With no other choice, you slam your hand down on the flashlight, praying it will turn on.''')
    print("")

    time.sleep(10)

    survived = battle_system(timer=5)

    if not survived:
     print()
     moral_state.decrease_moral()
    
    print ()
    print('''The flashlight flickers to life, its beam slicing through the darkness like a blade. 
The specter recoils, letting out a bone-chilling shriek as the light engulfs it. 
For a moment, the cabin is still, the oppressive darkness retreating to the corners of the room.''')
    time.sleep(15)
    print()
    slow_print("W T F is going on....", 0.30)
    print()
    print('''you said to yourself as you catch your breath, the relief washing over you, but it’s fleeting. 
''')
    time.sleep(10)
    print()
    print('''You reach for the door, desperate to escape, but the handle won’t budge. 
The cabin, once so unassuming from the outside, now feels like a living, breathing entity—a trap set just for you. 
In your frantic search for a way out, you notice a small hatch in the floor, hidden beneath a rotting rug''')
    print()
    time.sleep(20)
    print('''With no other options, you pry open the small hatch, revealing a narrow, wooden ladder leading down into the darkness. 
a gust of frigid air rushes up from below, carrying with it the unmistakable stench of mold and decay.
The air wafting up from below is even colder and more foreboding than the cabin itself, but staying here isn’t an option.''')
    ladder_sound.play()
    print()
    time.sleep(20)
    print('''As you descend, the darkness swallows you whole, and the whispers return, growing louder with each step down. 
They’re not coming from behind you, but from below—where the ladder leads. 
Each rung of the ladder groans under your weight, and you can't shake the feeling,
that you're descending into something far worse than the cabin above.''')
    Basement()

def Basement():
    
    print()
    print('''You hesitate for a moment, peering down into the yawning void beneath the hatch. 
The wooden ladder creaks ominously, its rungs worn and splintered, as if they haven’t been touched in decades. 
But the thought of staying in the cabin, with its oppressive walls and unseen terrors, is too much to bear. 
You take a deep breath, attach the latern to your backpack, gripping the flashlight tightly in one hand, and begin your descent.''')
    time.sleep(5)
    ladder_sound.play()
    print()
    time.sleep(20)
    print('''With each step down the ladder, the light above you dims, swallowed by the encroaching darkness. 
The cold seeps into your bones, a biting chill that seems to originate from the very earth below. The whispers, 
soft at first, grow louder with each rung you descend. They’re not the gentle murmurings of a breeze, 
but something far more sinister—voices that seem to speak directly to your mind, slipping into your thoughts like poison.''')
    print()
    time.sleep(20)
    print('''The ladder creaks under your weight, each groan of the wood reverberating through the pitch-black space around you. 
You try to focus on the steps, but the whispers claw at your consciousness, tugging at your sanity. 
They’re speaking in a language you don’t understand, yet their meaning is clear: you’re not supposed to be here.''')
    print()
    time.sleep(20)
    print('''The ladder creaks more and more, its rungs worn and splintered, as if they haven’t been touched in decades.''')
    print()
    time.sleep(20)
    print('''At last, your feet touch the cold, damp earth of the basement floor. 
The air here is even thicker, heavy with the scent of rot and something else—something old and malignant. 
You can barely see, the flashlight’s beam cutting through the darkness but doing little to illuminate the vast, 
oppressive space around you. The whispers have stopped, replaced by a suffocating silence that presses down on you from all sides.''')
    print()
    time.sleep(20)
    print('''As your eyes adjust, you begin to make out shapes in the darkness. 
Shelves lined with dusty, forgotten trinkets, broken furniture scattered across the floor,
and the walls, covered in a thick layer of grime and mold. But it’s the far corner of the basement that draws your attention, 
where something glints faintly in the weak light..''')
    print()
    time.sleep(20)
    print('''You approach cautiously, each step slow and deliberate, the floor beneath you slick with moisture. 
As you get closer, you realize it’s a mirror, its surface covered in grime and cobwebs.
But when you wipe it clean with your sleeve, you’re greeted with a reflection that makes your blood run cold...''')
    time.sleep(20)
    mirror_conversation()

# Defining the mirror conversation
def mirror_conversation():
    print()
    print('''The figure staring back at you is… you, but twisted in a way that defies explanation. 
The eyes are darker, emptier, and the face wears a sinister smirk that you’ve never seen before.''')
    print()
    time.sleep(10)
    print('''As you try to make sense of what you're seeing, 
another figure slowly materializes in the reflection—a shadowy presence standing just behind you, 
its eyes glowing with an unnatural light. It’s as if the darkness itself has taken shape,
watching you with a malevolent intent.''')
    print()
    time.sleep(20)
    slow_print('''You: “Who… who are you?''', 0.1) 
    print()
    slow_print('''Shadowy Figure (In a low, rasping voice): 
"Who am I? Who are you? The one who walks in circles, chasing shadows, chasing memories.''', 0.1)
    print()
    slow_print('''You (Heart pounding): “What do you want from me?”''', 0.1)
    print()
    slow_print('''Shadowy Figure: "Want? I want nothing. I merely exist, as do you. We are reflections, 
you and I, bound to this place by fate or folly. Tell me, what did you hope to find here?"

You (Desperately): “I don’t know… I just want to leave.”

Shadowy Figure: "Leave? There is no leaving, only returning. The forest, the cabin… they are not what they seem. 
They are mirrors, showing you the truth you refuse to see."

You: “What truth? What are you talking about?”

Shadowy Figure (Leaning closer, its voice almost a whisper): "It was there all along… waiting for you. 
It knows your name, your fears, your regrets. It knows why you came here, even if you do not."

You (Backing away): “I don’t understand…”

Shadowy Figure: "You will. The darkness reveals what the light conceals. But be warned, what you find may not be what you seek."

You (With a growing sense of dread): “What are you saying? What is this place?”

Shadowy Figure: "This place is you. The forest, the cabin, the shadows—they are all pieces of the same puzzle. 
A riddle wrapped in fear, shrouded in darkness. You cannot escape what you are."''', 0.1)
    print()
    slow_print('''You (Whispering to yourself): “This isn’t real… It can’t be real.”

Shadowy Figure: "Reality is a mirror, and mirrors never lie. The question is, 
do you have the courage to face what you see?"''', 0.1)
    print()
    time.sleep(10)
    print('''TThe shadowy figure in the mirror suddenly lunges forward,splitting into three breaking free from the glass.  
The room plunges into darkness, the only light coming from your flickering flashlight. 
You grip it tightly, knowing it’s your only defense.''')
    print()
    time.sleep(5)
    
    survived = battle_system(timer=5)
    

    if not survived:
     print()
     print('''You fumble with the flashlight, your hands shaking with fear. 
The light flickers, but before you can aim it at the specter, it’s too late. 
The figure overwhelms you, and everything goes black.''')
    game_over()

    print('''You manage to raise the flashlight just in time. 
The beam of light cuts through the darkness, striking the specter square in its hollow eyes. 
It recoils with a screech, dissolving into wisps of shadow that dissipate into the air.''')
    
    print()
    print('''The room is silent again, the oppressive darkness retreating. 
Your reflection in the mirror is normal once more, 
but you can’t shake the feeling that something has changed—inside you, 
and in the very fabric of this place...''')
    ending()

# Defing the keep waling choice
def keep_walking():
    print("")
    print('''Determined not to stop, you tighten your grip on the flashlight and continue moving forward. 
The forest seems to stretch on endlessly, each step echoing the ones before it. The path is barely visible,
obscured by creeping fog and overgrown roots that threaten to trip you with every step. The trees loom overhead like silent sentinels,
their branches twisting and curling as if trying to reach down and snatch you away.''')
    time.sleep(5)
    
    print()
    time.sleep(20)
    print('''"The deeper you go, the more the forest seems to change. The air grows colder,
and the darkness feels thicker, more oppressive. 
Your footsteps become the only sound, a rhythmic crunching of leaves and twigs that serves as a fragile tether to reality.
But then, without warning, the sounds of the forest—the rustling leaves, the distant cries, even the wind—cease entirely.
An unnatural silence descends, suffocating in its intensity.''')
    print()
    time.sleep(20)
    print('''As you push forward, you begin to feel a presence—a weight in the air, a feeling that you're not alone. 
The flashlight flickers, and just at the edge of its beam, you see movement. It's subtle at first, 
a shadow darting between the trees, but then it becomes unmistakable. Something is following you.''' )
    print()
    time.sleep(20)
    print('''As you push forward, you begin to feel a presence—a weight in the air, 
a feeling that you're not alone. The flashlight flickers, and just at the edge of its beam, you see movement. 
It's subtle at first, a shadow darting between the trees, but then it becomes unmistakable. Something is following you.''')
    walking_sound.stop()
    time.sleep(3)
    print()
    survived = battle_system(timer=5)

    if not survived:
     print()
     moral_state.decrease_moral()
    print()
    print('''You stop and turn around, shining your flashlight into the darkness. 
The beam catches a figure—a twisted, shadowy form that recoils from the light. 
It hisses and retreats into the shadows, vanishing as quickly as it appeared. 
The forest seems to release a breath it had been holding, and the sounds of the night slowly return. 
You feel a small surge of confidence, knowing that the light is your protection.''')
    print()
    time.sleep(20)
    print('''Despite the strange encounter, you manage to press on, the forest growing more twisted and unnatural with each passing step. 
not seeing any way forward you decided to circle back to the cabin you seen before. maybe it will have some answers..
or at least some shelter to get you through the night. ''')
    enter_cabin()

def ending():
    print()
    print('''Thank You for Playing!"

"Thank you for stepping into the darkness and experiencing Lost. Your courage and quick thinking have carried you through the shadows, 
but this is only the beginning. The forest holds many more secrets, 
and the truth is still waiting to be uncovered.

We hope you've enjoyed this Scream Secrets entry. 
Stay tuned for the completed game, where your choices will delve even deeper into the unknown. 
The shadows await your return… if you dare.''')
    lost_credits()





main_menu()
