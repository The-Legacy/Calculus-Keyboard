import time
from buttons import ButtonHandler
from keyboard import KeyboardHandler
from macros import get_macro

def main(): 
    """Main loop for calculator keyboard."""
    button_handler = ButtonHandler()
    keyboard_handler = KeyboardHandler()

    print("Calculator Keyboard Ready!")

    while True:
        pressed_button = button_handler.check_buttons()

        if pressed_button is not None:
            macro = get_macro(pressed_button)
            if macro:
                print(f"Button {pressed_button} pressed: {macro}")
                
                # Handle different macro types
                if isinstance(macro, dict):
                    if macro.get("type") == "hotkey":
                        # Send hotkey combination
                        keyboard_handler.send_hotkey(*macro["keys"])
                    elif macro.get("type") == "sequence":
                        # Send sequence of commands
                        keyboard_handler.execute_sequence(macro["sequence"])
                else:
                    # Send as text (LaTeX)
                    keyboard_handler.send_text(macro)
            else:
                print(f"Button {pressed_button} pressed but no macro defined")

        time.sleep(0.01)

if __name__ == "__main__":
    main()