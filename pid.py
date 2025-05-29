def PID_controller(sensor_readings):
    n_sensors = len(sensor_readings)

    pos = 0
    lasterr = 0
    kp,ki,kd = 0.07,0.0008,0.6  # adjustable values
    maxSpeed = 255

    for i in range(0,n_sensors):
        pos+=sensor_readings[i]*(i*1000)

    pos = pos/sum(sensor_readings)

    err = (n_sensors - 1)*500  - pos

    p = err
    i = err + i
    d = lasterr - err
    lasterr = err

    motorSpeed = p * kp + i * ki + d * kd
    # Considering 100 as base speed

    motorSpeedA = max(0, min(100 + motorSpeed, maxSpeed));
    motorSpeedB = max(0, min(100 - motorSpeed, maxSpeed));


    return motorSpeedA, motorSpeedB
