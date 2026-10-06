from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()


def inches_to_mm(inches):
    return inches * 25.4


def sec_to_msec(sec):
    return sec * 1000


def initialize() -> tuple[DriveBase, Motor]:
    # initialization
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.E)
    front_lift_motor = Motor(Port.D)
    back_lift_motor = Motor(Port.C)

    wheel_diameter = inches_to_mm(inches=3.375)
    axle_track = inches_to_mm(inches=5.875)
    straight_speed = 450  # [deg/s]
    turn_rate = 120  # [deg/s]

    drive_base = DriveBase(
        left_motor=left_motor,
        right_motor=right_motor,
        wheel_diameter=wheel_diameter,
        axle_track=axle_track,
    )
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=straight_speed, turn_rate=turn_rate)

    return drive_base, front_lift_motor, back_lift_motor


def calibrate_lift_motor(lift_motor):
    lift_motor.run_time(speed=-360, time=sec_to_msec(1))
    lift_motor.reset_angle(angle=0)
    lift_motor.run_target(speed=360, target_angle=270)


def calibrate_front_lift_motor(lift_motor):
    lift_motor.run_time(speed=-360, time=sec_to_msec(1))
    lift_motor.reset_angle(angle=0)


def stationary_check():
    while True:
        if hub.imu.stationary():
            wait(sec_to_msec(0.25))
            break
