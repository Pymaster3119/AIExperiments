import time
import pyautogui
import pyperclip
from PIL import Image
from tkinter import Tk

num_words = 10
main = Tk()
main.withdraw()
time.sleep(5)
curr_word = "Abomination"
for x in range(num_words):
    #Make Chat-GPT prompt
    #Assumes a 1440x900 screen
    pyautogui.leftClick(541,827, duration=0)
    pyautogui.typewrite("add one word to this so that, eventually, it will form a coherent sentence. Return the entirety of the sentence thus far including the word. Do not add a period The sentence thus far is: " + curr_word)
    time.sleep(0.1)
    pyautogui.click(1200,845)
    time.sleep(5)
    #Copy response
    responsearea = list(pyautogui.locateAllOnScreen("/Users/aditya/Desktop/AI Experiments/SentenceBuilder/Screenshot 2024-07-11 at 10.58.09 PM.png"))
    print(responsearea)
    pyautogui.moveTo(responsearea[0])
    pyautogui.moveRel(0,-35)
    pyautogui.dragRel(100,0,2,button="left")
    pyautogui.moveRel(-90,0)
    pyautogui.rightClick(pyautogui.position().x, pyautogui.position().y)
    pyautogui.moveRel(45,45)
    pyautogui.rightClick(pyautogui.position().x, pyautogui.position().y)
    curr_word = main.clipboard_get()
    print(curr_word)
    time.sleep(10)