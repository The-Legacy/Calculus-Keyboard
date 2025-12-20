# ignore these warnings, the imports exist on a pico board just not here
import board
import digitalio
import time

#GPIO pin assignments for 9 buttons (using available Pico Pins)
BUTTON_PINS = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
]

DEBOUNCE_TIME = 0.5 # 20ms debounce

class ButtonHandler:
    
    def __init__(self):
        self.buttons = []
        self.last_pressed = {}
        self._init_buttons()

    def _init_buttons(self):
        """Initialize all button pins and inputs"""
        for i, pin in enumerate(BUTTON_PINS):
            btn = digitalio.DigitalInOut(pin)
            btn.direction = digitalio.Direction.INPUT
            btn.pull = digitalio.Pull.UP
            self.buttons.append(btn)
            self.last_pressed[i] = 0

    def check_buttons(self):
        """Check all buttons for presses that are debouncing due to quick inputs"""
        current_time = time.monotonic()

        for i, button in enumerate(self.buttons):
            if not button.value:
                if current_time - self.last_pressed[i] > DEBOUNCE_TIME:
                    self.last_pressed[i] = current_time
                    return i
        
        return None