######  Set correct audio output device:
```
cat /proc/asound/modules
0 snd_hda_intel
1 snd_hda_intel
```

put in `~/.asoundrc` to configure default output (example below will use device 1)

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
######  Install dependencies:
Install python3-vlc:
```
pip3 install python-vlc
``` 
VLC should be pre-installed on Pi, otherwise 
```
sudo apt-get install vlc
```
https://www.jeffgeerling.com/blog/2022/playing-sounds-python-on-raspberry-pi

######  Run script on raspberry pi startup:
https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/

tldr:
make a log directory for cronjob:
```
cd
mkdir logs
```
make shell script `launcher.sh` with:
```
#!/bin/sh
python3 <path-to-python-script>/play-watts.py
```
then:
```
chmod 755 launcher.sh
sudo crontab -e
```
enter this line:
```
@reboot sh <path-to-shell-script>/launcher.sh >/home/pi/logs/cronlog 2>&1
```
Download Alan Watts lectures as mp3 files to the `resources` directory from:

https://archive.org/details/alanwattscollection
