#!/usr/bin/env python

# wipflag{todo}

from threading import Thread
from game import Game
from bytekeeper import ByteKeeper
from broker import Broker


class Main:
    def __init__(self):
        print('starting main...\n')
        self.set_running(True)
        self.bytekeeper = ByteKeeper()
        self.game = Game(self, self.bytekeeper)
        self.broker = Broker(self, self.bytekeeper)
        self.gamethread = Thread(target=self.game.run())
        self.brokerthread = Thread(target=self.broker.run())
        self.gamethread.start()
        self.brokerthread.start()

    def is_running(self):
        return self._running

    def set_running(self, running):
        self._running = running


if __name__ == "__main__":
    main = Main()
