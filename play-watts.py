#! /usr/bin/env python

import pygame
import os

pygame.mixer.init()


def play_mp3s():
    for f in os.listdir('resources'):
        i = 0
        if f.endswith('.mp3'):
            print(f'Playing: {f}')
            sound = pygame.mixer.Sound(f'resources/{f}')
            playing = sound.play()
            while playing.get_busy():
                pygame.time.delay(100)

    play_mp3s()


if __name__ == '__main__':
    play_mp3s()
