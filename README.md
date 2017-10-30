# Python Typing Game
Python plays an [English typing game](https://10fastfingers.com/typing-test/english).<br>
Here's how it works on [my YouTube channel](https://www.youtube.com/watch?v=Z4TcF5bT0FE).

# Required Libraries
- Numpy
- Matplotlib
- Pillow
- Selenium
- Pytesseract
- OpenCV
- PyAutoGUI

# How It Works
1. Selenium open Chrome and goes to [Typing Test English](https://10fastfingers.com/typing-test/english).
2. Pillow captures the area where English words are displayed.
3. OpenCV bainarizes the captured image to improve the accuracy of pytesseract.
4. Pytesseract extracts English words from the image.
5. Pyautogui automatically types the English words.

