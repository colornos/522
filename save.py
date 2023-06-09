from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

reader = SimpleMFRC522()

def save_to_file(id):
    with open("rfid.txt", "w") as file:
        file.write(f"{id}\n")

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id, text))
        save_to_file(id)
        sleep(5)
except KeyboardInterrupt:
    print("Program terminated")
    GPIO.cleanup()
    sys.exit()
