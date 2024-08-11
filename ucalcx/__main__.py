from common import *
from time_quantity import second, nanosecond
from length import meter, kilometer
from time_quantity import second, hour
from common.measurement import Measurement

def main():
    velocity = Measurement(5, meter / second)
    time = Measurement(10, second)
    print(velocity * time)

if __name__ == "__main__":
    main()