# Typing Game Solver

A Python program to solve [this English typing game](https://10fastfingers.com/typing-test/english)

## Usage
1. Capture the area where English words are displayed
2. Just wait for the program to solve the game

## How it works
1. Capture the specified area on the screen
2. OCR extracts English words from the captured image
3. Type the extracted English words with `PyAutoGui`
4. Repeat 1 ~ 3 until the game ends

## Demo
![demo](https://github.com/harupy/typing_game/blob/master/video.gif)
