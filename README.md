
### Key Points:
- **Overview:** Provides a brief introduction to the game and its theme.
- **How to Play:** Instructions on starting the game, making choices, and understanding the game mechanics, including combat and emotional state.
- **Controls:** Basic controls and their functions.
- **Credits:** Acknowledgement of the game's creators and contributors.
- **Installation:** Steps to set up and run the game.
- **Future Updates:** Information on the full release and what players can expect.

This README file gives players all the essential information they need to enjoy the game and understand its mechanics.

# Lost 1.5

**For Scream Secrets Game Jam**  
*22 AUG 2024*

## Overview

**Lost 1.5** is a text-based interactive horror game where you wake up in a mysterious forest with no memory of how you got there. Armed only with a flashlight, you must navigate through the dark woods, confront terrifying specters, and unravel the secrets that lie within. The game focuses on atmospheric storytelling, timed decision-making, and a moral system that affects the outcome of your journey.

## How to Play

### Starting the Game
- Launch the game by running the `main.py` script.
- From the main menu, press `1` to start the game or `2` to exit.

### Exploration
- As you progress, you'll be presented with choices that guide your journey. Simply follow the prompts and make decisions that feel right to you.
- The game uses atmospheric descriptions and slow-revealing text to immerse you in the eerie environment.

### Combat
- **Timed Battles:** When a specter appears, you’ll need to react quickly.
  - You have **5-7 seconds** to press `Enter` and shine your light on the specter.
  - **Success:** The specter is banished, and your emotional state may improve.
  - **Failure:** The specter attacks, leading to a decrease in your moral state, and potentially ending the game.

### Emotional State
- **Emotional Levels:** Your character's state of mind will change based on your decisions and battle outcomes.
  - **States range from:** Determined, Confused, Sad, Hopeless, Frantic, to Hysterical.
  - **Impact:** Your emotional state influences the story and its outcomes. Reaching the `Hysterical` state may lead to a game-over scenario.

### Making Choices
- The game adapts based on your choices. Every decision shapes the narrative, leading to different paths and possible endings.
- Choices include deciding which path to take, whether to confront or flee from dangers, and how to interact with the environment.

### Sound Effects
- The game features immersive sound effects to enhance the experience. These include ambient sounds of the forest, eerie whispers, and unsettling noises that accompany key moments in the story.

## Credits
- **Designed by:** Red Door Creative
- **Story by:** Red Door Creative
- **Sound effects by:** mastersoundboy2005, Poinrnemoprod, Adriann, Tomattka, and dibko

## Controls
- **Enter Key:** Used to interact during timed battles.
- **Keyboard Input:** Used to select options and make choices throughout the game.

## Ending
- After completing the game, you'll be presented with a thank-you message and a prompt to stay tuned for the full release in Fall 2026.

## Requirements
- **Python Version:** 3.12.5 or higher

- Installation

    Clone or download the repository to your local machine.
    Ensure you have the required Python version and dependencies installed.
    Navigate to the game directory and run main.py to start the game.

Future Updates

The full version of the game is expected to be released in Fall 2026. Stay tuned for more secrets, expanded storylines, and new challenges that will test your courage and decision-making skills.

Thank you for playing Lost 1.5! We hope you enjoyed the experience and look forward to sharing the full story with you soon.
- **Dependencies:** 
  - `pygame` (For sound playback)
  - `keyboard` (For detecting keypresses)
  
Install these dependencies using pip:
```bash
pip install pygame keyboard
