from auto_typing.motor_control import motor_cpp
import time

controller = motor_cpp.MotorController(2)

print("Initializing motor...")
controller.init()

def run_for_duration(duration_seconds, func, rate_hz=10, *args, **kwargs):
    interval = 1.0 / rate_hz
    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        loop_start = time.time()
        func(*args, **kwargs)
        elapsed = time.time() - loop_start
        sleep_time = max(0, interval - elapsed)
        time.sleep(sleep_time)

def run_motor():
    controller.run(-1., 50)

run_for_duration(10, run_motor, rate_hz=20)

