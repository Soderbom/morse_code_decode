from PIL import ImageGrab
import pyautogui as gui
import time
import json

def position_cursor():
    while True:
        try:
            print(gui.position())
            time.sleep(1)
        except KeyboardInterrupt:
            break

    return gui.position()

def read_code(mouse):
    morse_pattern = []
    image = ImageGrab.grab()
    prev_color = image.getpixel(mouse)
    now = time.time()
    while True:
        try:
            image = ImageGrab.grab()
            color = image.getpixel(mouse)
            if color != prev_color:
                t = time.time() - now
                status = True if color == color_on else False
                morse_pattern.append((t, status))
            prev_color = color
        except KeyboardInterrupt:
            break
    return morse_pattern


def translate_code(morse_pattern, short, morse_to_alpha):
    msg = ""
    letter = ""
    
    long = short * 3
    pause = short * 7

    for i in range(len(morse_pattern)):
        t = morse_pattern[i][0] - morse_pattern[i-1][0]    
        status = morse_pattern[i-1][1]
        values = [abs(t-short), abs(t-long), abs(t-pause)]
        if values.index(min(values)) == 0 and status:
            # code.append(".")
            letter += '.'
        elif values.index(min(values)) == 0 and not status:
            #code.append("sp")
            continue
        elif values.index(min(values)) == 1 and status:
            #code.append("-")
            letter += '-'
        else:
            #code.append("nl")
            try:
                msg += morse_to_alpha[letter]
            except:
                print("Letter unreadable")
            letter = ""
            if values.index(min(values)) == 2 and not status: 
                msg += " "
    try: 
        msg += mtoa[letter]
    except:
        pass
    return msg



color_on = (255,255,255)


mouse = position_cursor()
morse_pattern = read_code(mouse) 

short = min([morse_pattern[i][0] - morse_pattern[i-1][0] for i in range(1, len(morse_pattern))])

with open("morse_to_alpha.json") as f:
    mtoa = json.load(f)

msg = translate_code(morse_pattern, short, mtoa)

print("\n")
print(f"The message was: {msg}")
