from adafruit_hid.keycode import Keycode

# Macro definitions for calculator keyboard
# Each button maps to either LaTeX or an action (hotkey, sequence, etc.)

MACROS = {
    # Button pin -> Macro definition
    0: {"type": "hotkey", "keys": [Keycode.CONTROL, Keycode.ALT, Keycode.ONE]},   # Sound 1
    1: {"type": "hotkey", "keys": [Keycode.CONTROL, Keycode.ALT, Keycode.TWO]},   # Sound 2
    2: {"type": "hotkey", "keys": [Keycode.CONTROL, Keycode.ALT, Keycode.THREE]}, # Sound 3
    3: r"4",      # Summation
    4: r"5",      # Product
    5: r"6",      # Infinity
    6: r"7",      # Partial Derivative
    7: r"8",      # Gradient
    8: r"9",      # Approx Equal
}

def get_macro(button_pin):
    """
    Get the macro for a given button pin
    
    Args:
        button_pin (int): GPIO pin number

    Returns:
        macro: LaTeX string or macro dict
    """
    return MACROS.get(button_pin)

def list_macros():
    """Display all available macros"""
    for pin, macro in MACROS.items():
        if isinstance(macro, dict) and macro.get("type") == "hotkey":
            print(f"Button {pin}: Hotkey {macro['keys']}")
        else:
            print(f"Button {pin}: {macro}")
