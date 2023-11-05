# Use this extension for showing layer status with three leds

import pwmio
import time

from kmk.extensions import Extension, InvalidExtensionEnvironment
from kmk.keys import make_argumented_key

class CustLedMeta:
    def __init__(self, led):
        self.led = led

class LEDIndicator(Extension):
    def __init__(
        self,
        led_pins,
        brightness=30,
        brightness_limit=100,
    ):
        self._leds = []
        for led in led_pins:
            try:
                self._leds.append(pwmio.PWMOut(led))
            except Exception as e:
                print(e)
                raise InvalidExtensionEnvironment(
                    'Unable to create pulseio.PWMOut() instance with provided led_pin'
                )
        self._led_count = len(self._leds)

        self.brightness = brightness

        self.brightness_limit = brightness_limit

        make_argumented_key(
            names=('LED_ON',),
            on_press=self._key_hndlr,
            validator=self._led_key_validator,
        )

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        '''Light up every single led once for 200 ms'''
        for i in range(self._led_count + 2):
            if i < self._led_count:
                self._leds[i].duty_cycle = int(self.brightness / 100 * 65535)
            i_off = i - 2
            if i_off >= 0 and i_off < self._led_count:
                self._leds[i_off].duty_cycle = int(0)
            time.sleep(0.1)
        for led in self._leds:
            led.duty_cycle = int(0)
        self._leds[0].duty_cycle = int(self.brightness / 100 * 65535)
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        self._layer_indicator(sandbox.active_layers[0])
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        self.set_brightness(0)
        return

    def on_powersave_disable(self, sandbox):
        return

    def set_brightness(self, percent, layer_id=-1):
        if layer_id < 0:
            for led in self._leds:
                led.duty_cycle = int(percent / 100 * 65535)
        else:
            self._leds[layer_id - 1].duty_cycle = int(percent / 100 * 65535)
    
    def _key_hndlr(self, led, *args, **kwargs):
        leds = range(0, len(self._leds))
        for i in leds:
            self._leds[i].duty_cycle = int(0)
        self._leds[led.meta.led].duty_cycle = int(self.brightness / 100 * 65535)
    
    def _led_key_validator(self, led):
        return CustLedMeta(led)