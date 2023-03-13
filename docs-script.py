import pyautogui
import time
import random

time_delay_s = {
    "start": 10,
    "chr": 0.1,
    "dot": 30,
    "new_line": 45,
    "space": 5,
}


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


time.sleep(time_delay_s["start"])
keys = {"dot": 0, "new_line": 0, "space": 0}

print("started")
for i in words:
    match i:
        case ".":
            write_word(i, random.random() * time_delay_s["dot"])
        case "\n":
            break
            write_word(i, random.random()*time_delay_s["new_line"])
        case " ":
            write_word(i, random.random()*time_delay_s["space"])
        case _:
            write_word(i, random.random()*time_delay_s["chr"])
            # write_word(j, random.random()*2)
            # else:
            # write_word(j, random.random()*0.14)

print("finished")
