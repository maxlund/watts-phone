#! /usr/bin/env python

import vlc
import os
import time


def play_mp3s():
    for f in os.listdir('resources'):
        if f.endswith('.mp3'):
            print(f'Playing: {f}')
            player = vlc.MediaPlayer(f'resources/{f}')
            player.play()
            time.sleep(1.5)
            duration = player.get_length() / 1000.0
            time.sleep(duration)

    play_mp3s()


if __name__ == '__main__':
    play_mp3s()
