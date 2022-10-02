import sys
import argparse
import pygame
from pygame.locals import *
from time import sleep
import json

# Dot 183
# Dash 8722
# Trash space 32 8202

def turn_on(delay):
    pygame.draw.rect(window, "white", pygame.Rect(0, 0, 200, 200))
    pygame.display.update()
    pygame.time.delay(delay)
    pygame.draw.rect(window, "black", pygame.Rect(0, 0, 200, 200))
    pygame.display.update()

if len(sys.argv) < 2: 
    print("Add you text as an argument")
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('text', help='Text to morse')
parser.add_argument('-r', '--repeat', default=1, help='Repeat message X times. Default=1')
args = parser.parse_args()

with open("alpha_to_morse.json") as f:
    atom = json.load(f)

short = 200
long = short * 3 
pause = short * 7 

pygame.init()

window = pygame.display.set_mode((200,200))
clock = pygame.time.Clock()
window.fill((0, 0, 0))
pygame.display.update()

pygame.time.delay(3000)
for _ in range(int(args.repeat)):
    print("Loop")
    for letter in args.text.upper():
        pygame.time.delay(pause) if letter == ' ' else pygame.time.delay(long)
        try:
            for symbol in atom[letter]:
                # Skip if empty
                delay = short if symbol == '.' else long 
                turn_on(delay)
                pygame.time.delay(short)
        except KeyError:
            continue
        except KeyboardInterrupt:
            pygame.quit()

input("Press enter to exit.")
pygame.quit()


