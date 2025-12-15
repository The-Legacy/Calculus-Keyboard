import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

class KeyboardHandler:
    """Manages USB HID keyboard comunication"""

    def __init__(self):
        self.kbd = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayoutUS(self.kbd)

    def send_text(self, text):
        """Type via USB HID
        
        Args: (str): Test/LaTeX string
        """
        self.layout.write(text)

    def send_keys(self, *keys):
        """
        Send keyboard key codes.
        
        Args:
            *keys: Key codes from keyboard module
        """
        self.kbd.press(*keys)
        self.kbd.release(*keys)