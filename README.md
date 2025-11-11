# DuckyDiagnostic

A small cross-platform troubleshooter using the PicoDucky!

This is being subbmitted to Hack Club's YSWS [PicoDucky](picoducky.hackclub.com). A PicoDucky is a custon PCB that acts as a HID device and is open soursed on Github [here](https://github.com/Outdatedcandy92/PicoDucky).

### ⏰ Time Spent
_calculated through hackatime_

![](https://hackatime-badge.hackclub.com/U078VN0UU2K/DuckyDiagnostic
)
![](https://hackatime-badge.hackclub.com/U078VN0UU2K/PicoDucky%20-%20Local
)

---

## 🤩 My project

When the USB is plugged in, press the button one to three times to signal the OS. This opens a terminal and runs several commands to gather information about the computer and automatically perform OS-specific troubleshooting steps such as find the specs.

__Note__: _The current version uses the ```keyboard``` and ```platform``` librarys instead of Pico Dukcky Code for now!

---

## ⭐ Features

- Auto-Detects OS (python only)
- Creates a text file with information such as:
    - ```systeminfo```, ```hostname```, Processor (type, cores, speed), Memory, Network & WIFI and top processes.
- Uses ```keyboard``` and ```platform```  for easy python running.
- Hopfully PicoDucky future release

---

## 🐍 How to run (python)

- Make sure python is installed

- Use ```git clone https://github.com/hippogriff101/DuckyDiagnostic``` or download ```main.py``` from the releases tab (under devlopment)

- Locate directory 

```
cd DuckyDiagnostic
```
or go the place where you saved ```main.py```

- Install all required dependenceys:

```
pip install keyboard platform
```

- Run ```main.py```

```
python main.py
```

(a ```.exe``` and PicoDucky compatible version is in development)

---

## 🧠 AI Transparency

Ai was used in this project to assist in debuging code and learning the ```powershell``` and ```terminal``` commands that the script uses.

## 💼 License

[_MIT License_](https://github.com/hippogriff101/DuckyDiagnostic/blob/main/LICENSE)

_Copyright (c) 2025 Freddie_

## Demo

(will upload later date)



