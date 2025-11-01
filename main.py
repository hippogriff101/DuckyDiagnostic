import keyboard
import time

def main():
    while True:
        buttoninput = int(input("Press 1 for windows, 2 for linux and 3 for mac: "))

        if buttoninput == 1:
            windows()
            break
        elif buttoninput == 2:
            linux()
            break
        elif buttoninput == 3:
            mac()
            break
        else:
            print("Invalid input. Please try again.")

    time.sleep(1)
    keyboard.write("whoami > whoami.txt")
    keyboard.press_and_release("enter")
    time.sleep(0.5)
    keyboard.write("cat whoami.txt")
    keyboard.press_and_release("enter")

def windows():

    keyboard.press_and_release("win+r")
    time.sleep(0.5)
    keyboard.write("wt")
    keyboard.press_and_release("enter")


def linux():
    keyboard.press_and_release("ctrl+alt+t")

def mac():
    keyboard.press_and_release("cmd+space")
    time.sleep(0.5)
    keyboard.write("Terminal")
    keyboard.press_and_release("enter")

if __name__ == "__main__":
    main()