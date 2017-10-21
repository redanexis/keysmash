#!usr/bin/env python

# wipflag{}

# Interfaces library PySerial for our convenience.

import serial


class Broker:
    def __init__(self, main, bytekeeper):
        print('starting broker...\n')
        self.main = main
        self.bytekeeper = bytekeeper
        self.port = serial.Serial(port='/dev/ttyUSB0',
                                  baudrate=1000000,
                                  # bytesize=serial.EIGHT_BITS,
                                  # parity=serial.PARITY_NONE,
                                  # stopbits=serial.STOPBITS_ONE,
                                  timeout=0.004,
                                  # xonxoff=False,
                                  # rtscts=False,
                                  # write_timeout=None,
                                  # dsrdtr=False,
                                  # inter_byte_timeout=None
                                  )
        print(f'successfully created port {self.port.name}.\n')

    def handshake(self):
        print('attempting handshake...\n')
        self.port.read(8)  # raw read call
        self.port.reset_input_buffer()  # gets rid of the stop bit?
        self.send_button_data()

    def send_button_data(self):
        payload = self.bytekeeper.get_bytes()
        print(f'sending: {payload}\n')
        self.port.write(payload)
        self.port.write(0b1111)  # stop bit?

    def read(self):
        msg = self.port.read(12)  # 12 = 24bits question word * 4 / 8 # todo performance check of timeout
        print(f'reading: {msg}\n')

    def run(self):
        print('starting broker loop...\n')
        self.handshake()
        while self.main.is_running():
            self.read()
            self.send_button_data()
