import smbus
import math
import time
import socket

########################
####### constants ######
########################

## bluetooth setup

def MAC_port():
    return 'B8:27:EB:16:7A:5C', 3

## Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
gyro_scale = 131.0
accel_scale = 16384.0
address = 0x68  # This is the address value read via the i2cdetect command


########################
### helper functions ###
########################

def read_all():
    raw_gyro_data = bus.read_i2c_block_data(address, 0x43, 6)
    raw_accel_data = bus.read_i2c_block_data(address, 0x3b, 6)

    gyro_scaled_x = twos_compliment((raw_gyro_data[0] << 8) + raw_gyro_data[1]) / gyro_scale
    gyro_scaled_y = twos_compliment((raw_gyro_data[2] << 8) + raw_gyro_data[3]) / gyro_scale
    gyro_scaled_z = twos_compliment((raw_gyro_data[4] << 8) + raw_gyro_data[5]) / gyro_scale

    accel_scaled_x = twos_compliment((raw_accel_data[0] << 8) + raw_accel_data[1]) / accel_scale
    accel_scaled_y = twos_compliment((raw_accel_data[2] << 8) + raw_accel_data[3]) / accel_scale
    accel_scaled_z = twos_compliment((raw_accel_data[4] << 8) + raw_accel_data[5]) / accel_scale

    return (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z)
    
def twos_compliment(val):
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a, b):
    return math.sqrt((a * a) + (b * b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def angle_to_percent(val):
    if val > 45:
        return 200
    elif val < -45:
        return 0
    return int(val * 100 / 45) + 100


def loop(s):
    i = 0
    
    while True:
        i += 1
        time.sleep(time_diff - 0.005) 
        
        (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z) = read_all()
        
        gyro_scaled_x -= gyro_offset_x
        gyro_scaled_y -= gyro_offset_y
        
        gyro_x_delta = (gyro_scaled_x * time_diff)
        gyro_y_delta = (gyro_scaled_y * time_diff)
    
        gyro_total_x += gyro_x_delta
        gyro_total_y += gyro_y_delta
    
        rotation_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
        rotation_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
    
        last_x = K * (last_x + gyro_x_delta) + (K1 * rotation_x)
        last_y = K * (last_y + gyro_y_delta) + (K1 * rotation_y)
        
        text = '' + str(angle_to_percent(rotation_x)) + ':' + str(angle_to_percent(rotation_y))
        if text == 'q':
            break
        if i % 20 == 0:
            print(text)
            s.send(bytes(text,'UTF-8'))
            i = 0



def main():
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect(MAC_port())

    bus = smbus.SMBus(1)  # or bus = smbus.SMBus(1) for Revision 2 boards
    
    # Now wake the 6050 up as it starts in sleep mode
    bus.write_byte_data(address, power_mgmt_1, 0)
    
    now = time.time()
    
    K = 0.98
    K1 = 1 - K
    
    time_diff = 0.01
    
    (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z) = read_all()
    
    last_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
    last_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
    
    gyro_offset_x = gyro_scaled_x 
    gyro_offset_y = gyro_scaled_y
    
    gyro_total_x = (last_x) - gyro_offset_x
    gyro_total_y = (last_y) - gyro_offset_y

    loop(s)

    s.close()



if __name__ == "__main__":
    main()

