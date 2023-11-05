import board
import digitalio

led = digitalio.DigitalInOut(board.GP15)
led.direction =digitalio.Direction.OUTPUT
digitalio.Direction.OUTPUT

def led_on(on):
    led.value = bool(on)
