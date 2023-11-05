import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.GP6,board.GP7,board.GP8,board.GP9)
    col_pins = (board.GP20,board.GP19,board.GP21)
    diode_orientation = DiodeOrientation.COL2ROW