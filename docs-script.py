import pyautogui
import time
import random

time_delay_s = {
    "start": 5,
    "chr": 0.2,
    "dot": 0.5,
    "new_line": 0.1,
    "space": 1,
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


# time.sleep(time_delay_s)
keys = {"dot": 0, "new_line": 0, "space": 0}

print("started")
for i in words:
    match i:
        case ".":
            keys["dot"] += 1
        case "\n":
            keys["new_line"] += 1
        case " ":
            keys["space"] += 1
        # case _:

            # write_word(j, random.random()*2)
            # else:
            # write_word(j, random.random()*0.14)

print(keys.values())
