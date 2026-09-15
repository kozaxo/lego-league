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

    # calibrate lift mechanism
    calibrate_lift_motor(lift_motor=lift_motor)

    # drive to ship
    drive_base.straight((inches_to_mm(18)))

    # drop lift mechanism
    wait(sec_to_msec(0.125))
    lift_motor.run_target(speed=180, target_angle=0)

    # drive backwards from ship
    drive_base.straight((inches_to_mm(-8.5)))

    # lift motor out of way
    lift_motor.run_target(speed=180, target_angle=270)

    # turn left 90
    drive_base.turn(-90)

    # drive out from edge
    drive_base.straight((inches_to_mm(6)))

    # turn right 90
    drive_base.turn(90)

    # drive to lift ship
    drive_base.straight((inches_to_mm(14)))

    drive_base.straight((inches_to_mm(4)))

    # back away from ship to return to blue
    drive_base.straight((inches_to_mm(-5.5)))

    # turn left 45
    drive_base.turn(-45)

    drive_base.straight((inches_to_mm(6)))

    drive_base.turn(50)

    drive_base.straight((inches_to_mm(20)))

    drive_base.turn(15)

    drive_base.straight((inches_to_mm(28)))


if __name__ == "__main__":
    main()
