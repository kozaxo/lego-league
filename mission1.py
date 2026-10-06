from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from utils import (
    calibrate_lift_motor,
    inches_to_mm,
    initialize,
    sec_to_msec,
    stationary_check,
)

hub = PrimeHub()


def main():
    drive_base, front_lift_motor, back_lift_motor = initialize()
    mission(
        drive_base=drive_base,
        front_lift_motor=front_lift_motor,
        back_lift_motor=back_lift_motor,
    )


def mission(drive_base: DriveBase, front_lift_motor: Motor, back_lift_motor: Motor):
    stationary_check()

    # push up the drone
    drive_base.straight(inches_to_mm(24.5))

    # wait to make sure drone's up
    wait(sec_to_msec(1))

    # going back to home base
    drive_base.straight(inches_to_mm(-26))


if __name__ == "__main__":
    main()
