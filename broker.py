#!usr/bin/env python

# wipflag{todo}

# Interfaces library PySerial for our convenience.

import serial


class Broker:
    def __init__(self, main, bytekeeper):
        print('starting broker...')
        self.main = main
        self.bytekeeper = bytekeeper
        self.port = serial.Serial(port='/dev/ttyUSB0',
                                  baudrate=1000000,
                                  # bytesize=serial.EIGHT_BITS,
                                  # parity=serial.PARITY_NONE,
                                  # stopbits=serial.STOPBITS_ONE,
                                  timeout=0.006,
                                  # xonxoff=False,
                                  # rtscts=False,
                                  # write_timeout=None,
                                  # dsrdtr=False,
                                  # inter_byte_timeout=None
                                  )
        print(f'successfully created port {self.port.name}.')

    def handshake(self):
        print('attempting handshake...')
        self.port.read(255)  # raw read call
        self.port.reset_input_buffer()  # gets rid of the stop bit?
        self.send_button_data()

    def send_button_data(self):
        payload = self.bytekeeper.get_bytes()
        print(f'sending: {payload.hex()}')
        self.port.write(payload)
        self.port.write(0b1110)  # stop bit? 0111? todo

    def read(self):
        msg = self.port.read(255)  # 12 = 24bits question word * 4 / 8 # todo performance check of timeout
        print(f'reading: {msg.hex()}')

    def run(self):
        print('starting broker loop...\n')
        self.handshake()
        while self.main.running:
            self.read()
            self.send_button_data()
