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
    drive_base.straight(inches_to_mm(26))
    drive_base.turn(angle=-60)
    drive_base.straight(inches_to_mm(8))
    drive_base.turn(angle=-25)
    drive_base.straight(inches_to_mm(9))
    drive_base.turn(angle=-90)
    drive_base.straight(inches_to_mm(-2))
    lift_motor.run_target(speed=180, target_angle=0)
    wait(sec_to_msec(0.25))
    lift_motor.run_target(speed=180, target_angle=270)
    drive_base.straight(inches_to_mm(-1))
    drive_base.turn(angle=90)
    drive_base.straight(inches_to_mm(9))
    drive_base.turn(angle=-90)
    drive_base.straight(inches_to_mm(23.25))
    drive_base.turn(angle=270)
    drive_base.straight(inches_to_mm(9))
    drive_base.turn(angle=-90)
    drive_base.straight(inches_to_mm(-1.625))
    lift_motor.run_target(speed=180, target_angle=0)
    drive_base.straight(inches_to_mm(-1.75))
    drive_base.turn(75)
    lift_motor.run_target(speed=180, target_angle=270)
    drive_base.turn(-75)
    drive_base.straight(inches_to_mm(2))
    drive_base.turn(35)
    drive_base.straight(inches_to_mm(5))
    lift_motor.run_target(speed=180, target_angle=0)
    drive_base.straight(inches_to_mm(-4))
    drive_base.turn(55)
    drive_base.straight(inches_to_mm(30))


if __name__ == "__main__":
    main()
