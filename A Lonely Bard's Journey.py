#---------------------------#
#|   Marielli Vichique      |
#|   Text Adventure Game    |
#| A Lonely Bard's Journey  |
#---------------------------#



# Text adventure game where you the player are a bard lost in a 
# strange and fantastical land attempting to find your way back to normalcy.
# Various prompts are given to the player to choose from, leading to different scenarios
# and endings based on their choices.
# minimum 10 prompts


from ast import While
import random
import pygame
from time import sleep
import sys
import time

#--------------------------------------------------------------------------- Initialize Pygame-----------------------------------------------------------------------
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()


# ---------- Color codes for text ---------- 
COLORS = {
    "reset": "\033[0m",
    "narrator": "\033[38;5;211m",  # orange
    "player": "\033[38;5;81m",     # cyan/blue
    "npc": "\033[38;5;179m",       # warm yellow
    "system": "\033[38;5;250m",    # gray
    "important": "\033[38;5;196m", # red
}

# --------------------------------------------------------------------------- Define Text Speed function ---------------------------------------------------------------
def slowPrint(
    text,
    base_delay=0.05,
    jitter=0.01,
    pauses=None,
    color=None,
    end="\n"
):
    
    #-- Pauses added after punctuation for natural flow --
    if pauses is None:
        pauses = {
            ".": 0.7,
            ",": 0.7,
            ";": 0.35,
            ":": 0.35,
            "!": 0.0,
            "?": 0.7,
            "…": 0.9,
        }

    if color and color in COLORS:
        sys.stdout.write(COLORS[color])

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        # Extra pause on punctuation
        if char in pauses:
            time.sleep(pauses[char])

        # Slight variation so it doesn’t feel robotic
        delay = base_delay + random.uniform(0, jitter)
        time.sleep(delay)

    if color:
        sys.stdout.write(COLORS["reset"])

    sys.stdout.write(end)
    sys.stdout.flush()

#------------------------------------------------------------Define player status variables --------------------------------------------------------------
playerMarked = False
instrumentPlayed = False
playerSpared = False
reflectedInPond = False
encounteredCreature = False


# ---------------------------------------------------------------------- Define Continue Button --------------------------------------------------------------------
def continuePrompt(prompt="\n[Press Enter to continue]"):
    slowPrint(prompt, base_delay=0.0, jitter=0.0, color="system")
    input()

#---------------------------------------------------------------------Define Speed of Text Set by Player----------------------------------------------------------------
textSpeed = 0.05  # Default text speed
def setTextSpeed():
    global textSpeed
    systemSays("Before we begin || Choose your preferred text speed:")
    systemSays("1) Slow")
    systemSays("2) Medium")
    systemSays("3) Fast")
    choice = input("Enter the number corresponding to your choice: ")
    if choice == "1":
        textSpeed = 0.07
    elif choice == "2":
        textSpeed = 0.06
    elif choice == "3":
        textSpeed = 0.02
    else:
        systemSays("Invalid choice. Setting to default (Medium).")
        textSpeed = 0.04
    systemSays(f"Text speed set to {['Slow', 'Medium', 'Fast'][int(choice)-1] if choice in ['1','2','3'] else 'Medium'}.")

# ------------------------------------------------------------Define text Speed for different characters ------------------------------------------------------------
def narratorSays(text):
    slowPrint(text, base_delay=(textSpeed), jitter=0.01, color="narrator")

def playerSays(text):
    slowPrint(text, base_delay=(textSpeed), jitter=0.01, color="player")

def npcSays(text, name=None):
    if name:
        slowPrint(f"{name}: {text}", base_delay=(textSpeed), jitter=0.01, color="npc")
    else:
        slowPrint(text, base_delay=(textSpeed), jitter=0.01, color="npc")

def systemSays(text):
    slowPrint(text, base_delay=0.02, jitter=0.0, color="system")

def importantSays(text):
    slowPrint(text, base_delay=(textSpeed), jitter=0.01, color="important")


# ---------------------------------------------------------------------Define Song Book variables---------------------------------------------------------------------



def songBook(songs):
    systemSays("[Songs Learned ]")
    if not songs:
        systemSays("Your song book is empty.")
    else:
        systemSays("You flip through your song book:")
        for song in songs:
            systemSays(f"- {song}")
    continuePrompt()

# Display Name of songs and effects
def displaySongsAndEffects(songs, effects):
    systemSays("[YOUR SONGS AND STATUS EFFECTS]")
    if songs:
        systemSays("Songs:")
        for song in songs:
            systemSays(f"- {song}")
    else:
        systemSays("No songs learned yet.")
    
    if effects:
        systemSays("Status Effects:")
        for effect in effects:
            systemSays(f"- {effect}")
    else:
        systemSays("No status effects currently.")
    continuePrompt()

# ------------------------------------------------------------------Define selected instrument choice ----------------------------------------------------------------
def chooseInstrument():
    global selected_instrument
    instruments = ["Lute", "Harp", "Flute", "Drum"]
    systemSays("What is beside you?:")
    systemSays("1) A Lute")
    systemSays("2) A Harp")
    systemSays("3) A Flute")
    systemSays("4) A Drum")
    choice = input("Choose an instrument: ")
    if choice == "1":
        selected_instrument = "Lute"
    elif choice == "2":
        selected_instrument = "Harp"
    elif choice == "3":
        selected_instrument = "Flute"
    elif choice == "4":
        selected_instrument = "Drum"
    else:
        systemSays("Invalid choice. Please select a valid instrument.")
        chooseInstrument()

# --------------------------------------------------------------------Define player name choice -------------------------------------------------------------------
def playerName():
    playerSays("\nWhat is my name?... Do I even have one?")
    sleep(2)    
    playerName = input("Enter your name: ")

    narratorSays("\nYou think to yourself")
    sleep(1)
    playerSays(f"\n{playerName}... Yes, that sounds right! I think I'm {playerName}...")
    sleep(1)
    narratorSays("\nYou feel a momentary wave of relief as you clutch onto this small fragment of identity you created.\nThough you know it feels wrong.")
    sleep(1)
    continuePrompt()

#--------------------------------------------------------Define Playing Instrument Choice ----------------------------------------------------------------------
instrumentPlayed = False

def playInstrument():
    global instrumentPlayed
    systemSays(f"\nDo you wish to play your {selected_instrument} to try and soothe your mind?")
    systemSays("1) Yes")
    systemSays("2) No")
    choice = input("What is your choice: ")
    if choice == "1":
        narratorSays(f"You prepare to play your {selected_instrument} hoping to shake this unnerving feeling and find solace in its once familiar tune...")
        sleep(1)
        systemSays("Nothing happens")
        sleep(2)
        narratorSays("Your mind is drawing blanks on what to play")
        sleep(1)
        narratorSays("Melodies once familiar now lost within the fog that has blanketed your mind.")
        sleep(1)
        systemSays(f"You put your {selected_instrument} away")
        sleep(1)
        narratorSays("Maybe you'll remember later")
        sleep(2)
        narratorSays("Hopefully")
        sleep(2)
        continuePrompt()

        instrumentPlayed = True
    elif choice == "2":
        narratorSays(f"You decide against playing your {selected_instrument} for now, you do not wish to draw attention to yourself.")
        sleep(1)
        narratorSays("Maybe it's for the best, you can always try again later.")
        systemSays(f"You put your {selected_instrument} away")
        continuePrompt()


#------------------------------------------------------------------------ Define Game Over Scenarios -------------------------------------------------------------------

def indecisiveEnding():
    global playerMarked, instrumentPlayed, playerSpared, reflectedInPond

    gameoverEnding = ["1", "2", "3"]

    choice = random.choice(gameoverEnding)

    if choice == "1":
        narratorSays("\nUnable to decide, you remain still for a moment and soak in the sight of the strangely comforting yet frightening scenary of this land.")
        sleep(1)
        narratorSays("You decide to look up in an attempt to decipher the strange patterns in the every changing sky only to feel a dull ache begin to creep up your legs ")
        sleep(1)
        narratorSays("As you look down to assess the growing pain you realize with horror that your once human legs have transformed into something unrecognizable.")
        sleep(1)
        narratorSays("Panic sets in as you try to move but find yourself rooted to the ground, your lower half now a grotesque amalgamation of twisted roots and tendons.")
        sleep(1)
        narratorSays("You become one with the land you so desperately wanted answers from.")
        sleep(1)
        importantSays("GAME OVER")

    elif choice == "2":
        narratorSays("\nDecision paralysis takes hold as you stand frozen, unable to choose a path.")
        sleep(1)
        narratorSays("Though you feel like you have an eternity to decide...the land decides for you.")
        narratorSays("...")
        narratorSays("You blink and suddenly find yourself surrounded by an eerie silence.")
        sleep(1)
        narratorSays("You finally feel like you're ready to decide, but as you muster up the courage to move, you realize there was nothing but a vast emptiness around you.")
        sleep(1)
        narratorSays("The land had forgotten you and left you to your thoughts for 300 years")
        sleep(1)
        narratorSays("Before you can even process what has happened, the last of your consciousness fades away.")
        sleep(1)
        importantSays("GAME OVER")
        
    elif choice == "3":
        narratorSays("You have toiled in this strange land for too long that you can't seem to decide for yourself.")
        sleep(1)
        narratorSays("Feeling the weight of helplessness creep in, you succumb to the overwhelming despair.")
        sleep(1)
        narratorSays("As if waiting for an invitation, the land and its grotesque creatures close in around you.")
        sleep(1)
        narratorSays("You willingly give yourself to the land and its horrors, becoming one with the darkness.")
        sleep(1)
        importantSays("GAME OVER")
            
    gameover = True   
    print("Would you like to play again? (yes/no)")
    response = input().lower()
    if response == "yes":
        gameover = False
        # Reset player status variables for a new game
        playerMarked = False
        instrumentPlayed = False
        playerSpared = False
        reflectedInPond = False
        #Restart the game
        Begin()
    #End game if player chooses not to play again
    else:
        sys.exit()       

#------------------------------------------------------------------Define Simple Game Over Function -------------------------------------------------------------------
def simpleGameOver():
    sleep(1)
    importantSays("GAME OVER")
    sleep(1)
    gameover = True   
    print("Would you like to play again? (yes/no)")
    response = input().lower()

    # Reset player status variables for a new game
    if response == "yes":
        gameover = False
        runGame()

    #End game if player chooses not to play again
    else:
        sys.exit()
#-------------------------------------------------------------------------Define Title Intro ---------------------------------------------------------------------------
def titleIntro():    
    narratorSays("A Lonely Bard's Journey")
    narratorSays("Chapter 1: A Haunting Melody in a Strange Land")
    continuePrompt()
#-----------------------------------------------------------------------Define Beginning Scenario ------------------------------------------------------------------------

def Begin():

    sleep(1) 
    narratorSays("You awaken in a strange but nostalgic land. The skies above swirl with an unnatural pattern as the colors meld into something you can barely describe.")
    sleep(1)
    narratorSays("Your mind is in disarray, but you feel an all too familiar object by your side, an instrument you once cherished.\n")
    sleep(1)
    # ====== Prompt 1  Choose Instrument =========
    chooseInstrument()
    narratorSays(f"\nYour {selected_instrument}. Somehow the sight of it alone makes your stomach churn as you feel your face distort with grief.")
    narratorSays("...")
    playerSays("Grief?")
    sleep(2)
    narratorSays(f"\nYou can't quite understand why your body reacted with such disdain just now. Maybe trying out your {selected_instrument} will ease your mind.")
    sleep(1)
    # ====== Prompt 2  Play the instrument? =========
    playInstrument()
    sleep(1)
    narratorSays("\nAs you breathe in your new yet strangely familiar surroundings, you wonder what else you may have forgotten.\nA loved one? A purpose? A name?")
    sleep(1)
    narratorSays("A Name...")
    sleep(1)
    # ====== Prompt 3  Player Name =========
    playerName()
    sleep(1)
    narratorSays("\nAs you slowly regain your faculties and rise to your feet your ears pick up on the faintest of haunting melodies dancing in the wind like a siren's call.")
    sleep(1)
    narratorSays("You feel a strangely familiar pull urging every muscle fiber in your body to head towards the source.")
    sleep(1)
    narratorSays("But your mind stays resolute.")
    sleep(1)
    narratorSays("\nYour mood lightens as you realize your newfound resistance.")
    sleep(1)
    playerSays("\nMaybe being a bard has something to do with this weird but useful perk?")
    sleep(1)
    continuePrompt()
    sleep(1)

#--------------------------------------------------------------- Define The Haunting Melody Choice -------------------------------------------------------------

def hauntedChoice():
    
    narratorSays("\nYou ponder for a moment before making your decision.")
    playerSays("\nNothing good ever comes from following a siren's call.\nBut maybe it will lead me to answers about who I am and what I'm doing here...")
    sleep(1)
    # ====== Prompt 4  Choose First Path =========
    systemSays("\nWhat will you do?")
    systemSays("1) Head towards the Source of the Haunting Melody.")
    systemSays("2) Head in the opposite direction away from the Source of the ghoulish tune.")
    systemSays("3) Undecided/Stay put and observe surroundings.")
    choice = input("What is your choice:")
    pathChoice = choice
    while pathChoice in ["1", "2", "3"]:

        if pathChoice == "1":
            narratorSays(f"With nothing to lose but the clothes on your back, your {selected_instrument}, and some hazy memories \nYou venture towards the source of the ghoulish tune, fighting against your every instinct to run the opposite way.")
            sleep(1)
            followMelody()

        elif pathChoice == "2":
            narratorSays("You decide to indulge in your bodies fight or flight instincts and take off in the opposite direction of the lovingly ghoulish tune.")
            sleep(1)
            narratorSays("As the nightmarish melody fades into a whisper, you can only hope this was the right choice.")
            sleep(1)
            continuePrompt()

            liquidChoice()

        elif pathChoice == "3":
            indecisiveEnding()
    else:
        systemSays("Invalid entry.")
        systemSays("1) Head towards the Source of the Haunting Melody.")
        systemSays("2) Head in the opposite direction of where the tune is coming from.")
        systemSays("3) Undecided/Stay put and observe surroundings.")
        pathChoice = input("What is your choice:")
            
#-------------------------------------------------------------Define Choosing Option 1: Follow the Haunting Melody --------------------------------------------------------------------------
def followMelody():
    global playerMarked, playerSpared, encounteredCreature

    encounteredCreature = True

    narratorSays("With each step closer, the melody intensifies as if growing in anticipation of your arrival. \nEnchanting, Embracing, Indulging your six senses with notes that felt like honey dripping from a chalice of shadows.")
    sleep(2)
    narratorSays("Then you see it")
    sleep(2)
    narratorSays("...")
    sleep(3)
    importantSays("And it sees you")
    sleep(2)
    narratorSays("A grotesque figure of meat, tendon, tooth and eyes emerges from the shadows, its form shifting and contorting in a way that causes your mind to reel.")
    sleep(1)
    importantSays("With each passing second, you feel what little sanity you had left threatning to slip away")
    sleep(1)
    importantSays("You can feel your mind fracturing under its gaze alone")
    sleep(1)

    # ====== Prompt 5 Horror Encounter Response Action =========

    systemSays("\nYou must act quick or lose yourself completely?")
    systemSays("1) Attempt to understand what you are looking at.")
    systemSays("2) Pull out your instrument and attempt to play it again.")
    systemSays("3) Try to flee from the creature.")
    systemSays("4) Look Away.")

    choice = input("Enter your choice:")

    if choice == "1":
        narratorSays("You force yourself to focus on the creature, trying to make sense of its grotesque form.")
        sleep(1)
        narratorSays("But the more you look, the more your mind unravels, the creature's presence overwhelming your senses.")
        sleep(1)
        narratorSays("With a final, desperate effort, you try to hold onto your sanity, but it's too late.")
        sleep(1)
        importantSays("Words left unspoken, memories left forgotten, you succumb to the creature's eldritch influence and fuse with its flesh.")
        sleep(1)
        importantSays("Forever engorged in its nightmarish embrace.")
        
        simpleGameOver()

    elif choice == "2":
        narratorSays(f"Desperation takes hold as you pull out your {selected_instrument} once more.\nYou're out of options.")
        sleep(2)
        narratorSays("As your hands shake uncontrollably, you chant a quick prayer and attempt to play anything that will save you from this nightmare.")
        narratorSays("...")
        sleep(2)
        systemSays("Nothing happens")
        sleep(1)
        importantSays("...")
        sleep(1)
        importantSays("Who were you trying to fool?")
        sleep(1)
        importantSays("The Gods have long abandoned this forsaken place. \nAnd you along with it.")
        sleep(1)
        narratorSays(f"As if to mock your futile efforts, the abomination rams into you sending you sprawling to the ground and your {selected_instrument} flying out of reach.")
        sleep(1)
        importantSays("Within less than the time it takes to breath, your mind is snuffed from existence.")
        sleep(3)
        
        simpleGameOver()

    elif choice == "3":
        narratorSays("Panic sets in as you turn to flee from the abomination and its sickly melody.")
        sleep(1)
        narratorSays("You feel your heart pounding in your chest, each beat echoing in your ears as tears stream down your face.")
        sleep(1)
        importantSays("But why are you crying?")
        sleep(1)
        importantSays("...")
        sleep(1)
        narratorSays("You don't realize that you've slowed to a crawl")
        sleep(1)
        narratorSays("In the split second it took for you to realize, something had scratched its way into your mind and was spreading")
        sleep(1)
        importantSays("Your vision blurs as the creature's influence takes hold, your thoughts colliding and melding into new forms. Your very identity begins to unravel.")
        sleep(2)
        narratorSays("Then it stops")
        sleep(1)
        narratorSays("The creature is gone")
        sleep(1)
        narratorSays("You stand at the precepice of madness and sanity. Hope and despair. You feel like you're about to break from just an illusion?")
        narratorSays("...")
        sleep(2)
        importantSays("No, this was real.")
        sleep(1)
        importantSays("But why do you feel so heavy?")

        playerMarked = True
        continuePrompt()
        liquidChoice()


    elif choice == "4":
        narratorSays("Before your eyes begin trailing towards the creatures figure, you look away just in time avoiding its direct gaze.")
        sleep(1)
        narratorSays("Even though you can't see it, you can feel its gaze alone threaten to unravel your mind.")
        sleep(1)
        narratorSays("Was it trying to figure what you were?\nOr was it just toying with your feeble human mind?")
        sleep(1)
        narratorSays("\nIn the midst of your confusion, you notice that you still have enough strength to move your legs.")
        sleep(1)
        narratorSays("All you needed was a momentary distraction to get it to stop focusing on you.")
        sleep(1)
        narratorSays("As if sensing your request, the abomination pulls itself towards the shadows from which it emerged, its grotesque form dissolving into the darkness.")

        playerSpared = True
        continuePrompt()
        liquidChoice()


#--------------------------------------------------------------------- Define Pond Scene ---------------------------------------------------------------------------
def liquidChoice():
    global reflectedInPond, playerMarked, playerSpared, encounteredCreature

    narratorSays("\nWith the threat of the siren's song long gone, you pause for a moment... you have been in this odd yet everchanging land for what feels like an eternity" \
    " and are still in one piece!")
    sleep(2)
    playerSays("\nI'll drink to that once I get out of this hell hole.")
    sleep(3)
    narratorSays("\nWith a slight shift in your wit and the sanity to back it, you decide to not linger around here any longer than necessary.")
    sleep(1)
    continuePrompt()

    narratorSays("\nAfter what felt like hours of wandering through the bizarre almost surreal landscape, you stumble upon a serene pond nestled amidst the twisted flora.")
    sleep(1)
    narratorSays("The water's surface shimmered with an otherworldly glow, reflecting the swirling patterns of the sky above.")
    sleep(1)
    if playerMarked:
        narratorSays("You notice a faint, eerie glow emanating from beneath the water's surface, as if something was calling out to you from the depths.")
        sleep(1)
        playerSays("\nWhy do I feel a sense of deja vu?")
        sleep(1)
    elif playerSpared:
        narratorSays("The pond seems to radiate a calming energy, its tranquil waters inviting you to take a moment of respite from your harrowing journey.")
        sleep(1)
        narratorSays("You feel compelled to approach the pond, drawn by its mysterious allure.")
        sleep(1)
        continuePrompt()

    # ====== Prompt 6  Choose Pond Interaction =========
    systemSays("\nWhat will you do?")
    systemSays("1) Approach the pond and look into its depths.")
    systemSays("2) Ignore the pond and continue on your journey.")
    systemSays("3) Undecided/Stay put and observe surroundings.")
    choice = input("What is your choice:")
    pondChoice = choice
    while pondChoice in ["1", "2", "3"]:

        if pondChoice == "1":
            if playerMarked:
                narratorSays("You cautiously approach the pond, drawn by the eerie glow emanating from its depths.")
                sleep(1)
                narratorSays("As you peer into the water, you see a distorted reflection of yourself")
                sleep(1)
                narratorSays("Your once human features now twisted and warped, a grotesque mockery of your former self.")
                sleep(1)
                narratorSays("A chill runs down your spine as you realize that the pond is showing you a glimpse of what you are becoming.")
                sleep(1)
                narratorSays("With a sense of dread, you reach out to touch the water's surface, hoping to find some solace or answers.")
                sleep(1)
                narratorSays("But as your fingers make contact with the water, you feel a searing pain shoot through your body.")
                sleep(1)
                narratorSays("The pond seems to reject you, its waters churning violently as if trying to expel your presence.")
                sleep(1)
                narratorSays("You quickly withdraw your hand, feeling a sense of relief as the pain subsides.")
                sleep(1)
                narratorSays("Your gaze lingers on your reflection, a mix of fear and sadness welling up inside you.")
                sleep(1)

                # ====== Prompt 7  Look into the pond further? =========
                systemSays("Do you wish to continue looking into the pond?")
                systemSays("1) Yes")
                systemSays("2) No")

                pondLookChoice = input("What is your choice:")
                if pondLookChoice == "1":
                    narratorSays("As you continue to gaze into the pond, your reflection begins to shift and change.")
                    sleep(1)
                    narratorSays("You see a glimpse of a human dressed in tattered clothes, their face obscured by shadows.")
                    sleep(1)
                    narratorSays("Was this once you?")
                    sleep(1)
                    narratorSays("The images in the pond grew clearer with each passing moment, revealing fragments of memories long forgotten.")
                    sleep(1)
                    narratorSays("Then you slip")
                    sleep(1)
                    narratorSays("\nAs you lose your balance and fall into the pond, the water embraces you in its cool depths.")
                    sleep(1)
                    narratorSays("This embrace was different though, you felt a familar warmth as the pond continued showing you more and more of your past self.")
                    sleep(1)
                    narratorSays("You see flashes of a life once lived, filled with music, laughter, and love.")
                    sleep(1)
                    importantSays("Then it fade")
                    sleep(2)
                    importantSays("And you along with it")
                    sleep(2)

                    simpleGameOver()

                elif pondLookChoice == "2":
                    if playerMarked:
                        narratorSays("You feel a deep sense of dread begin settling in your chest as your warped flesh shifts uneasily.")
                        sleep(1)
                        narratorSays("Was this new flesh of yours already attempting to help you? Or was it reeling back in fear?")
                        sleep(1)
                        narratorSays("You wish to rip this disgusting flesh off your body... \nBut deep down, you know, you would just be ripping your skin till you bleed out.")
                        sleep(1)
                        playerSays("\nWhat can I even do anymore...")
                        sleep(3)
                        narratorSays("\nThe thought lingers as dread weighs down on you harder and harder.")
                        sleep(1)
                        narratorSays("You turn and walk away from the pond, feeling that you've had enough.")
                        sleep(1)
                        narratorSays("Each step growing heavier as you head down the only and possibly last path you'll ever walk.")
                        sleep(1)
                        continuePrompt()

                        cavernOfBlood()

                    elif playerSpared:
                        narratorSays("You decide to look away from the pond, though you would have loved to keep staring, you knew it was time to move on.")
                        sleep(2)
                        narratorSays("\nAs you turn away, you feel a sense of peace wash over you, and a sense of gratitude for the brief respite the pond provided.")
                        sleep(1)
                        continuePrompt()

                        cavernOfBlood()

                reflectedInPond = True
                continuePrompt()

            elif playerSpared:
                narratorSays("You approach the pond, captivated by its surviving beauty amidst the broken land.")
                sleep(1)
                narratorSays("As you gaze into the water, you see your reflection staring back at you.")
                sleep(1)
                narratorSays("Though you seem unchanged, you can't help but feel uneasy. All it takes is one wrong decision.")
                sleep(3)
                narratorSays("With a deep breath, you reach out and touch the water's surface, feeling a soothing energy course through your body.")
                sleep(1)
                narratorSays("For a moment, you feel a sense of clarity and purpose, as if the pond has granted you a brief respite from the chaos of this strange land.")
                sleep(1)
                narratorSays("Your gaze lingers on your reflection")
                sleep(1)
                reflectedInPond = True
                continuePrompt()

                # ====== Prompt 8  Look into the pond further? =========
                systemSays("Do you wish to continue looking into the pond?")
                systemSays("1) Yes")
                systemSays("2) No")

                pondLookChoice = input("What is your choice:")
                if pondLookChoice == "1":
                    narratorSays("As you continue to gaze into the pond, your reflection begins to shift and change further.")
                    sleep(1)
                    narratorSays("You see a glimpse of a human dressed in tattered clothes, their face obscured by shadows.")
                    sleep(1)
                    narratorSays("Was this once you?")
                    sleep(1)
                    narratorSays("The images in the pond grew clearer with each passing moment, revealing fragments of memories long forgotten.")
                    sleep(1)
                    narratorSays("Then you slip")
                    sleep(1)
                    narratorSays("\nAs you lose your balance and fall into the pond, the water embraces you in its cool depths.")
                    sleep(1)
                    narratorSays("This embrace was different though, you felt a familar warmth as the pond continued showing you more and more of your past self.")
                    sleep(1)
                    narratorSays("You see flashes of a life once lived, filled with music, laughter, and love.")
                    sleep(1)
                    importantSays("Then it fades")
                    sleep(2)
                    importantSays("And you along with it")
                    sleep(2)

                    simpleGameOver()

                elif pondLookChoice == "2":
                    if playerMarked:
                        narratorSays("You feel a deep sense of dread begin settling in your chest as your warped flesh shifts uneasily.")
                        sleep(1)
                        narratorSays("Was this new flesh of yours warning you? Or was it reeling back in fear?")
                        sleep(1)
                        continuePrompt()

                        cavernOfBlood()

                    elif playerSpared:
                        narratorSays("You decide to look away from the pond, feeling that you've had enough for now.")
                        sleep(1)
                        narratorSays("As you turn away, you feel a sense of peace wash over you, grateful for the brief respite the pond provided.")
                        sleep(1)
                        continuePrompt()
                        cavernOfBlood()

            elif not encounteredCreature:
                narratorSays("You cautiously approach the pond, drawn by its mysterious allure.")
                sleep(1)
                narratorSays("As you peer into the water, you see your reflection staring back at you.")
                sleep(1)
                narratorSays("With a deep breath, you reach out and touch the water's surface, feeling a soothing energy course through your body.")
                sleep(1)
                narratorSays("For a moment, you feel as if the pond is willing to grant you bits and pieces of your framgmented memories.")
                sleep(1)
                narratorSays("\nJust as you begin to feel hopeful, you suddenly lose your balance and slip into the pond.")
                sleep(1)
                narratorSays("The water envelops you, its cool embrace sending a shiver down your spine.")
                sleep(1)
                narratorSays("As you struggle to find your bearings, you feel a strange warmth spreading through your body.")
                sleep(1)
                narratorSays("You see flashes of a life once lived, filled with music, laughter, and love.")
                sleep(1)
                narratorSays("Then it fades")
                sleep(2)
                narratorSays("Not having succumbed to the creature's influence earlier, you feel no change within yourself and swim back to the surface and back to land.")
                sleep(2)
                playerSays("I guess a little dip in the pond never hurt anyone.")
                sleep(1)
                reflectedInPond = True
                narratorSays("You spend what feels like an hour drying off and gathering your thoughts then march forward with renewed determination.")
                continuePrompt()

                cavernOfBlood() 
            

        elif pondChoice == "2":
            narratorSays("You decide to ignore the pond, feeling that it holds no significance for you.")
            sleep(1)
            narratorSays("...")
            sleep(2)
            narratorSays("As you turn away, you can't help but feel a sense of unease, wondering what secrets the pond might have held.")
            sleep(1)
            continuePrompt()
            cavernOfBlood()

        elif pondChoice == "3":
            indecisiveEnding()
    else:
        systemSays("Invalid entry.")
        systemSays("1) Approach the pond and look into its depths.")
        systemSays("2) Ignore the pond and continue on your journey.")
        systemSays("3) Undecided/Stay put and observe surroundings.")
        pondChoice = input("What is your choice:")

#-------------------------------------------------------Define Scene: Cavern of Blood ---------------------------------------------------------------------------
def cavernOfBlood():
    if playerMarked and reflectedInPond:
        narratorSays("\nAs you continue your journey, you stumble upon a cavern pulsating with a sinister energy.")
        sleep(1)
        importantSays("As you near the entrance, you feel your warped flesh pulsate excitedely.")
        sleep(1)
        importantSays("As soon as you step foot inside, the air thickens with the scent of iron and decay.")
        sleep(1)
        importantSays("You want to turn back, but your body moves forward of its own accord.")
        sleep(1)
        importantSays("The walls made of flesh and bone, seemingly tossed together with viscous liquid that oozed down like blood.")
        sleep(1)
        importantSays("As you begin to lose yourself in the cavern's nightmarish embrace, you feel your body begin to shift and change.")
        sleep(1)
        importantSays("Your flesh melds with the cavern walls, as you realize that the abomination you encountered earlier was but a harbinger of your own transformation.")
        sleep(1)
        importantSays("You were nothing more than prey being led to the slaughter... the land's grotesque desires.")
        sleep(1)
        
        simpleGameOver()
        
    elif playerMarked and not reflectedInPond:
        narratorSays("\nAs you continue your journey, you stumble upon a cavern pulsating with a sinister energy.")
        sleep(1)
        narratorSays("Even though you feel uneasy, your warped flesh seems to pull you towards the entrance.")
        sleep(1)
        narratorSays("As soon as you step foot inside, the air thickens with the scent of iron and decay.")
        sleep(1)
        narratorSays("You want to turn back, but your body moves forward of its own accord.")
        sleep(1)
        narratorSays("The walls made of flesh and bone, seemingly tossed together with viscous liquid that oozed down like blood.")
        sleep(1)
        narratorSays("As you begin to lose yourself in the cavern's nightmarish embrace, you suddenly feel your instrument tugging at your side.")
        sleep(1)
        narratorSays("You desperately reach for it even though you know it won't help.")
        sleep(1)
        narratorSays("With a final effort, you play a haunting melody that resonates through the cavern.")
        sleep(1)
        narratorSays("The cavern seems to respond to your music, the walls pulsating in time with the melody.")
        sleep(1)
        narratorSays("In that moment, you feel a fleeting sense of control over your transformation, as if your music has momentarily staved off the land's grotesque desires.")
        sleep(1)
        narratorSays("But how did you even know that melody?")
        sleep(1)
        continuePrompt()
        narratorSays("Your body feels heavy, your vision blurs as you feel the cavern's attempt to bind you in it's embrace")
        sleep(1)
        narratorSays("With what little energy you have left, you claw and scratch your way passed the ridges boulders and sharpened stalagmites")
        narratorSays("...")
        importantSays("You crawl and scrape.., scavenge and claw your way forward")
        sleep(2)
        importantSays("You feel your body being tugged at from multiple angles as you head deeper and deeper into the darkness.")
        sleep(3)
        importantSays("Then you pause")
        sleep(3)
        importantSays("You catch a momentary glimpse of yourself in a water droplet falling from above.")
        sleep(2)
        importantSays("You do not move... you do not breath... for fear that whatever you just saw would be your reality forever.")
        importantSays("...")
        importantSays("You stay like this...")
        sleep(3)
        importantSays("Forever")

        simpleGameOver
    
    elif playerSpared and reflectedInPond:
        narratorSays("\nAs you continue your journey, you stumble upon a cavern pulsating with a sinister energy.")
        sleep(1)
        narratorSays("Though you feel uneasy, you decide to enter the cavern, drawn by an inexplicable force.")
        sleep(1)
        narratorSays("As soon as you step foot inside, the air thickens with the scent of iron and decay.")
        sleep(1)
        narratorSays("You want to turn back, but your determination to find any clues dwarfs your fears.")
        continuePrompt()
        sleep(1)
        narratorSays("The walls made of flesh and bone, seemingly tossed together with viscous liquid that oozed down like blood.")
        sleep(1)
        narratorSays("As you begin to lose yourself in the cavern's nightmarish embrace, you suddenly feel your instrument tugging at your side.")
        sleep(1)
        narratorSays("You desperately reach for it even though you know it won't help.")
        # ======= Prompt 9  Play Instrument in Cavern? =========
        systemSays(f"Will you play your {selected_instrument}?")
        systemSays("1) Yes")
        systemSays("2) No")
        choice = input("What is your choice:")
        if choice == "1":
            narratorSays(f"With a final effort, you play a haunting melody that resonates through the cavern.")
            sleep(1)
            narratorSays("The cavern seems to respond to your music, the walls pulsating in time with the melody.")
            sleep(1)
            narratorSays("In that moment, you feel a fleeting sense of control over your fate, as if your music has momentarily staved off the land's grotesque desires.")
            sleep(1)
            narratorSays("But how did you even know that melody?")
            sleep(1)
            continuePrompt()

        elif choice == "2":
            narratorSays(f"You decide against playing your {selected_instrument}, feeling that it won't help in this situation.")
            sleep(1)
            importantSays("Then you hear it.")
            sleep(1)
            importantSays("The grotesque amalgamation of flesh and blood that had spared you earlier.")
            sleep(1)
            importantSays("It had been waiting for you.")
            sleep(1)
            narratorSays("You hold your breath and hug the walls praying for any chance of escape.")
            sleep(1)
            importantSays("But it was no use.")
            sleep(3)
            importantSays("The grotesque amalgamation of flesh and blood that had spared you earlier was only toying with you.")
            sleep(1)
            importantSays("This time, there was no escape.")
            sleep(1)

            simpleGameOver()

    elif playerSpared and not reflectedInPond:
        narratorSays("\nAs you continue your journey, you stumble upon a cavern pulsating with a sinister energy.")
        sleep(1)
        narratorSays("Though you feel uneasy, you decide to enter the cavern, drawn by an inexplicable force.")
        sleep(1)
        narratorSays("As soon as you step foot inside, the air thickens with the scent of iron and decay.")
        sleep(1)
        narratorSays("You want to turn back, but your determination to find any clues dwarfs your fears.")
        continuePrompt()
        sleep(1)
        narratorSays("The walls made of flesh and bone, seemingly tossed together with viscous liquid that oozed down like blood.")
        sleep(1)
        narratorSays("As you begin to lose yourself in the cavern's nightmarish embrace, your suddenly reminded of your instrument at your side.")
        sleep(1)
        narratorSays("You desperately reach for it even though you know it won't help.")
        # ======= Prompt 10 Play Instrument in Cavern? =========
        systemSays(f"Will you play your {selected_instrument}?")
        systemSays("1) Yes")
        systemSays("2) No")
        choice = input("What is your choice:")
        if choice == "1":
            sleep(1)
            narratorSays(f"With a final effort, you attempt to play a tune on your {selected_instrument}.")
            sleep(1)
            narratorSays("But all that comes out is a discordant noise that echoes through the cavern.")
            sleep(1)
            narratorSays("The cavern seems to respond to your failed attempt at music, the walls pulsating ominously as you hear the sound of dripping liquid growing louder.")
            sleep(1)
            narratorSays("You hold your breath and hug the walls, hoping to avoid whatever horrors lurk within.")
            sleep(1)
            importantSays("But it was no use.")
            sleep(3)
            importantSays("The grotesque amalgamation of flesh and blood that had spared you earlier found you.")
            sleep(1)
            importantSays("This time, there was no escape.")
            sleep(1)
            simpleGameOver()

        elif choice == "2":
            narratorSays(f"You decide against playing your {selected_instrument}, feeling that it won't help in this situation.")
            sleep(1)
            importantSays("Then you hear it.")
            sleep(1)
            importantSays("The grotesque amalgamation of flesh and blood that had spared you earlier.")
            sleep(1)
            importantSays("It had been waiting for you.")
            sleep(1)
            narratorSays("You hold your breath and hug the walls praying for any chance of escape.")
            sleep(1)
            importantSays("But it was no use.")
            sleep(3)
            importantSays("The grotesque amalgamation of flesh and blood that had spared you earlier was only toying with you.")
            sleep(1)
            importantSays("This time, there was no escape.")
            sleep(1)

            simpleGameOver()
    elif not encounteredCreature:
        narratorSays("\nAs you continue your journey, you stumble upon a cavern pulsating with a sinister energy.")
        sleep(1)
        narratorSays("Though you feel uneasy, you decide to enter the cavern against your own good judgment.")
        sleep(3)
        narratorSays("\nAs soon as you step foot inside, the air thickens with the scent of iron and decay.")
        sleep(1)
        narratorSays("You want to turn back")
        sleep(2)
        importantSays("but your pure mind is clouded with an unshakable compulsion.")
        continuePrompt()
        sleep(1)
        importantSays("The walls made of flesh and bone, seemingly slathered together with viscous liquid, oozes with each pulse.")
        sleep(1)
        importantSays("You begin to lose yourself in the cavern's nightmarish embrace") 
        narratorSays(f"when suddenly... your {selected_instrument} vibrates softly.")
        sleep(1)
        narratorSays("You desperately reach for it even though you know it won't help.")
        # ======= Prompt 11 Play Instrument in Cavern? =========
        systemSays(f"Will you play your {selected_instrument}?")
        systemSays("1) Yes")
        systemSays("2) No")
        choice = input("What is your choice:")
        if choice == "1":
            sleep(1)
            narratorSays(f"With a final effort, you attempt to play a tune on your {selected_instrument}.")
            sleep(1)
            narratorSays("But all that comes out is a discordant noise that echoes through the cavern.")
            sleep(1)
            narratorSays("The cavern seems to respond to your failed attempt at music, the walls pulsating ominously as you hear the sound of dripping liquid growing louder.")
            sleep(1)
            narratorSays("You hold your breath and hug the walls, hoping to avoid whatever horror lurks within.")
            sleep(1)
            importantSays("But it was no use.")
            sleep(3)
            importantSays("The grotesque amalgamation of flesh and blood that had spared you earlier found you.")
            sleep(1)
            importantSays("This time, there was no escape.")
            sleep(1)
            simpleGameOver()

        elif choice == "2":
            narratorSays(f"You decide against playing your {selected_instrument}, feeling that it won't help in this situation.")
            sleep(1)
            importantSays("Then you hear it.")
            sleep(1)
            importantSays("A horrid sound of flesh and bone sliding across the ground.")
            sleep(1)
            importantSays("You freeze, fear crippling your thoughts as this grotesque amalgamation of flesh and blood emerges from the shadows.")
            sleep(1)
            importantSays("Before you have time to react, it lunges at you.")
            sleep(1)
            importantSays("Escape was never an option.")
            sleep(1)
            simpleGameOver()

#------------------------------------------------------------------------ Define End Scene----------------------------------------------------------------------------
def endScene():
    narratorSays("To be continued...")
    sleep(2)
    importantSays("Thank you for playing A Lonely Bard's Journey!")
    sleep(2)
    importantSays("Stay tuned for Chapter 2!")

# ----------------------------------------------------------------------- Main Game Loop ---------------------------------------------------------------------------
def runGame():
    global selected_instrument
    global encounteredCreature, playerMarked, playerSpared, reflectedInPond, instrumentPlayed

    encounteredCreature = False
    playerMarked = False
    playerSpared = False
    reflectedInPond = False
    instrumentPlayed = False
    
    titleIntro()
    setTextSpeed()
    Begin()
    hauntedChoice()
    liquidChoice()
    cavernOfBlood()
    endScene()


# actually start the game
if __name__ == "__main__":
    runGame()
