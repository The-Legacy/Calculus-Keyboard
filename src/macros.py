# LaTeX macro definitions for calculator keyboard
# Each button maps to a LaTeX command

MACROS = {
    # Button pin -> Latex String
    0: r"\int",      # Integral
    1: r"\frac{}{}", # Fraction
    2: r"\sqrt",     # Square Root
    3: r"\sum",      # Summation
    4: r"\prod",     # Product
    5: r"\infty",    # Infinity
    6: r"\partial",  # Partial Derivative
    7: r"\nable",    # Gradient
    9: r"\approx",   # Aprrox Equal
}

def get_macro(button_pin):
    """
    Get the LaTeX macro for a given button pi
    
    Args: button_pin (int): GPIO pin number

    Return LaTeX macro
    """

    return MACROS.get(button_pin)

def list_macros():
    """Display all available macros"""
    for pin, macro in MACROS.items():
        print(f"Button {pin}, {macro}")
