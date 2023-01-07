#! /usr/bin/env python

import vlc
import os
import time
import RPi.GPIO as gpio


def play_mp3s(pin_number):
    for f in os.listdir('resources'):
        if f.endswith('.mp3'):
            print(f'Playing: {f}')
            player = vlc.MediaPlayer(f'resources/{f}')
            player.play()
            time.sleep(1.5)
            while player.is_playing():
                pin_input = gpio.input(pin_number)
                if pin_input == 1:
                    player.set_audio_volume(0)
                else:
                    player.set_audio_volume(100)
                time.sleep(0.2)

    play_mp3s(pin_number)


if __name__ == '__main__':
    pin_number = 7
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin_number, gpio.IN)
    play_mp3s(pin_number)
