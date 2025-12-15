import sys
import os

# Mock modules for testing
class MockPin:
    def __init__(self, name):
        self.name = name

class MockBoard:
    GP0 = MockPin("GP0")
    GP1 = MockPin("GP1")
    GP2 = MockPin("GP2")
    GP3 = MockPin("GP3")
    GP4 = MockPin("GP4")
    GP5 = MockPin("GP5")
    GP6 = MockPin("GP6")
    GP7 = MockPin("GP7")
    GP8 = MockPin("GP8")

class MockDigitalInOut:
    Direction = type('Direction', (), {'INPUT': 'INPUT', 'OUTPUT': 'OUTPUT'})
    Pull = type('Pull', (), {'UP': 'UP', 'DOWN': 'DOWN'})

    def __init__(self, pin):
        self.pin = pin
        self.direction = None
        self.pull = None
        self.value = True #sims unpressed btn

    def set_pressed(self):
        self.value = False

class MockKeyboard:
    def __init__(self, devices):
        self.devices = devices

    def press(self, *keys):
        pass

    def release(self, *keys):
        pass

class MockKeyboardLayoutUS:
    def __init__(self, kbd):
        self.kbd = kbd
        self.history = []

    def write(self, text):
        self.history.append(text)
        print(f"[MOCK] Typed: {text}")

# Inject mocks
sys.modules['board'] = MockBoard()
sys.modules['digitalio'] = type('digitalio', (), {
    'DigitalInOut': MockDigitalInOut,
    'Direction': MockDigitalInOut.Direction,
    'Pull': MockDigitalInOut.Pull
})()
sys.modules['usb_hid'] = type('usb_hid', (), {'devices': []})()
sys.modules['adafruit_hid'] = type('adafruit_hid', (), {})()
sys.modules['adafruit_hid.keyboard'] = type('keybaord', (), {'Keyboard': MockKeyboard})()
sys.modules['adafruit_hid.keyboard_layout_us'] = type('layout', (), {'KeyboardLayoutUS': MockKeyboardLayoutUS})()

# Now import and test
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from buttons import ButtonHandler
from keyboard import KeyboardHandler
from macros import get_macro

def test_macros():
    """Test macro definitions"""
    print("\n=== Testing Macros ===")
    for i in range(9):
        macro = get_macro(i)
        print(f"Button {i}: {macro}")

def test_keyboard_input():
    """Test button presses and text output"""
    print("\n=== Test button presses and text output")
    button_handler = ButtonHandler()
    keyboard_handler = KeyboardHandler()

    # Simulate pressing button 0
    button_handler.buttons[0].set_pressed()
    pressed = button_handler.check_buttons()
    if pressed is not None:
        macro = get_macro(pressed)
        keyboard_handler.send_text(macro)
        print(f"Button {pressed} sent: {macro}")

if __name__ == "__main__":
    test_macros()
    test_keyboard_input()
    print("\n All tests passed!")