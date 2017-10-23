from PIL import Image
from PIL import ImageGrab
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
import pyautogui as pyag
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import cv2


def main():

    # change current directory to the directory where this script file is
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # specify where tesseract exe file is
    tesseract_dir = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    pytesseract.pytesseract.tesseract_cmd = tesseract_dir

    # url of the english typing game site
    url = 'https://10fastfingers.com/typing-test/english'

    # create plot area for the captured image
    fig, ax = plt.subplots()
    mngr = plt.get_current_fig_manager()
    mngr.window.setGeometry(10, 800, 1300, 250)
    plt.pause(0.001)

    # open Chrome and go to the game site
    chrome_options = Options()
    chrome_options.add_argument('--window-position=0,0')
    chrome_options.add_argument('--window-size=1000,600')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    print('Loading...')
    driver.get(url)
    time.sleep(3)

    while True:  # infinite loop until the game ends
        print('-----------------------------------------')
        print('Extracted words')
        print('-----------------------------------------')

        # captured image from the screen
        img = ImageGrab.grab(bbox=(120, 308, 1213, 430))

        # display the captured image in the plot area created before
        ax.imshow(img)
        plt.pause(0.001)

        # binarize the captured image to improve
        # the accuracy of optical character recognition (ocr)
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)[1]
        img = Image.fromarray(img)

        # extract words from the binarized image
        ocr_words = pytesseract.image_to_string(img).split(' ')

        for words in ocr_words:
            # the last word in each row is connected to
            # the first word in the next row with '\n' or '\n\n'
            # that's why I split words here or it will cause errors
            if '\n\n' in words:
                words = words.split('\n\n')
            elif '\n' in words:
                words = words.split('\n')
            else:
                words = [words]

            for word in words:
                try:
                    print(word)
                except Exception as e:
                    print('unicode error')
                # type word using puautogui
                pyag.typewrite(word.replace(' ', '') + ' ')
                time.sleep(0.2)

        if len(ocr_words) < 10:
            print('Done!')
            time.sleep(3)
            driver.quit()
            break


if __name__ == '__main__':
    main()
