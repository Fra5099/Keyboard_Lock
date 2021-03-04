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
        os.system('xinput float 8')
        time.sleep(5)

        # Enable the keyboard fo 10s
        os.system('xinput reattach 8 3')
        time.sleep(10)

def main():
    
    lockKeyboard()

main()