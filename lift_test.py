from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from utils import (
    calibrate_front_lift_motor,
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
    # stationary_check()
    calibrate_front_lift_motor(lift_motor=front_lift_motor)
    front_lift_motor.run_target(speed=360, target_angle=90)

    drive_base.settings(straight_speed=50)

    # drive_base.straight(inches_to_mm(-2))
    # calibrate_lift_motor(lift_motor=back_lift_motor)
    front_lift_motor.run_target(speed=360, target_angle=270)

    drive_base.straight(inches_to_mm(-2))


    # front_lift_motor.run_target(speed=180, target_angle=-270)
    # back_lift_motor.run_target(speed=180, target_angle=-270 * 10)


if __name__ == "__main__":
    main()
