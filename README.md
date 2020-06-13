# Stormtrooper Voicebox

Ability to Puppeteer while Trooping.  Inspired by the Disney's Stormtroopers walking around Black Spire Outpost.

  * [Supplies](#supplies)
    + [Note](#note)
  * [Source](#source)
    + [Notes](#notes)
    + [TODO](#todo)
  * [Systemd Service](#systemd-service)
  * [References](#references)

## Supplies
- [Raspberry Pi Zero](https://www.adafruit.com/?q=rasberry%20pi%20zero)
- [Simple RF L4 Receiver - 315MHz](https://www.adafruit.com/?q=Simple%20RF%20M4%20Receiver)
- [USB Audio Adapter - Works with Raspberry Pi](https://www.adafruit.com/product/1475)
- [Hammer Header Male - Solderless Raspberry Pi Connector](https://www.adafruit.com/product/3662)
- [Keyfob 4-Button RF Remote Control - 315MHz](https://www.adafruit.com/product/1095)
- [Premium Female/Female Jumper Wires](https://www.adafruit.com/product/1950)
- Battery Pack to power the Raspberry Pi Zero on the move similar to [this one](https://www.amazon.com/Portable-RAVPower-22000mAh-Li-polymer-Smartphone/dp/B01G1XH46M/)
- Sound files some can be found [here](https://www.soundboard.com/sb/stormtrooper_sounds)

### Note
- If you don't have the kit for the Hammer Header you might want to consider https://www.adafruit.com/product/3413.
- If you don't have all the necessary pieces for the Raspberry Pi Zero you might want to consider a [CanaKit](https://www.amazon.com/CanaKit-Raspberry-Wireless-Complete-Starter/dp/B072N3X39J)

## Source

Copy sounds.py to your Raspberry Pi Zero.  The code needs some refactoring, but it works.

### Notes
- Depending on where you copy the source code to you might need to update the voicebox.serice file.
- Depending on which pins you attach your cables you may need to update the source code

### TODO
- Refactor the code so that you can add additional button combos.

## Systemd Service

Copy to /usr/lib/systemd/system/voicebox.service on your Raspberry Pi Zero

```
systemctl enable voicebox.service # start service when the device starts
systemctl start voicebox.service # to test the serice without restarting
systemctl stop voicebox.service # stop the service
systemctl status voicebox.serice # service status
```
### References
Similar project concept [Panic Button (315Mhz)](https://www.raspberrypi.org/forums/viewtopic.php?t=161149)
