######  Check sound devices:
```
cat /proc/asound/modules
0 snd_hda_intel
1 snd_hda_intel
```

put in `~/.asoundrc` to configure default output (example below will device 1)

```
pcm.!default {
     type hw
     card 1
}
ctl.!default {
     type hw
     card 1
}
```

Pygame will also fail without the required mixer libraries, so you also need to run `apt-get install libsdl2-mixer-2.0-0`
https://www.jeffgeerling.com/blog/2022/playing-sounds-python-on-raspberry-pi

Docs for pygame mixer module:

https://www.pygame.org/docs/ref/mixer.html

https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound


######  Run script on raspberry pi startup:
https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/

tldr:
make a log directory for cronjob:
```
cd
mkdir logs
```
make shell-script `launcher.sh` with:
```
!/bin/sh
python3 <path-to-python-script>/play-watts.py
```
then:
```
chmod 755 launcher.sh
sudo crontab -e
```
enter this line:
```
@reboot sh /home/pi/bbt/launcher.sh >/home/pi/logs/cronlog 2>&1
```
Download Alan Watts lectures from https://archive.org/details/alanwattscollection and put them in the `resources` directory
