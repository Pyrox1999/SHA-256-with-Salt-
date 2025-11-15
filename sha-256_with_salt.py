import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame
import hashlib
import sys
import os

pygame.mixer.music.load("song.ogg") #Palrom
pygame.mixer.music.play(-1)

level = -1
target = ""
target2=""
made=False
optional=False

def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def draw():
    global level, target,target2,optional
    screen.clear()
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        made=False
        screen.blit("back", (0, 0))
        screen.draw.text("Enter the word you want to encrypt:", center=(400, 130), fontsize=24, color=(25, 0, 55))
        screen.draw.text(target, center=(400, 180), fontsize=24, color=(55, 25, 0))
    elif level == 2:
        screen.blit("back",(0,0))
        screen.draw.text("Do you want to use Salt? (y/n)", center=(400, 130), fontsize=24, color=(25, 0, 55))
    elif level==3:
        screen.blit("back",(0,0))
        if not optional:
            screen.draw.text("Your word in SHA-256 is: \n"+target2, center=(400, 130), fontsize=24, color=(25, 0, 55))
        if optional:
            screen.draw.text("Your word in SHA-256 with Salt is: \n"+target2, center=(400, 130), fontsize=24, color=(25, 0, 55))

def on_key_down(key, unicode=None):
    global level, target,optional
    if key==keys.ESCAPE:
        pygame.quit()
    if key == keys.BACKSPACE and (level==1 or level==3):
        target = ""
    elif key == keys.RETURN and level==1:
        level = 2
    elif unicode and key != keys.RETURN and level==1:
        target += unicode
    elif key==keys.Y and level==2:
        optional=True
        level=3
    elif key==keys.N and level==2:
        optional=False
        level=3

def update():
    global target,target2
    global made
    global level
    global optional

    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
    elif level -1 and keyboard.space:
        level = 0
    if level==3 and keyboard.space:
        level=0
    if not made and level==3:
        made=True
    
        if optional:
            salt_bytes = os.urandom(16)
            salt = salt_bytes.hex()
            combined = f"{target}::{salt}"
            target2 = sha256_hash(combined)
        else:
            target2 = sha256_hash(target)
        print(target2)

pgzrun.go()
