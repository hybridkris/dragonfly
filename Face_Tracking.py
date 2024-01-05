import sensor, image, time, pyb

# Set up the sensor
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

# Load Haar Cascade
face_cascade = image.HaarCascade("frontalface", stages=25)
clock = time.clock()

# LED setup for indicating face detection
red_led = pyb.LED(1)

# Define the color pink in RGB565
green = (0, 180, 0)



while(True):
    clock.tick()
    img = sensor.snapshot()

    # Detect faces
    faces = img.find_features(face_cascade, threshold=0.75, scale_factor=1.25)

    for face in faces:
        # Draw rectangles around detected faces in green color
        img.draw_rectangle(face, color=green)

        # Turn on the red LED when a face is detected
        red_led.on()

    # Turn off the LED when no faces are detected
    if not faces:
        red_led.off()

    # Print frame rate
    print(clock.fps())
