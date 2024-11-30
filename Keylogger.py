from pynput import keyboard, mouse
from datetime import datetime

def print_pressed_keys(key):
    log_event(f"Keyboard {key}")

def print_clicked_buttons(x, y, button, pressed):
    action = "pressed" if pressed else "released"
    log_event(f"Mouse {button} {action} at ({x}, {y})")

def log_event(event):
    timestamp = datetime.now()
    time_str = timestamp.strftime("%H %M %S")
    date_str = timestamp.strftime("%d %m %y")
    log_str = f"{time_str} {date_str} {event}\n"
    with open("event.log", "a") as f:
        f.write(log_str)

print("Listening for keyboard and mouse input...")

keyboard_listener = keyboard.Listener(on_press=print_pressed_keys)
mouse_listener = mouse.Listener(on_click=print_clicked_buttons)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()
