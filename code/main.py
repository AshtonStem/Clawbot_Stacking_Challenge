myVariable = 0

def when_started1():
global myVariable
motor_8.spin_to_position(90, DEGREES)
if motor_8.is_done():
motor_8.stop()
drivetrain.drive_for(FORWARD, 11, INCHES)
motor_8.spin_to_position(90, DEGREES)
if motor_8.is_done():
motor_8.stop()
Up_down.spin_for(FORWARD, 180, DEGREES)
drivetrain.drive_for(REVERSE, 10, INCHES)
drivetrain.turn_for(RIGHT, 180, DEGREES, wait=False)
drivetrain.drive_for(FORWARD, 11, INCHES)
motor_8.spin_to_position(90, DEGREES)
if motor_8.is_done():
motor_8.stop()
drivetrain.drive_for(REVERSE, 10, INCHES)
drivetrain.turn_for(RIGHT, 180, DEGREES, wait=False)
drivetrain.stop()

when_started1()
