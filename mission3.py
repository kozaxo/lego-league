from pybricks.hubs import PrimeHub
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
    drive_base, lift_motor = initialize()
    mission(drive_base=drive_base, lift_motor=lift_motor)


def mission(drive_base, lift_motor):
    stationary_check()
    calibrate_lift_motor(lift_motor=lift_motor)
    drive_base.straight(inches_to_mm(25))
    drive_base.turn(35)
    drive_base.straight(inches_to_mm(3))
    drive_base.turn(-80)
    drive_base.straight((inches_to_mm(3.5)))
    drive_base.turn(-45)
    wait(sec_to_msec(1))
    drive_base.straight(inches_to_mm(-1.5))
    drive_base.turn(-30)
    drive_base.straight(inches_to_mm(2))
    drive_base.turn(35)
    drive_base.straight(inches_to_mm(30))
    drive_base.turn(90)


if __name__ == "__main__":
    main()
