radio.onReceivedString(function (receivedString) {
    if (receivedString == "Open") {
        if (angle > 0) {
            angle += -1
            maqueen.servoRun(maqueen.Servos.S1, angle)
        }
    } else if (receivedString == "Close") {
        if (angle < 98) {
            angle += 1
            maqueen.servoRun(maqueen.Servos.S1, angle)
        }
    } else if (receivedString == "LEDL") {
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    } else if (receivedString == "LEDR") {
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    } else if (receivedString == "neoPixelR") {
        R += 24
    } else if (receivedString == "neoPixelG") {
        G += 24
    } else if (receivedString == "neoPixelB") {
        B += 24
    } else if (receivedString == "showOff") {
        music.playMelody("C5 C B E A F G A ", 500)
        maqueen.servoRun(maqueen.Servos.S1, 10)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 255)
        for (let index = 0; index < 255; index++) {
            maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
            maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
            B += 1
            G += -1
            strip.showColor(neopixel.colors(neopixel.rgb(R, G, B)))
            basic.pause(1)
            maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
            maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
        }
        maqueen.motorStop(maqueen.Motors.All)
    } else if (receivedString == "Hiii") {
        music.playMelody("C E G C5 E G D C5 ", 1595)
        basic.showString("What is up?")
        music.playMelody("E D C E D E F G ", 120)
    } else {
    	
    }
    strip.showColor(neopixel.colors(neopixel.rgb(R, G, B)))
})
radio.onReceivedValue(function (name, value) {
    if (name == "lMotor") {
        if (value > 0) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, value)
        } else {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, Math.abs(value))
        }
    }
    if (name == "rMotor") {
        if (value > 0) {
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, value)
        } else {
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, Math.abs(value))
        }
    }
})
let strip: neopixel.Strip = null
let angle = 0
let R = 0
let G = 0
let B = 0
radio.setGroup(1)
angle = 80
maqueen.servoRun(maqueen.Servos.S1, angle)
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
basic.forever(function () {
    serial.writeValue("yAccel", input.acceleration(Dimension.Y))
})
control.inBackground(function () {
	
})
