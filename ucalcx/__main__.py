from common import *
from time_quantity import second, nanosecond
from length import meter, kilometer
from time_quantity import second, hour
from common.measurement import Measurement

def main():
    speed = Measurement(10, kilometer / hour)
    time = Measurement(2, hour)
    print(speed)
    print(speed.convert_to(meter / second))
    print(speed * time)
    print(speed / time)

if __name__ == "__main__":
    main()