from common import *
from time_quantity import second
from length import meter, kilometer
from time_quantity import second, hour
from common.measurement import Measurement

def main():
    print(Measurement(1, meter) + Measurement(1, kilometer))
    print(Measurement(1, meter) - Measurement(1, kilometer))
    print(Measurement(1, meter) * Measurement(2, hour))
    print(Measurement(1, meter) / Measurement(2, hour))

if __name__ == "__main__":
    main()