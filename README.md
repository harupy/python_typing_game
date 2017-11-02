# Python Typing Game
Python plays an [English typing game](https://10fastfingers.com/typing-test/english).

# Required Libraries
- Numpy
- Matplotlib
- Pillow
- Selenium
- Pytesseract
- OpenCV
- PyAutoGUI

# How It Works

[Here's how it works.](https://www.youtube.com/watch?v=t3jwDWAF5y0)

1. Selenium opens up Chrome and goes to the game webpage(https://10fastfingers.com/typing-test/english).
2. Pillow captures an image from the screen.
3. OpenCV binarizes the captured image to improve the accuracy of OCR.
4. Pytesseract extracts English words from the binarized image.
5. PyAutoGUI automatically types the extracted English words.
<br>

![result](https://github.com/harupy/typing_game/blob/master/video.gif)
