""" 
Distraction tool that will lock the keyboard
xinput should be installed on Linux for enabling this function to work
"""
import os
import time


def lockKeyboard():
    """
    This function will lock the keyboard on Linux machine then it will enable it
    """
    while True:
        # locks the keyboard for 5s
        # command: xinput float keyborad_ID
        os.system('xinput float 8')
        time.sleep(5)

        # Enable the keyboard fo 10s
        # command: xinput float keyborad_ID slave_keyboard_number
        os.system('xinput reattach 8 3')
        time.sleep(10)

def main():
    
    lockKeyboard()

main()
