import pyautogui
import time
import random


def get_words():
    f = open("Input-Text.txt", "r")
    words = f.read()
    f.close()
    return words


def write_word(word: str, delay_s: int):
    time.sleep(delay_s)
    pyautogui.write(word)
    return None


words = get_words()
print("got words")
# time_delay_s = 4

# time.sleep(time_delay_s)
keys = {"dot": 0, "new_line": 0, "space": 0}

print("started")
for i in words:
    for j in i:
        if j == ".":
            keys["dot"] += 1
        if j == "\n":
            keys["new_line"] += 1
        if j == " ":
            keys["space"] += 1
            # write_word(j, random.random()*2)
        # else:
            # write_word(j, random.random()*0.14)

print(keys.values())
