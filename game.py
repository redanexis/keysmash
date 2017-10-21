#!/usr/bin/env python

# wipflag {}

# Interfaces the libraries pygame and threading for our convenience.

import pygame
import time


class Game:
    def __init__(self, main, bytekeeper):
        print('starting events manager...\n')
        self.main = main
        self.bytekeeper = bytekeeper
        self.size = self.weight, self.height = 100, 100
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        #
        self.button_start = False
        self.button_y = False
        self.button_x = False
        self.button_b = False
        self.button_a = False
        self.button_l = False
        self.button_r = False
        self.button_z = False
        self.button_up = False
        self.button_down = False
        self.button_right = False
        self.button_left = False
        self.stick_x = 1
        self.stick_y = 1
        self.cstick_x = 1
        self.cstick_y = 1
        self.shoulder_l = 0
        self.shoulder_r = 0

    def on_loop(self):
        self.bytekeeper.update_byte(self.button_start,
                                    self.button_y,
                                    self.button_x,
                                    self.button_b,
                                    self.button_a,
                                    self.button_l,
                                    self.button_r,
                                    self.button_z,
                                    self.button_up,
                                    self.button_down,
                                    self.button_right,
                                    self.button_left,
                                    self.stick_x,
                                    self.stick_y,
                                    self.cstick_x,
                                    self.cstick_y,
                                    self.shoulder_l,
                                    self.shoulder_r)
        pygame.event.pump()
        time.sleep(0.008)  # todo performance check

    def on_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                elif event.key == pygame.K_RSHIFT:
                    self.button_z = True
                elif event.key == pygame.K_LEFT:
                    self.stick_y = 0
                elif event.key == pygame.K_RIGHT:
                    self.stick_y = 2
                elif event.key == pygame.K_a:
                    self.button_a = True
                elif event.key == pygame.K_b:
                    self.button_b = True
                elif event.key == pygame.K_x:
                    self.button_x = True
                elif event.key == pygame.K_y:
                    self.button_y = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pass
                elif event.key == pygame.K_RSHIFT:
                    self.button_z = False
                elif event.key == pygame.K_LEFT:
                    self.stick_y = 1
                elif event.key == pygame.K_RIGHT:
                    self.stick_y = 1
                elif event.key == pygame.K_a:
                    self.button_a = False
                elif event.key == pygame.K_b:
                    self.button_b = False
                elif event.key == pygame.K_x:
                    self.button_x = False
                elif event.key == pygame.K_y:
                    self.button_y = False
                elif event.key == pygame.K_ESCAPE:  # terminates program
                    self.main._running = False
                    print('>> esc <<')

    def cleanup(self):
        pygame.quit()

    def loop(self):
        while self.main.is_running():
            self.on_loop()
            self.on_events()
        self.cleanup()

    def run(self):  # threading
        print('starting events manager loop...\n')
        self.loop()
