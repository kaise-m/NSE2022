# coding: utf-8
## @package faboMPU9250
#  This is a library for the FaBo 9AXIS I2C Brick.
#
#  http://fabo.io/202.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBo9Axis_MPU9250
import time
import sys
import csv
import datetime

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

DIFF_JST_FROM_UTC = 9
jp_time = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)

with open('mag_record_' + str(jp_time) + '.csv','w',newline='') as f: 
    writer = csv.writer(f)
    writer.writerow(["mag_x", "mag_y", "mag_z"])
f.close()

try:
    while True:
        accel = mpu9250.readAccel()
#         print(" ax = " , ( accel['x'] ))
#         print(" ay = " , ( accel['y'] ))
#         print(" az = " , ( accel['z'] ))

        gyro = mpu9250.readGyro()
#         print(" gx = " , ( gyro['x'] ))
#         print(" gy = " , ( gyro['y'] ))
#         print(" gz = " , ( gyro['z'] ))

        mag = mpu9250.readMagnet()
        print(" mx = " , ( mag['x']   ), end='')
        print(" my = " , ( mag['y']   ), end='')
        print(" mz = " , ( mag['z'] ))
        print()
        
        with open('mag_record_' + str(jp_time) + '.csv','a',newline='') as f: 
            writer = csv.writer(f)
            writer.writerow([mag['x'], mag['y'], mag['z']])
        f.close()
         
        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
