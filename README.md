# python_typing_game
Python plays an English typing game ([Typing Test English](https://10fastfingers.com/typing-test/english)).

# Required libraries
- Numpy
- Matplotlib
- Pillow
- Selenium
- Pytesseract
- OpenCV
- PyAutoGUI

# How it works
1. selenium open Chrome and goes to [Typing Test English](https://10fastfingers.com/typing-test/english).
2. pillow captures the area where English words are displayed.
3. opencv bainarizes the captured image to improve the accuracy of pytesseract.
4. pytesseract extracts English words from the image.
5. pyautogui automatically types the English words.

Here's how it works on my Youtube channel : https://www.youtube.com/watch?v=Z4TcF5bT0FE

# Improvements
1. pytesseract sometimes misrecognizes words which start with lower-case "w".
2. The arguments of ImageGrab work only for my enviroment. I'm trying to implement a program like window's snipping tool to get the pixel coordinates on the screen.
