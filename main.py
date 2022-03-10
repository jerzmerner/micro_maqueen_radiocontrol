def on_received_string(receivedString):
    global angle, R, G, B
    if receivedString == "Open":
        if angle > 0:
            angle += -1
            maqueen.servo_run(maqueen.Servos.S1, angle)
    elif receivedString == "Close":
        if angle < 180:
            angle += 1
            maqueen.servo_run(maqueen.Servos.S1, angle)
    elif receivedString == "LEDL":
        if pins.digital_read_pin(DigitalPin.P8) == 1:
            maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        else:
            maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    elif receivedString == "LEDR":
        if pins.digital_read_pin(DigitalPin.P12) == 1:
            maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
        else:
            maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    elif receivedString == "Honk":
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P0, 0)
        basic.pause(200)
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P0, 0)
    elif receivedString == "neoPixelR":
        R += 24
    elif receivedString == "neoPixelG":
        G += 24
    elif receivedString == "neoPixelB":
        B += 24
    elif receivedString == "showOff":
        music.play_melody("E B C5 A B G A F ", 238)
        maqueen.servo_run(maqueen.Servos.S1, 10)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 255)
        for index in range(255):
            maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
            maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
            B += 1
            G += -1
            strip.show_color(neopixel.colors(neopixel.rgb(R, G, B)))
            basic.pause(1)
            maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
            maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
        for index2 in range(255):
            maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
            maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
            G += 1
            R += -1
            strip.show_color(neopixel.colors(neopixel.rgb(R, G, B)))
            basic.pause(1)
            maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
            maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
        maqueen.motor_stop(maqueen.Motors.ALL)
    elif receivedString == "Honk":
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.pause(200)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    else:
        pass
    strip.show_color(neopixel.colors(neopixel.rgb(R, G, B)))
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    if name == "lMotor":
        if value > 0:
            serial.write_value("lForw", value)
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, value)
        else:
            serial.write_value("lBack", value)
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, abs(value))
    if name == "rMotor":
        if value > 0:
            serial.write_value("rForw", value)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, value)
        else:
            serial.write_value("rBack", value)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, abs(value))
radio.on_received_value(on_received_value)

strip: neopixel.Strip = None
angle = 0
B = 0
G = 0
R = 0
radio.set_group(1)
angle = 80
maqueen.servo_run(maqueen.Servos.S1, angle)
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)