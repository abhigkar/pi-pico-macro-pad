import board
from indicator import LEDIndicator
#from kmk.extensions.statusled import statusLED
from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence

from kmk.keys import KC


keyboard = KMKKeyboard()

layers = Layers()
encoder_handler = EncoderHandler()

keyboard.modules = [layers, encoder_handler]
keyboard.extensions.append(MediaKeys())


encoder_handler.pins = ((board.GP5, board.GP4, board.GP3, False),)

keyboard.col_pins = (board.GP20,board.GP19,board.GP21)
keyboard.row_pins = (board.GP6,board.GP7,board.GP8,board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

led = LEDIndicator(
    led_pins=[board.GP12, board.GP13, board.GP14, board.GP15]
)

keyboard.extensions.append(led)

#statusLED = statusLED(led_pins=[board.GP12, board.GP13, board.GP14, board.GP15])
#keyboard.extensions.append(statusLED)


#Layers
LAYER1 = simple_key_sequence([KC.DF(0), KC.LED_ON(0)])
LAYER2 = simple_key_sequence([KC.TO(1), KC.LED_ON(1)])
LAYER3 = simple_key_sequence([KC.TO(2), KC.LED_ON(2)])
LAYER4 = simple_key_sequence([KC.TO(3), KC.LED_ON(3)])

#Zoom
END_ZOOM_MEETING = simple_key_sequence([KC.LALT(KC.Q),KC.ENTER])
CONTROL_VIDEO = KC.LALT(KC.V)
CONTROL_AUDIO = KC.LALT(KC.A)
CONTROL_SHARING = KC.LALT(KC.S)
#TAKE_SCREENSHOT = 

THRILLED_FACE = simple_key_sequence([KC.COLON,KC.MINUS,KC.LSHIFT(KC.D)])
FROG_FACE = send_string("(frogface)")

EXXCE_MERGE_CELL = simple_key_sequence([KC.LALT(KC.H), KC.LALT(KC.M),KC.LALT(KC.M)])

_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [
    # ZOOM Layerz`
    [
        XXXXXXX,		XXXXXXX,	LAYER2,
        XXXXXXX,	    FROG_FACE,	THRILLED_FACE,
        XXXXXXX,		XXXXXXX,	XXXXXXX,
        XXXXXXX,		XXXXXXX,	END_ZOOM_MEETING,    
    ],
    # NUM Layer
    [
        XXXXXXX,		KC.LGUI(KC.R),	LAYER3,
        KC.N1,			KC.N2,			KC.N3,  
        KC.N4,			KC.N5,			KC.N6,
        KC.N7,			KC.N8,			KC.N9,
    ],
     # FUN Layer
    [
        XXXXXXX,		KC.LGUI(KC.E),	LAYER4,
        KC.F1,			KC.F2,			KC.F3,
        KC.F4,			KC.F5,			KC.F6,
        KC.F7,			KC.F8,			KC.F9
    ],
    # UTIL Layer
    [
        XXXXXXX,		KC.LGUI(KC.E),	LAYER1,
        EXXCE_MERGE_CELL,			XXXXXXX,			XXXXXXX,
        XXXXXXX,			XXXXXXX,			XXXXXXX,
        XXXXXXX,			XXXXXXX,			XXXXXXX
    ],
]

encoder_handler.map = [ ((KC.VOLD, KC.VOLU, KC.AUDIO_MUTE),), # Standard
                         ((KC.VOLD, KC.VOLU, KC.AUDIO_MUTE),),
                         ((KC.VOLD, KC.VOLU, KC.AUDIO_MUTE),),
                         ((KC.VOLD, KC.VOLU, KC.AUDIO_MUTE),),
                        ]

if __name__ == '__main__':
    keyboard.go()