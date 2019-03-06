# Typing Game Solver

A Python program to solve [this English typing game](https://10fastfingers.com/typing-test/english)

## Usage
1. Run `python typing_game.py`
2. Capture the area where English words are displayed
3. Just wait for the game to end

## How this works
1. Capture the specified area on the screen
2. Apply OCR to the captured image to extract English words 
3. Type the extracted words with `PyAutoGui`
4. Repeat 1 ~ 3 until the game ends

## Demo
![demo](https://github.com/harupy/typing_game/blob/master/video.gif)
