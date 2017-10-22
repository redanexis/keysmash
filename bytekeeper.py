#!usr/bin/env python

# wipflag{}
# Keeps and updates the bytearray containing the virtual controller state.


class ByteKeeper:
    def __init__(self):
        print('starting bytekeeper...')

        # ready-to-send bytes
        self.readybytelist = []
        self.bytes_empty = (  # tuples are faster...?
            #  pls mind transmission order (<-) & (/\)
            0b10001000100010001000100010001000,  # Right shoulder; defaults to 0
            0b10001000100010001000100010001000,  # Left shoulder; defaults to 0
            0b11101000100010001000100010001000,  # Cstick Y value; defaults to 128
            0b11101000100010001000100010001000,  # Cstick X value; defaults to 128
            0b11101000100010001000100010001000,  # Stick Y value; defaults to 128
            0b11101000100010001000100010001000,  # Stick X value;
            0b10001000100010001000100010001110,  # buttons (D<, D>, Dv, D^, Z, R, L, 1)
            0b10001000100010001000100010001000)  # buttons (A B X Y Start 0 0 0)

        self.bytes_current = list(self.bytes_empty)

        # face
        self.button_start = 0b10001000100010001110100010001000
        self.button_y = 0b10001000100011101000100010001000
        self.button_x = 0b10001000111010001000100010001000
        self.button_b = 0b10001110100010001000100010001000
        self.button_a = 0b11101000100010001000100010001000

        self.button_l = 0b10001000100010001000100011101110
        self.button_r = 0b10001000100010001000111010001110
        self.button_z = 0b10001000100010001110100010001110
        self.button_up = 0b10001000100011101000100010001110
        self.button_down = 0b10001000111010001000100010001110
        self.button_right = 0b10001110100010001000100010001110
        self.button_left = 0b11101000100010001000100010001110
        self.stick_analog_values = {0: 0b11101000100010001000100010001000,  # default, mid-range value, do not update
                                    1: 0b10001000100010001000100010001000,  # zero value
                                    2: 0b11101110111011101110111011101110}  # max value
        self.shoulder_analog_values = {0: 0b10001000100010001000100010001000,  # default, zero value, do not update
                                       1: 0b11101110111011101110111011101110}  # max value

    def update_byte(self,
                    button_start=False,
                    button_y=False,
                    button_x=False,
                    button_b=False,
                    button_a=False,
                    button_l=False,
                    button_r=False,
                    button_z=False,
                    button_up=False,
                    button_down=False,
                    button_right=False,
                    button_left=False,
                    stick_x=0,
                    stick_y=0,
                    cstick_x=0,
                    cstick_y=0,
                    shoulder_l=0,
                    shoulder_r=0
                    ):

        self.bytes_current = list(self.bytes_empty)

        if button_start:
            self.bytes_current[7] |= self.button_start
        if button_y:
            self.bytes_current[7] |= self.button_y
        if button_x:
            self.bytes_current[7] |= self.button_x
        if button_b:
            self.bytes_current[7] |= self.button_b
        if button_a:
            self.bytes_current[7] |= self.button_a
        if button_l:
            self.bytes_current[6] |= self.button_l
        if button_r:
            self.bytes_current[6] |= self.button_r
        if button_z:
            self.bytes_current[6] |= self.button_z
        if button_up:
            self.bytes_current[6] |= self.button_up
        if button_down:
            self.bytes_current[6] |= self.button_down
        if button_right:
            self.bytes_current[6] |= self.button_right
        if button_left:
            self.bytes_current[6] |= self.button_left
        if stick_x:
            self.bytes_current[5] = self.stick_analog_values[stick_x]
        if stick_y:
            self.bytes_current[4] = self.stick_analog_values[stick_y]
        if cstick_x:
            self.bytes_current[3] = self.stick_analog_values[cstick_x]
        if cstick_y:
            self.bytes_current[2] = self.stick_analog_values[cstick_y]
        if shoulder_l:
            self.bytes_current[1] = self.shoulder_analog_values[shoulder_l]
        if shoulder_r:
            self.bytes_current[0] = self.shoulder_analog_values[shoulder_r]
        # do the thing
        self.the_thing()

    # the thing todo fix this
    def the_thing(self):
        bytelist = []
        for x in self.bytes_current:
            bytelist += (x.to_bytes(length=4, byteorder='big'))
        self.readybytelist = bytes(bytelist)

    def get_bytes(self):
        return self.readybytelist
