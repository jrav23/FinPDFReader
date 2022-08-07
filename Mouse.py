import threading

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.keyboard import Listener, KeyCode

delay = 0.31
keyboard_delay = 1
button = Button.left
start_stop_key = KeyCode(char=']')
start_stop_cirlces = KeyCode(char='[')https://www.espn.com/nfl/boxscore/_/gameId/401326636

exit_key = KeyCode(char=';')


class ClickMouse(threading.Thread):
    print('Welcome to the ClickMouse Auto Click Bot! \n\nCurrent delay setting for the click function is: {} seconds between clicks \n\nIn order to Start/Stop the Auto Click function- \n-Press the {} key \n\nTo exit the program- \n-Press the {} key \n\nEnjoy!\n\n\n~~Created by CrudeExistence.'.format(delay,start_stop_key,exit_key))
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

