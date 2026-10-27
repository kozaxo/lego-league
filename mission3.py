from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from utils import (
    calibrate_front_lift_motor,
    calibrate_rear_lift_motor,
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

    # raising the hook to get it out of the way
    #front_lift_motor.run_time(speed=-360, time=sec_to_msec(1))
    
    #calibrate_rear_lift_motor(lift_motor=back_lift_motor)
    #back_lift_motor.run_until_stalled(speed=10000,then=Stop.COAST, duty_limit=20)
    #back_lift_motor.run_angle(speed=10000,rotation_angle=360)
    
    back_lift_motor.run_angle(speed=-1000,rotation_angle=2300)
    #drive_base.straight(inches_to_mm(-2))
    back_lift_motor.run_angle(speed=2000, rotation_angle=2300)
    #back_lift_motor.run_until_stalled(1000, duty_limit=25)
    #calibrate_rear_lift_motor(lift_motor=back_lift_motor)
    # drive forward past the rock
    #drive_base.straight(inches_to_mm(15))

    # lowering hook over rock stick
    #front_lift_motor.run_target(speed=360, target_angle=270)

    # go backward
    #drive_base.straight(inches_to_mm(-5))

    # raising the hook to flip the rock the second time.
    #calibrate_front_lift_motor(lift_motor=front_lift_motor)

    #drive_base.straight(inches_to_mm(5))

    #front_lift_motor.run_target(speed=360, target_angle=270)

    #drive_base.straight(inches_to_mm(-20))


    # drive_base.straight(inches_to_mm(-2))

    # front_lift_motor.run_target(speed=360, target_angle=275)

    # drive_base.straight(inches_to_mm(-2))

    # front_lift_motor.run_target(speed=360, target_angle=165)


if __name__ == "__main__":
    main()
