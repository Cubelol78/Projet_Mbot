# (c) 2020 Christophe Gueneau
import microbit
import machine
import time


class Robot:
    def __init__(self):
        self._vit = 0
        microbit.i2c.init(freq=100000, sda=microbit.pin20, scl=microbit.pin19)

    def run(self, mot, sens, vit):
        buf = bytearray(3)
        if mot == 0:
            buf[0] = 0x00
        else:
            buf[0] = 0x02
        buf[1] = sens
        buf[2] = vit
        microbit.i2c.write(0x10, buf)

    def stop(self):
        self.run(0, 0, 0)
        self.run(1, 0, 0)

    def run2(self, vit, dir):
        # 128=0 et mise échelle 255
        vitp = (vit - 128) * 255 / 127
        dirp = (dir - 128) * 255 / 127

        # vitesses moteurs
        vit0 = vitp - dirp
        vit1 = vitp + dirp

        # mini 0 maxi 255
        if vit >= 128:
            vit0 = max(0, min(vit0, 255))
            vit1 = max(0, min(vit1, 255))
        else:
            vit0 = min(0, max(-255, vit0))
            vit1 = min(0, max(-255, vit1))

        # sens rotation
        if vit0 < 0:
            vit0 = abs(vit0)
            sens0 = 1
        else:
            sens0 = 0

        if vit1 < 0:
            vit1 = abs(vit1)
            sens1 = 1
        else:
            sens1 = 0

        print("vit=", vit, " dir=", dir, "vitp", vitp, " dirp", dirp," vit0=", vit0, " s0=", sens0, " vit1=", vit1, " s1=", sens1)
        self.run(0, sens0, int(vit0))
        self.run(1, sens1, int(vit1))

    def distance(self):
        microbit.pin1.write_digital(1)
        time.sleep_ms(10)
        microbit.pin1.write_digital(0)
        microbit.pin2.read_digital()
        t = machine.time_pulse_us(microbit.pin2, 1)
        dist = 340 * t / 20000
        return dist


