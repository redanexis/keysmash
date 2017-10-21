#!usr/bin/env python

# wipflag{}
# Keeps and updates the bytearray containing the virtual controller state.


class ByteKeeper:
    def __init__(self):
        print('starting bytekeeper...\n')
        # send-ready format byte
        self.readybytelist = []

        self.bytes_empty = [  # tuples are faster...?
            #  pls mind transmission order (<-) & (\/)
            0b10001000100010001000100010001000,  # buttons (A B X Y Start 0 0 0)
            0b10001000100010001000100010001110,  # buttons (D<, D>, Dv, D^, Z, R, L, 1)
            0b10001000100010001000100010001000,  # Stick X value. todo currently value 1 for testing purposes
            0b11101000100010001000100010001000,  # Stick Y value
            0b11101000100010001000100010001000,  # Cstick X value
            0b11101000100010001000100010001000,  # Cstick Y value
            0b10001000100010001000100010001000,  # Left shoulder
            0b10001000100010001000100010001000]  # Right shoulder

        self.bytes_current = self.bytes_empty

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
        self.analog_values = {0: 0b11101000100010001000100010001000,
                              1: 0b11101000100010001000100010001000,
                              2: 0b11101110111011101110111011101110}

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
                    stick_x=1,
                    stick_y=1,
                    cstick_x=1,
                    cstick_y=1,
                    shoulder_l=0,
                    shoulder_r=0
                    ):
        self.bytes_current = self.bytes_empty

        if button_start:
            self.bytes_current[0] |= self.button_start
        if button_y:
            self.bytes_current[0] |= self.button_y
        if button_x:
            self.bytes_current[0] |= self.button_x
        if button_b:
            self.bytes_current[0] |= self.button_b
        if button_a:
            self.bytes_current[0] |= self.button_a
        if button_l:
            self.bytes_current[1] |= self.button_l
        if button_r:
            self.bytes_current[1] |= self.button_r
        if button_z:
            self.bytes_current[1] |= self.button_z
        if button_up:
            self.bytes_current[1] |= self.button_up
        if button_down:
            self.bytes_current[1] |= self.button_down
        if button_right:
            self.bytes_current[1] |= self.button_right
        if button_left:
            self.bytes_current[1] |= self.button_left
        # 0 == False, 1 && 2 && 3(...) == True
        if stick_x:
            self.bytes_current[2] |= self.analog_values[stick_x]
        if stick_y:
            self.bytes_current[3] |= self.analog_values[stick_y]
        if cstick_x:
            self.bytes_current[4] |= self.analog_values[cstick_x]
        if cstick_y:
            self.bytes_current[5] |= self.analog_values[cstick_y]
        if shoulder_l:
            self.bytes_current[6] |= self.analog_values[shoulder_l]
        if shoulder_r:
            self.bytes_current[7] |= self.analog_values[shoulder_r]

        #  do the thing
        bytelist = []
        for x in self.bytes_current:
            bytelist += (x.to_bytes(length=4, byteorder='big'))
        self.readybytelist = bytelist
        # </the thing>

    def get_bytes(self):
        return self.readybytelist
