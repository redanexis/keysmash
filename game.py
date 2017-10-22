#!/usr/bin/env python

# wipflag {}

# Interfaces the libraries pygame and threading for our convenience.
# Events manager.

import pygame
import time


class Game:
    def __init__(self, main, bytekeeper):
        print('starting events manager...')
        self.main = main
        self.bytekeeper = bytekeeper
        self.size = self.weight, self.height = 100, 100
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

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
        self.stick_x = 0
        self.stick_y = 0
        self.cstick_x = 0
        self.cstick_y = 0
        self.shoulder_l = 0
        self.shoulder_r = 0

    def on_loop(self):
        self.bytekeeper.update_byte(button_start=self.button_start,
                                    button_y=self.button_y,
                                    button_x=self.button_x,
                                    button_b=self.button_b,
                                    button_a=self.button_a,
                                    button_l=self.button_l,
                                    button_r=self.button_r,
                                    button_z=self.button_z,
                                    button_up=self.button_up,
                                    button_down=self.button_down,
                                    button_right=self.button_right,
                                    button_left=self.button_left,
                                    stick_x=self.stick_x,
                                    stick_y=self.stick_y,
                                    cstick_x=self.cstick_x,
                                    cstick_y=self.cstick_y,
                                    shoulder_l=self.shoulder_l,
                                    shoulder_r=self.shoulder_r)
        print(self.bytekeeper.get_bytes().hex())
        time.sleep(0.5)  # todo performance check (0.008 was working)
        pygame.event.pump()

    def on_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                elif (event.key == pygame.K_RSHIFT) or (event.key == pygame.K_LSHIFT):
                    self.button_z = True
                elif event.key == pygame.K_KP5:
                    self.stick_x = 1
                elif event.key == pygame.K_KP8:
                    self.stick_x = 2
                elif event.key == pygame.K_KP4:
                    self.stick_y = 1
                elif event.key == pygame.K_KP6:
                    self.stick_y = 2
                elif event.key == pygame.K_a:
                    self.button_a = True
                elif event.key == pygame.K_s:
                    self.button_b = True
                elif event.key == pygame.K_d:
                    self.button_start = True
                elif event.key == pygame.K_f:
                    self.button_x = True
            if event.type == pygame.KEYUP:  # set stuff back to neutral (0 or False)
                if event.key == pygame.K_SPACE:
                    pass
                elif (event.key == pygame.K_RSHIFT) or (event.key == pygame.K_LSHIFT):
                    self.button_z = False
                elif event.key == pygame.K_KP5:
                    self.stick_x = 0
                elif event.key == pygame.K_KP8:
                    self.stick_x = 0
                elif event.key == pygame.K_KP4:
                    self.stick_y = 0
                elif event.key == pygame.K_KP6:
                    self.stick_y = 0
                elif event.key == pygame.K_a:
                    self.button_a = False
                elif event.key == pygame.K_s:
                    self.button_b = False
                elif event.key == pygame.K_d:
                    self.button_start = False
                elif event.key == pygame.K_f:
                    self.button_x = False

                elif event.key == pygame.K_ESCAPE:  # terminates program
                    self.main.running = False
                    print('>esc<')
                else:
                    print(event)  # print event keys

    def cleanup(self):
        pygame.quit()

    def loop(self):
        while self.main.running:
            self.on_loop()
            self.on_events()
        self.cleanup()

    def run(self):  # threading
        print('starting events manager loop...')
        self.loop()
