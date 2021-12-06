#!/usr/bin/env python3

from trilobot import Trilobot, BUTTON_A

"""
TODO
"""
print("Trilobot Example: Avoid Walls\n")


SPEED = 0.7  # The speed to drive at
TURN_DISTANCE = 30  # How close a wall needs to be, in cm, before we start turning

tbot = Trilobot()

# Start moving forward
tbot.forward(SPEED)

while not tbot.read_button(BUTTON_A):
    distance = tbot.read_distance()

    # Turn if we are too closer than the turn distance
    if distance < TURN_DISTANCE:
        tbot.set_right_speed(-SPEED)
    else:
        tbot.set_right_speed(SPEED)
    # No sleep is needed, as distance sensor provides sleep
