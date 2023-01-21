#! /usr/bin/env python

import vlc
import os
import time
import RPi.GPIO as gpio

resources_path = '/home/admin/watts-phone/resources'
pin_number = 7

gpio.setmode(gpio.BOARD)
gpio.setup(pin_number, gpio.IN)

vlc_instance = vlc.Instance('--loop')
medias = [vlc_instance.media_new(f'{resources_path}/{f}') for f in os.listdir(resources_path) if f.endswith('.mp3')]
list_player = vlc_instance.media_list_player_new()
list_player.set_media_list(vlc_instance.media_list_new(medias))
media_player = list_player.get_media_player()

list_player.play()
while True:
    pin_input = gpio.input(pin_number)

    if pin_input == 1:
        media_player.audio_set_volume(0)
    else:
        media_player.audio_set_volume(100)

    if list_player.is_playing():
        time.sleep(0.2)
    else:
        list_player.play()
