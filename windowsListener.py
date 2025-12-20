import keyboard
import os

# Map hotkeys to sound files
SOUNDS = {
    'ctrl+alt+1': r"C:\Users\logan\OneDrive\Documents\Event_Listeners\mp3s\Christmas1.mp3",
    'ctrl+alt+2': r"C:\Users\logan\OneDrive\Documents\Event_Listeners\mp3s\Christmas2.mp3",
    'ctrl+alt+3': r"C:\Users\logan\OneDrive\Documents\Event_Listeners\mp3s\Christmas3.mp3",
}

def play_sound(sound_file):
    """Play a sound file using Windows Media Player"""
    try:
        # Use os.startfile to open with default media player
        os.startfile(sound_file)
        print(f"Playing: {sound_file}")
    except Exception as e:
        print(f"Error playing sound: {e}")

# Register all hotkeys
for hotkey, sound_file in SOUNDS.items():
    keyboard.add_hotkey(hotkey, lambda s=sound_file: play_sound(s))

print("Sound listener running...")
print("Button 0 (Ctrl+Alt+1) -> Christmas1")
print("Button 1 (Ctrl+Alt+2) -> Christmas2")
print("Button 2 (Ctrl+Alt+3) -> Christmas3")
print("Press Ctrl+C to stop")

keyboard.wait()