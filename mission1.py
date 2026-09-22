from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from utils import (
    calibrate_lift_motor,
    inches_to_mm,
    initialize,
    sec_to_msec,
    stationary_check,
)

hub = PrimeHub()


def main():
    drive_base, lift_motor = initialize()
    mission(drive_base=drive_base, lift_motor=lift_motor)


def mission(drive_base: DriveBase, lift_motor):
    stationary_check()

    # push up the drone
    drive_base.straight(inches_to_mm(22.5))

    # wait to make sure drone's up
    wait(sec_to_msec(1))

    # going back to home base
    drive_base.straight(inches_to_mm(-25))


if __name__ == "__main__":
    main()
